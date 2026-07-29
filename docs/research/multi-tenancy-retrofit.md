# Multi-Tenancy Retrofit: SurrealDB Native Permissions vs. Application-Layer Scoping

Research for issue [#9](https://github.com/danieldannhofer-gif/open-notebook-school/issues/9).
Date: 2026-07-29. Repo state: `main` @ `cac4e01`.

---

## Answer

**Recommendation: enforce tenancy in the application, at a narrowed repository layer. Do not adopt SurrealDB record-level permissions as the primary control on this stack.**

The decision is forced by a version fact, not a preference:

- This project pins **SurrealDB v2** (`docker-compose.yml:4`, `Dockerfile.single:26`).
- **GHSA-vjjx-rfw4-rmfc**: graph traversal (`->edge->`) bypassed table `PERMISSIONS FOR select` entirely in **all versions before 3.1.0**. Fixed only in 3.1.0.
- This app's *entire* data model is graph traversal. Sources and notes are reached from notebooks via `->reference->` and `->artifact->` edges (`open_notebook/domain/notebook.py:32-60`), and chat sessions via `refers_to` (`notebook.py:131-137`).

So on v2, native `PERMISSIONS` would be bypassed on precisely the query shapes this codebase uses most. Adopting native permissions requires first upgrading v2 → 3.1.5+ (two major versions, a data migration), and even then you would carry the residual risks below. That is a large, high-risk prerequisite for a classroom app.

Three further findings, each independently sufficient to reject native permissions as the *primary* control:

1. **The app connects as a root system user** (`repository.py:50-55`, env `SURREAL_USER`/`SURREAL_PASSWORD`, defaulting to `root:root`). SurrealDB docs are explicit that table `PERMISSIONS` "do not restrict system users at the root, namespace, or database level, as those users are governed by roles instead." Native permissions would be **silently inert** until the connection identity is re-plumbed per request.
2. **`repo_query` opens a brand-new connection per call** (`repository.py:70`, `db_connection()` at `repository.py:47-62`). There is no pool. Per-request record auth is therefore *cheap to plumb* but the connection cost is already being paid ~88 times across the query surface — and background workers (`surreal_commands`) have no HTTP request and no end-user identity at all.
3. **The two search functions are DB-side `DEFINE FUNCTION`s that scan whole tables** (`migrations/1.surrealql` `fn::text_search`, `migrations/9.surrealql` `fn::vector_search`). These are the single highest-value leak path in the app — a pupil's search query would return other pupils' source chunks — and they are invisible to any per-call-site `WHERE owner = ...` review, because the scoping would have to happen *inside the SurrealQL function body*.

**Counted query surface (verified):** 85 `repo_query` call sites outside `repository.py`, plus 11 other `repo_*` calls (`repo_create` 1, `repo_insert` 1, `repo_upsert` 2, `repo_update` 3, `repo_delete` 3, `repo_relate` 1) = **96 total**. But this is *not* 96 independent problems — see §1: roughly 60 are already `$id`-parameterised point lookups that become safe for free once the entry-point ownership check is done, and the genuinely dangerous set is **~20 table-scan queries plus 2 DB-side search functions**.

**There is a real chokepoint, but it is not `repo_query`.** It is `ObjectModel` (`domain/base.py`) plus a small set of table-scan queries. `repo_query` takes an opaque SurrealQL string and cannot be scoped generically. The recommended shape is a **default-deny typed accessor layer above `repo_query`, with `repo_query` itself made private/lint-forbidden outside it** — details in §5.

---

## 1. Codebase survey

### 1.1 `repository.py` — thin, stateless, string-in/rows-out

`open_notebook/database/repository.py` is 195 lines and has no notion of identity.

- `get_database_url()` (`:12`), `get_database_password()` (`:24`) read env vars.
- `db_connection()` (`:47-62`) is an `@asynccontextmanager` that constructs a fresh `AsyncSurreal`, calls `db.signin({"username": os.environ["SURREAL_USER"], "password": ...})`, then `db.use(namespace, database)`, yields, and closes.
  - **Verified:** the signin payload has only `username`/`password` — this is a *system user* signin (root, given the compose default `root:root` at `docker-compose.yml:7`). No `namespace`/`database`/`access` keys, i.e. no record access.
- `repo_query(query_str, vars)` (`:65-82`) opens a connection, runs `connection.query(query_str, vars)`, passes results through `parse_record_ids`, closes. **A new TCP/WS connection and signin per query.** The module docstring in `open_notebook/database/CLAUDE.md` confirms this is intentional: "Connection per operation: Each repo_* function opens/closes connection (no pooling)".
- `ensure_record_id(value)` (`:40-44`) coerces `str | RecordID` → `RecordID` via `RecordID.parse`. It is a **type coercion only — it performs no ownership or existence check.** This matters: it is easy to mistake it for a validation boundary. It is not one.
- `parse_record_ids(obj)` (`:29-37`) recursively stringifies `RecordID`s on the way out.

Other writers: `repo_create` (`:85`), `repo_relate` (`:106`), `repo_upsert` (`:123`), `repo_update` (`:134`), `repo_delete` (`:158`), `repo_insert` (`:169`). Of these, `repo_create`/`repo_insert`/`repo_delete` use the SDK's native `connection.insert`/`connection.delete`; the rest build SurrealQL strings and delegate to `repo_query`.

**Only one caller opens a connection outside `repository.py`:** `async_migrate.py:39` (migrations). Verified by grep for `db_connection|AsyncSurreal` across the tree. So `repository.py` *is* a genuine single door to the database — the problem is what passes through it, not that there are side doors.

### 1.2 `ObjectModel` CRUD — a real, narrow chokepoint

`open_notebook/domain/base.py`:

- `get_all(order_by)` (`:39-100`) → builds `SELECT * FROM {table_name}` (`:84`/`:86`) and runs it. **Unscoped table scan. This is the primary leak site for every model.** Note the `order_by` value is regex-validated against `^[a-z_][a-z0-9_]*$` (`:55`) to block injection — so the sanitisation habit exists here already; there is just no tenancy predicate.
- `get(id)` (`:103-128`) → `SELECT * FROM $id` with `{"id": ensure_record_id(id)}` (`:120`). **Parameterised point lookup, no ownership check.** An IDOR: any authenticated pupil who knows or guesses `note:abc` gets the record. Note SurrealDB record IDs are random-ish by default, but IDs leak constantly through API responses and chat citations, so this is not a defence.
- `save()` (`:146-193`) → `repo_create` for new, `repo_update` for existing (`:162`, `:170`). No owner stamped, and **no ownership check before update** — `repo_update` will happily merge into any record ID supplied.
- `delete()` (`:203-215`) → `repo_delete(self.id)` (`:208`). No ownership check.
- `relate()` (`:217-229`) → `repo_relate`. No check that source and target belong to the same tenant — relevant because a crafted `RELATE` could link another pupil's source into your notebook.
- `_get_class_by_table_name` (`:131-144`) resolves subclass from the ID prefix, i.e. `ObjectModel.get()` is polymorphic across tables.

`RecordModel` (`:239-361`) is the singleton-config pattern (`_load_from_db` at `:282`, `update` at `:323`). These are **global app settings, not per-pupil data** — `ContentSettings`, `DefaultPrompts`. They should stay global (teacher/admin-writable) and are *not* part of the tenancy problem.

**Verified model tables** (from `table_name` ClassVars): `notebook`, `source`, `note`, `chat_session`, `source_embedding`, `source_insight`, `transformation`, `credential`, `model`, `episode_profile`, `speaker_profile`, `episode`. Relation tables from migration 1: `reference` (source→notebook), `artifact` (note→notebook), `refers_to` (chat_session→source).

**Inference (not verified by running it):** if `notebook` is made the tenancy root and `Notebook.get_all()` is scoped, then `source`/`note` reached *only* via `->reference->`/`->artifact->` from an owned notebook inherit scoping for free. The exposure is the paths that do **not** go through a notebook: `ObjectModel.get()`, the search functions, and the direct table scans listed below.

### 1.3 The accurate count, and why "~70 sites" overstates the work

Verified counts (grep across `open_notebook/`, `api/`, `commands/`, excluding `repository.py` itself and imports):

| Function | Call sites |
|---|---|
| `repo_query` | 85 |
| `repo_update` | 3 |
| `repo_delete` | 3 |
| `repo_upsert` | 2 |
| `repo_create` | 1 |
| `repo_insert` | 1 |
| `repo_relate` | 1 |
| **Total** | **96** |

`repo_query` by file:

| File | Count |
|---|---|
| `open_notebook/domain/notebook.py` | 17 |
| `commands/embedding_commands.py` | 11 |
| `api/routers/source_chat.py` | 6 |
| `api/routers/notebooks.py` | 6 |
| `api/routers/embedding_rebuild.py` | 6 |
| `open_notebook/domain/base.py` | 4 |
| `api/routers/sources.py` | 4 |
| `open_notebook/podcasts/migration.py` | 3 |
| `open_notebook/domain/credential.py` | 3 |
| `open_notebook/database/async_migrate.py` | 3 |
| `open_notebook/ai/models.py` | 3 |
| `api/routers/models.py` | 3 |
| `api/routers/chat.py` | 3 |
| `api/credentials_service.py` | 3 |
| `open_notebook/podcasts/models.py` | 2 |
| `open_notebook/ai/model_discovery.py` | 2 |
| `commands/podcast_commands.py` | 2 |
| `api/routers/credentials.py` | 2 |
| `open_notebook/domain/provider_config.py` | 1 |
| `api/routers/config.py` | 1 |

**Triage — this is the load-bearing part of the survey.** Not all 96 are tenancy-relevant:

- **Not tenant data at all (~25 sites).** `async_migrate.py` (3), `credential.py` (3), `credentials_service.py` (3), `credentials.py` (2), `ai/models.py` (3), `model_discovery.py` (2), `models.py` router (3), `provider_config.py` (1), `config.py` (1), `podcasts/migration.py` (3). These are **admin/global config** — AI provider credentials, model registry, migrations. In a classroom deployment these should be *teacher/admin-only*, enforced by role at the API layer, not row-scoped. **Decision needed:** are `transformation`, `episode_profile`, `speaker_profile` global-shared (teacher authors, pupils use) or per-pupil? Recommend global-shared, which removes them from the row-scoping problem.
- **Already-scoped-by-parameter point lookups (~50 sites).** e.g. `notebook.py:310-315` (`select source.* from $id fetch source`), `:444-449`, `:460-465`, `:604-611`, `notebooks.py:158`, `:206`, `:254-260`, `:294-300`, `chat.py:221/282/347`, `sources.py:650/852`, and most of `embedding_commands.py` (`:226`, `:323`, `:415`, `:624`, `:760`). These filter by a specific `$id` the caller already supplied. **They are safe *if and only if* that ID was ownership-checked at the entry point.** They do not each need a `WHERE owner =` clause; they need one authorisation gate upstream. This is the single biggest reason the "~70 places to patch" framing is pessimistic.
- **Genuinely dangerous unscoped table scans (~20 sites).** These return rows the caller never named, and each is a real leak:
  - `base.py:84`/`:86` — `SELECT * FROM {table}` (affects **every** model via `get_all()`)
  - `base.py:120` — `SELECT * FROM $id` (IDOR on any table)
  - `notebooks.py:61` — list-all-notebooks (note `:64-65` filters `archived` **in Python, after fetching everything** — the pattern to avoid)
  - `credential.py:176` — `SELECT * FROM {cls.table_name}{order_clause}`
  - `embedding_commands.py:842-847`, `:858-859`, `:868-869`, `:873-874` — collect **all** sources / **all** notes for embedding rebuild
  - `embedding_rebuild.py` (6 sites) — same family
  - `notebook.py:702-707` and `:752-761` — `fn::text_search` / `fn::vector_search`
- **DB-side functions (2, highest severity).** `fn::text_search` (`migrations/1.surrealql`) and `fn::vector_search` (`migrations/9.surrealql`) run `SELECT ... FROM source_embedding` / `FROM source_insight` / `FROM note` with **no owner predicate**. `api/routers/search.py:29-42` passes only `keyword`, `limit`, `search_sources`, `search_notes`, `minimum_score` — there is nowhere for a tenant to be threaded today. **Fixing these requires editing SurrealQL in a new migration and adding an `$owner` parameter to both function signatures.** No amount of Python-side review catches this one.

### 1.4 Query construction style — an obstacle to static analysis

**Verified:** 75 of the `repo_query` call sites pass the query as a multi-line literal starting on the following line, and at least three use **f-string interpolation** into the query text (`credential.py:176`, `notebook.py:33`, `notebook.py:55`). The interpolated values are internal (`cls.table_name`, a projection fragment), not user input, so these are not injection bugs today — but f-strings mean a naive "does this query string contain `owner`?" linter cannot reason about the final SQL. This constrains the static-analysis option in §5.

---

## 2. SurrealDB native scoping

Version context: project runs **SurrealDB v2** (`docker-compose.yml:4` `image: surrealdb/surrealdb:v2`; `Dockerfile.single:26`). Python SDK `surrealdb==1.0.8` (`uv.lock:3356-3357`). Latest upstream stable is 3.2.1 (July 2026); 3.0 went GA 2026-02-17.

### 2.1 The mechanism exists and is expressive

`DEFINE TABLE ... PERMISSIONS` supports `NONE`, `FULL`, or per-operation `FOR select | create | update | delete WHERE <expr>`, where the expression is SurrealQL evaluated against the auth context, conventionally via `$auth`:

```surql
DEFINE TABLE note PERMISSIONS
    FOR select WHERE owner = $auth.id
    FOR create, update WHERE owner = $auth.id
    FOR delete WHERE owner = $auth.id OR $auth.role = 'teacher';
```

Key semantics, verified from docs:

- **Tables default to `PERMISSIONS NONE`**; fields default to `PERMISSIONS FULL` (inheriting the table rule). Default-deny at table level is genuinely good — a *new* table added later is closed until someone opens it. This is the strongest argument in favour of the native approach.
- In v2 the auth mechanism is `DEFINE ACCESS ... ON DATABASE TYPE RECORD` with `SIGNUP` / `SIGNIN` / `WITH JWT` / `AUTHENTICATE` / `DURATION FOR TOKEN ... FOR SESSION ...`. It replaced 1.x's `DEFINE SCOPE` + `DEFINE TOKEN` (removed entirely in 3.0). `WITH JWT` allows trusting an external issuer, with claims exposed as `$token`.
- `$auth` is populated from the record named by the token's `id` claim, and exposes that record's fields (`$auth.id`, `$auth.role`, …).
- Record access **requires finite token expiry** — `DURATION FOR TOKEN NONE` is rejected.

### 2.2 The blocking limitation: graph traversal bypassed permissions before 3.1.0

**[GHSA-vjjx-rfw4-rmfc]** — "Graph traversal bypasses table SELECT permissions", CVSS 6.5 Moderate, **affects all versions < 3.1.0, fixed in 3.1.0**:

> Authenticated users could read records on any table reachable through a graph edge or `REFERENCES TO` back-reference, regardless of that table's `PERMISSIONS FOR select` clause.

Root cause: `GraphEdgeScan` and `ReferenceScan` fetched records from storage without running `Document::pluck_select`, the permission filter. `SELECT * FROM source->edge->target` returned full documents from restricted tables.

**This is not a theoretical concern for this codebase — it is a direct hit.** The core reads are graph traversals:

- `notebook.py:32-38` — `select in as source from reference where out=$id fetch source`
- `notebook.py:54-60` — `select in as note from artifact where out=$id fetch note`
- `notebook.py:131-137` — `<- chat_session as chat_session from refers_to`
- `notebooks.py:155`, `:203` — `count(<-artifact.in)`, `count(<-reference.in)`
- `notebook.py:176-182`, `:241-247` — `count(->reference[WHERE out != $notebook_id].out)`

On v2, `PERMISSIONS FOR select WHERE owner = $auth.id` on `source` and `note` would be **enforced on direct scans and silently bypassed on exactly these traversals**. That failure mode — protection that works in your manual spot-check (`SELECT * FROM note`) and fails on the path the app actually uses — is worse than no protection, because it manufactures false confidence.

A follow-up advisory **[GHSA-hv6h-hc26-q48p]** (Moderate, affects **3.1.0–3.1.4**, fixed **3.1.5**) shows the same class of bug recurring at *field* level: `resolve_record_batch` applied table-level but not field-level SELECT permissions on graph-edge (`->`), back-reference (`<~`), and target-vertex projections. **Inference:** the traversal permission path has been a repeated source of bypasses across two consecutive minor releases. For a pupil-data application, that is a meaningful reliability signal about depending on it as the sole control.

### 2.3 Other limitations

- **Custom functions.** `DEFINE FUNCTION` accepts its own `PERMISSIONS NONE | FULL | WHERE <cond>` clause — but that gates *who may call the function*, not what the body may read. **The docs do not state whether table permissions are enforced inside a function body** (I checked the `DEFINE FUNCTION` page specifically and it is silent; there is an open upstream issue, surrealdb#4603, requesting "execution level specifiers for functions", which implies the semantics are not currently controllable). **This is unverified and would need empirical testing.** It directly determines whether `fn::text_search`/`fn::vector_search` would be scoped automatically. Given the uncertainty, the safe assumption is that **you must parameterise the functions with `$owner` regardless of which strategy you pick.** This is the one piece of work that is unavoidable either way.
- **Performance.** Docs and secondary sources state permissions are evaluated dynamically per query and per result, and that complex permission logic degrades performance. **No published benchmark numbers were found.** The concrete concern for this app: `fn::vector_search` (`migrations/9.surrealql`) already does a full scan of `source_embedding` computing `vector::similarity::cosine` per row, with no vector index. Adding a per-row permission predicate on top of an already-unindexed full scan compounds. **An owner predicate that can use an index (`DEFINE INDEX ON source_embedding COLUMNS owner`) will almost certainly outperform a permission expression evaluated per row after the scan** — inference, but a well-founded one given the query shape.
- **Blast radius of `PERMISSIONS NONE` default.** Good for security, operationally sharp: the moment you add record auth, every table without an explicit rule — including the 12 relation/config tables — goes dark. Migration 1 defines `reference`, `artifact`, `refers_to`, `podcast_config`; migrations 11–15 add `credential` etc. All would need explicit rules in one atomic migration or the app breaks wholesale.

---

## 3. The auth-model mismatch

**This is the decisive practical objection, and yes — it means re-plumbing the connection identity per request.**

Verified facts:

1. The connection signs in as a **system user**: `repository.py:50-55` passes only `{"username", "password"}` from `SURREAL_USER`/`SURREAL_PASSWORD`. Compose defaults these to `root:root` (`docker-compose.yml:7`, `:31-32`).
2. SurrealDB docs, `DEFINE TABLE` page, unambiguous: table permissions "do not restrict system users at the root, namespace, or database level, as those users are governed by roles instead." The authorization guide repeats it: "System users are not restricted by table or field `PERMISSIONS`, using roles instead."

**Therefore: if you write `DEFINE TABLE note PERMISSIONS FOR select WHERE owner = $auth.id` today and change nothing else, it has zero effect.** Every query still returns every row. This is the silent-no-op trap — the migration applies cleanly, tests pass, and nothing is enforced.

### What re-plumbing actually costs here

The mechanics are available: the Python SDK supports `signin({"namespace":..., "database":..., "access":..., ...})` for record access, plus `authenticate(token)` and `invalidate()`.

The surprising good news: **because `repo_query` already opens a fresh connection per call (`repository.py:70`), there is no pool to invalidate.** The classic "connection-pooled async app can't do per-request DB identity" objection — where you must either pin a connection per request (destroying pool efficiency) or `SET ROLE`/reset on every checkout — **does not bite here, because the pool does not exist.** You would thread a token into `db_connection()` and call `authenticate(token)` instead of the root `signin`. Roughly:

```python
# sketch only — not implemented
@asynccontextmanager
async def db_connection(token: str | None = None):
    db = AsyncSurreal(get_database_url())
    if token:
        await db.authenticate(token)     # record user → $auth populated
    else:
        await db.signin({"username": ..., "password": ...})  # system user
    await db.use(ns, db_name)
```

But the cost lands elsewhere, and it is substantial:

- **Threading the token through 96 call sites.** `repo_query(q, vars)` has no identity parameter. You would add one and update every caller — or use a `ContextVar` set by middleware. The `ContextVar` route is the only tractable one, and it has a known failure mode: **anything running outside the request context silently falls back to the root/no-token path**, i.e. fails *open*. That is the exact bug class you are trying to eliminate.
- **Background workers have no user.** `surreal_commands` jobs (`submit_command` at `notebook.py:502`, `:553`, `:651`; `api/command_service.py:28`; `api/podcast_service.py:96`) run in a separate worker process with no HTTP request. `commands/embedding_commands.py` has 11 `repo_query` calls that must write embeddings across all tenants. Under record auth these workers must run as a **system user, bypassing permissions entirely** — so the embedding/podcast paths get no protection from the native mechanism, and `embedding_rebuild.py`'s 6 collect-everything queries stay unscoped by construction.
- **The `$auth` record must live in SurrealDB.** Record access requires a `user`/`pupil` table in the same database, with `SIGNIN`/`SIGNUP` logic in SurrealQL, replacing `PasswordAuthMiddleware` (`api/auth.py:12-75`). Alternatively `WITH JWT` against your own issuer — better fit, since you need teacher/pupil/class/course modelling anyway that is awkward to express in SurrealQL signin expressions.
- **Per-connection overhead grows.** Today each `repo_query` costs connect + system signin. Under record auth it is connect + `authenticate(token)` + token verification. A single API request already fans out to many `repo_query` calls (`notebooks.py` list endpoint, then per-notebook counts). **Inference:** this is the more likely performance problem in practice — more than the permission-expression evaluation cost — because it multiplies a per-connection handshake that is already being paid too often.

**Honest assessment:** the re-plumbing is *feasible* — more feasible than in a typical pooled app, thanks to the no-pool design. But it buys protection that (a) is bypassed on this app's dominant query shape until you upgrade to 3.1.5+, (b) does not cover background workers at all, (c) does not cover the search functions without separate work, and (d) requires replacing the auth system as a prerequisite rather than as a follow-on. The cost is front-loaded and the coverage is partial.

---

## 4. Migration strategy

Repo migrations live in `open_notebook/database/migrations/`, numbered `N.surrealql` / `N_down.surrealql`.

**Correction to the ticket premise:** the ticket says migrations are at 9. **Verified: they are at 15.** Files `1`–`15` exist with matching `_down` files, and `AsyncMigrationManager.__init__` (`async_migrate.py:~100-160`) hard-codes the list of 15 up + 15 down migrations. `open_notebook/database/CLAUDE.md` documents 15. **New migrations are therefore 16, 17, … and each requires a code change to `AsyncMigrationManager` — there is no auto-discovery** (an explicitly documented gotcha). Migrations run automatically on API startup via the FastAPI lifespan handler.

### 4.1 Suggested sequence

**Migration 16 — identity tables** (additive, no behaviour change):
`school_user` (id, email, role: pupil|teacher|admin, display_name), `class`, `course`, plus membership relations. Backfill a single `school_user:legacy_owner` record representing the pre-existing single-tenant deployment.

**Migration 17 — ownership columns, nullable, plus indexes:**

```surql
DEFINE FIELD IF NOT EXISTS owner ON TABLE notebook TYPE option<record<school_user>>;
DEFINE FIELD IF NOT EXISTS owner ON TABLE source   TYPE option<record<school_user>>;
DEFINE FIELD IF NOT EXISTS owner ON TABLE note     TYPE option<record<school_user>>;
DEFINE FIELD IF NOT EXISTS owner ON TABLE chat_session TYPE option<record<school_user>>;
DEFINE FIELD IF NOT EXISTS owner ON TABLE source_embedding TYPE option<record<school_user>>;
DEFINE FIELD IF NOT EXISTS owner ON TABLE source_insight   TYPE option<record<school_user>>;

DEFINE INDEX IF NOT EXISTS idx_notebook_owner ON TABLE notebook COLUMNS owner;
DEFINE INDEX IF NOT EXISTS idx_source_owner   ON TABLE source   COLUMNS owner;
DEFINE INDEX IF NOT EXISTS idx_note_owner     ON TABLE note     COLUMNS owner;
DEFINE INDEX IF NOT EXISTS idx_sembed_owner   ON TABLE source_embedding COLUMNS owner;
DEFINE INDEX IF NOT EXISTS idx_sinsight_owner ON TABLE source_insight   COLUMNS owner;
```

Two notes. **`option<...>` is deliberate for this step only** — it lets the migration land without breaking writes. **Denormalising `owner` onto `source_embedding` and `source_insight` is deliberate and important**: it lets the search functions filter with an indexed predicate instead of joining back to `source` per row, which is the difference between a scoped search that performs and one that doesn't.

Note migrations 1 and 9 define `source`/`note` as `SCHEMAFULL`, so **fields must be declared** — you cannot just start writing `owner` from Python.

**Migration 18 — backfill:**

```surql
UPDATE notebook SET owner = school_user:legacy_owner WHERE owner = NONE;
UPDATE source   SET owner = school_user:legacy_owner WHERE owner = NONE;
UPDATE note     SET owner = school_user:legacy_owner WHERE owner = NONE;
-- derive children from their parent source
UPDATE source_embedding SET owner = source.owner WHERE owner = NONE;
UPDATE source_insight   SET owner = source.owner WHERE owner = NONE;
```

**On pre-existing ownerless data — this is the question that decides whether the retrofit is safe.** Three options, and only one is acceptable:

| Option | Behaviour | Verdict |
|---|---|---|
| Treat `owner = NONE` as **public** | Old rows visible to all pupils | **Reject.** Fails open. One missed backfill = mass leak. |
| Treat `owner = NONE` as **invisible** | Old rows unreachable | Safe but silently destroys the existing corpus |
| **Backfill to `legacy_owner`, then make the field mandatory** | Old rows owned by a teacher/admin account, re-assignable through the UI | **Recommended** |

**Migration 19 — tighten, after backfill is verified:** change `option<record<school_user>>` → `record<school_user>` so the database itself rejects any future ownerless write. This is the step that converts "we remembered to set owner" into "we cannot fail to set owner", and it is the highest-value single line in the whole plan. Gate it on a verification query returning zero: `SELECT count() FROM note WHERE owner = NONE GROUP ALL`.

**Migration 20 — re-define the search functions with an owner parameter.** Mandatory under either strategy (see §2.3):

```surql
DEFINE FUNCTION OVERWRITE fn::vector_search(
    $query: array<float>, $match_count: int, $sources: bool,
    $show_notes: bool, $min_similarity: float, $owner: record<school_user>
) { ... WHERE owner = $owner AND embedding != none AND ... };
```

Then update `notebook.py:702-707` / `:752-761` and their `api/routers/search.py:29-42` callers to pass it. Follow the existing `REMOVE FUNCTION IF EXISTS` / re-`DEFINE` pattern from migration 9. **Make `$owner` a required parameter with no default** — an optional one would fail open.

Rollback: write the `_down` files (the existing convention) and remember `AsyncMigrationManager` needs both lists extended.

---

## 5. Avoiding missed-scope leaks — recommendation for this codebase

The ordering principle: **prefer controls that fail closed and that make the unsafe thing hard to express, over controls that require reviewers to notice an absence.** "Did someone forget a `WHERE`?" is exactly the question humans and LLM code review are worst at.

### 5.1 Primary — a default-deny typed accessor layer, with `repo_query` made unreachable

`repo_query` cannot be scoped generically: it takes opaque SurrealQL. Wrapping it with string manipulation to inject `WHERE` clauses would be fragile and defeated by the f-string call sites (§1.4). The tractable move is to **stop calling it directly** and route tenant data through a small typed layer that cannot express an unscoped read:

1. Rename `repo_query` → `_repo_query_unscoped` and add a scoped API that **requires** an owner argument (no default, no `Optional`):

```python
async def repo_query_scoped(query: str, owner: RecordID, vars: dict) -> list[dict]:
    if owner is None:
        raise ValueError("owner is required")
    ...
```

2. Add `ScopedObjectModel(ObjectModel)` overriding `get_all` / `get` / `save` / `delete` to always take an `owner` and always emit `WHERE owner = $owner`. Move `Notebook`, `Source`, `Note`, `ChatSession`, `SourceInsight`, `SourceEmbedding` onto it. `base.py:84`, `:86`, `:120` are the three lines that carry most of the risk.
3. **Stamp `owner` on write inside `_prepare_save_data()`** (`base.py:195-201`) so ownership is set by construction, not remembered per call site.
4. Leave admin/config models (`Credential`, `Model`, `Transformation`, profiles, `RecordModel` singletons) on plain `ObjectModel`, gated by an API-layer **role** check. Making them tenant-scoped would be wrong.

The `ObjectModel` chokepoint is real: fixing `get_all`/`get`/`save`/`delete` covers every model at once. It is the ~20 table-scan sites and the 2 DB functions that need individual attention — **not 96 sites, and not 70.**

### 5.2 Enforcement — make the bypass fail CI, not review

A grep-based lint is the cheapest high-value control here and works despite the f-strings (it checks *who calls*, not what the SQL says):

- Fail CI if `_repo_query_unscoped` is imported anywhere outside an allowlist (`repository.py`, `async_migrate.py`, `commands/`, admin services).
- Fail CI on any new `.surrealql` `DEFINE TABLE` lacking a corresponding `owner` field declaration.

Ruff supports custom-banned imports (`flake8-tidy-imports` `banned-api`) and the repo already runs ruff + pre-commit (`pyproject.toml` dev deps, `.pre-commit-config`). **Inference:** this is a few lines of config, not a new tool. Full static taint analysis of SurrealQL strings is not worth building — the f-string construction makes it unreliable, and the allowlist gets ~90% of the value.

### 5.3 Tests — the only control that catches semantic leaks

The existing suite (`tests/`, 16 files) has no cross-tenant test. Add `tests/test_tenant_isolation.py` with a **two-pupil fixture** (pupil A and pupil B each with a notebook, source, note, chat session, insight) and assert, for **every** list endpoint and **every** `get_all()`, that A never sees B's rows. Then:

- **A parametrised sweep over routers is worth more than hand-written cases.** Enumerate the registered routes from `app.routes` (`api/main.py:290-312`) and assert every GET returning a collection is empty-or-A-only when authenticated as A. New endpoints are then covered by default — a new leak has to actively defeat the test rather than merely not be thought about.
- **Explicitly test the leak paths this survey identified**, because they are the ones generic tests miss: `POST /api/search` as pupil A must not return B's source chunks (both `type=text` and `type=vector` — they hit different DB functions); `GET /api/notebooks/{B's id}` as A must 404 not 403 (403 confirms existence); `ObjectModel.get("note:<B's id>")` as A must raise.
- **Add an ownerless-row test:** insert a row with `owner = NONE` and assert *nobody* sees it. This pins the fail-closed decision from §4.1 so a later refactor cannot quietly flip it to fail-open.

### 5.4 Defence in depth — keep native permissions as a second layer, later

Once (and only once) the app is on **SurrealDB ≥ 3.1.5**, add `DEFINE TABLE ... PERMISSIONS` as a *backstop* beneath the application layer. Belt-and-braces is right for pupil data. But it is a phase-2 item: it requires the v2→v3 upgrade plus the record-auth re-plumbing from §3, and it must not be the thing you are relying on in the meantime.

---

## Recommendation on the central trade-off

**Enforce tenancy in the application (repository layer). Treat database-native permissions as a later second layer, not the primary control.**

### Why not native permissions (database)

Honest costs, specific to this codebase:

- **Blocked by version.** Graph traversal bypassed SELECT permissions in everything before 3.1.0 (GHSA-vjjx-rfw4-rmfc). This project is on v2, and traversals *are* its read path (`notebook.py:32-60`, `:131-137`). Requires a v2→3.1.5+ upgrade first — two majors and a data migration — before you get anything.
- **Silently inert until auth is re-plumbed.** Root/system users bypass `PERMISSIONS` by design. Adding permissions today changes nothing while looking like it changed everything.
- **Requires replacing `PasswordAuthMiddleware` first**, with either SurrealQL-expressed signin or a JWT issuer, as a *prerequisite* rather than a follow-on.
- **Doesn't cover background workers.** `surreal_commands` has no end-user identity and must run as a system user, leaving `commands/embedding_commands.py` (11 queries) and `embedding_rebuild.py` (6) unprotected regardless.
- **Doesn't cover the search functions** without the same `$owner` migration you'd write anyway, and whether table permissions even apply inside function bodies is **undocumented and unverified**.
- Genuine upside, worth stating: `PERMISSIONS NONE` default-deny means a *future* table is closed until opened. The application-layer approach must reproduce that property deliberately (§5.2).

### Why the application layer

- **Works on v2 today**, no upgrade, no auth replacement on the critical path.
- **Covers all execution contexts uniformly** — HTTP requests and background workers alike.
- **The chokepoint is real.** `ObjectModel.get_all`/`get`/`save`/`delete` (`base.py:39`, `:103`, `:146`, `:203`) covers every model in one change; `repository.py` is the only door to the DB (only `async_migrate.py:39` bypasses it).
- **`owner` predicates can use an index**, unlike per-row permission expressions — material for `fn::vector_search`, which already full-scans `source_embedding` with no vector index.
- Honest costs: it is **opt-in, so it fails open by default** — the exact weakness native permissions don't have. This must be bought back with the three mechanisms in §5: the banned-import lint (5.2), the `record<school_user>` NOT-NULL tightening in migration 19 (4.1), and the route-enumerating isolation sweep (5.3). **Without all three, this recommendation is materially weaker than the native option.** It also means ~20 table-scan sites plus 2 SurrealQL functions get edited by hand, and every future `repo_query` author must go through the scoped API — a standing discipline cost that the lint, not code review, has to carry.

### Ordered plan

1. Migration 16–19: identity tables, `owner` columns + indexes, backfill to `legacy_owner`, then tighten to non-optional.
2. Migration 20: re-define `fn::text_search` / `fn::vector_search` with a required `$owner`. **Mandatory under either strategy.**
3. `ScopedObjectModel` + owner-stamping in `_prepare_save_data()`; migrate the six tenant models.
4. Hand-fix the ~20 table-scan sites; decide global-vs-per-pupil for `transformation` / profiles.
5. Rename `repo_query` → `_repo_query_unscoped`; add the ruff banned-import allowlist to CI.
6. `tests/test_tenant_isolation.py`: two-pupil fixture, route-enumerating sweep, explicit search/IDOR/ownerless cases.
7. *Later, optional:* upgrade to SurrealDB ≥ 3.1.5, add `DEFINE TABLE ... PERMISSIONS` as a backstop.

**Verified vs. inferred.** Verified: all file:line references, the 96-call-site count and per-file breakdown, migration count of 15, root-user signin in `db_connection`, SurrealDB v2 pin, SDK version 1.0.8, the two GHSA advisories and their affected/fixed versions, the docs statements on system-user bypass and `PERMISSIONS NONE` defaults, and the unscoped bodies of both search functions. Inferred and flagged as such: relative performance of indexed `owner` predicates vs. permission expressions; the claim that notebook-rooted scoping transitively covers sources/notes; the read of surrealdb#4603 as implying function-body permission semantics are uncontrollable; and the per-connection `authenticate()` overhead argument. Explicitly unverified and needing an empirical test before relying on it: **whether table `PERMISSIONS` are enforced inside `DEFINE FUNCTION` bodies.**

---

## Sources

All accessed 2026-07-29.

**SurrealDB documentation**
- DEFINE TABLE statement — https://surrealdb.com/docs/surrealql/statements/define/table
- DEFINE ACCESS ... TYPE RECORD — https://surrealdb.com/docs/surrealql/statements/define/access/record
- DEFINE ACCESS statement — https://surrealdb.com/docs/surrealql/statements/define/access
- DEFINE FUNCTION statement — https://surrealdb.com/docs/surrealql/statements/define/function
- Authentication (system users vs. record users) — https://surrealdb.com/docs/surrealdb/security/authentication
- Permissions & row-level security — https://surrealdb.com/docs/learn/security/authorization/permissions-and-row-level-security
- Security best practices — https://surrealdb.com/docs/surrealdb/reference-guide/security-best-practices
- Upgrading 1.x to 2.x — https://surrealdb.com/docs/surrealdb/installation/upgrading/migrating-data-to-2x
- Upgrading 2.x to 3.x — https://surrealdb.com/docs/surrealdb/installation/upgrading/migrating-data-to-3x
- Release notes & changelog — https://surrealdb.com/releases
- Python SDK — https://github.com/surrealdb/surrealdb.py

**Security advisories**
- GHSA-vjjx-rfw4-rmfc — Graph traversal bypasses table SELECT permissions (<3.1.0, fixed 3.1.0), CVSS 6.5 — https://github.com/advisories/GHSA-vjjx-rfw4-rmfc
- GHSA-hv6h-hc26-q48p — Field-level SELECT permissions bypassed via graph/reference traversals (3.1.0–3.1.4, fixed 3.1.5) — https://github.com/advisories/GHSA-hv6h-hc26-q48p
- surrealdb#4603 — Feature: execution level specifiers for functions — https://github.com/surrealdb/surrealdb/issues/4603

**Secondary (corroborating, lower trust)**
- Optimizing Query Performance in SurrealDB — https://medium.com/@firmanbrilian/optimizing-query-performance-in-surrealdb-indexing-permissions-and-query-design-best-practices-394195672b55
- SurrealDB 3.0 GA announcement (2026-02-17) — https://tech.eu/2026/02/17/surrealdb-secures-23m-and-launches-surrealdb-3-0-to-address-ai-agent-memory-challenges/

**Codebase (this repo, `main` @ `cac4e01`)**
- `open_notebook/database/repository.py` — `db_connection` :47-62, `repo_query` :65-82, `ensure_record_id` :40-44
- `open_notebook/domain/base.py` — `get_all` :39-100, `get` :103-128, `save` :146-193, `delete` :203-215, `_prepare_save_data` :195-201
- `open_notebook/domain/notebook.py` — traversals :32-60, :131-137; search :702-707, :752-761
- `open_notebook/database/migrations/1.surrealql` — schema + `fn::text_search`
- `open_notebook/database/migrations/9.surrealql` — `fn::vector_search`
- `open_notebook/database/async_migrate.py` — `AsyncMigrationManager` (15 migrations), `db_connection` use :39
- `api/auth.py` — `PasswordAuthMiddleware` :12-75
- `api/routers/search.py` :29-42, `api/routers/notebooks.py` :61, `commands/embedding_commands.py` :842-874
- `docker-compose.yml` :4, :7 — `surrealdb/surrealdb:v2`, `root:root` default
- `uv.lock` :3356-3357 — `surrealdb==1.0.8`
