# Data protection obligations for hosting children's data

Research for [issue #8](https://github.com/danieldannhofer-gif/open-notebook-school/issues/8). All sources accessed **2026-07-29**.

> **Scope note.** This is engineering research against primary sources, not legal advice. Several conclusions below turn on facts only the project owner can supply (jurisdiction, who the controller is, which provider is used). Those are flagged as open questions rather than resolved.

---

## Answer

The decision-relevant conclusions, in order of how much they change the build:

- **Google's Gemini API is off the table as currently drafted.** The Gemini API Additional Terms of Service say you "will not use the Services as part of a website, application, or other service ... that is directed towards or is likely to be accessed by individuals under the age of 18." That is a flat prohibition with no educational carve-out, and it is not tier-dependent. A classroom tool for 12-year-olds is squarely the prohibited case. Google Cloud **Vertex AI** and **Gemini for Education** are governed by different agreements and may be viable — but that is an unverified alternative, not a confirmed one. See [Q3](#3-model-provider-terms-regarding-minors).
- **OpenAI is usable but imposes a hard technical precondition.** OpenAI's under-18 API guidance states you "should not use OpenAI services to process any personal data of children under 13 or the applicable age of digital consent without first implementing zero data retention in our API." Under both the Austrian (14) and German (16) digital-consent ages, **12-year-olds are under the applicable age**, so **Zero Data Retention is required** — and ZDR is not a config flag, it requires prior approval from OpenAI sales. This is a procurement lead-time item, not a code change. See [Q3](#3-model-provider-terms-regarding-minors).
- **Anthropic is the most permissive of the three** — no age floor in the Commercial Terms, and the Usage Policy expressly contemplates "organizations providing minors with the ability to directly interact with products that incorporate our API(s)" subject to additional guidelines (age verification, content moderation, monitoring, AI disclosure). No zero-retention precondition is stated. Default API retention is 30 days, no training on customer content. See [Q3](#3-model-provider-terms-regarding-minors).
- **Yes, display name + join code is personal data.** Not a close call. A pupil is an identified or identifiable natural person the moment their work is attributable to them within the class, and pseudonymisation **does not** remove data from GDPR scope — it is a security measure that reduces risk, not a scope exemption. Full GDPR obligations apply. See [Q1](#1-is-a-display-name--join-code-personal-data).
- **Consent is almost certainly the wrong legal basis, and Article 8 probably never engages.** Where a school is the controller acting under its statutory educational function, the basis is **public task** (Art 6(1)(e)), not consent. The EDPB states Article 8 applies **only** where processing is based on consent *and* the service is offered directly to a child — a school-deployed tool is neither. The Art 8 age threshold is therefore likely a red herring for the core flow. See [Q2](#2-legal-basis-and-consent).
- **The ticket's premise about Germany is wrong.** Germany did **not** use the Art 8 opening clause; it remains at **16**. Austria set it at **14** (§4(4) DSG). The ticket's assumption that both are 14 is incorrect for Germany. See [Q2](#2-legal-basis-and-consent).
- **The ICO Children's Code probably does not bind this project** — contrary to the ticket's framing. The Code applies to information society services; the ICO states it does not apply to edtech providers that are not direct-to-consumer and act solely on school instruction. But this depends entirely on the deployment model, and **if pupils sign up themselves rather than via a school, the Code applies in full**. See [Q4](#4-what-a-school-would-require).
- **A DPIA is effectively mandatory** on every jurisdictional path — children (vulnerable data subjects) plus AI (innovative technology) meets the EDPB two-criteria threshold, and the ICO says services in scope of the children's code "inevitably" involve high-risk processing. See [Q4](#4-what-a-school-would-require).

**The single biggest open question is jurisdiction** — see [Jurisdiction](#jurisdiction-the-open-question) immediately below, which lists exactly which findings flip.

---

## Jurisdiction: the open question

The ticket names UK GDPR / DPA 2018 / ICO. The user's locale signals suggest Austria or Germany. **These are mutually exclusive regimes for determining who regulates you, and the answer has not been confirmed.** This must be resolved before schema and auth are frozen.

What is the same regardless of the answer:

- Display name + join code is personal data (identical Art 4(1) text in UK GDPR and EU GDPR).
- Pseudonymisation does not exempt you.
- A DPIA is required.
- An Art 28 data processing agreement is required with every processor.
- Data subject rights (access, erasure, rectification) apply.
- Provider terms bind you contractually regardless of jurisdiction.

What changes:

| Question | UK | Austria | Germany |
|---|---|---|---|
| Regulator | ICO | Datenschutzbehörde (DSB) | State DPA (Landesbeauftragte) — varies by Bundesland |
| Art 8 digital-consent age | 13 (DPA 2018 s9) | **14** (§4(4) DSG) | **16** (no opening-clause law) |
| ICO Children's Code | Applies **only if** direct-to-consumer (see Q4) | Does not apply (UK instrument) | Does not apply (UK instrument) |
| DPIA "blacklist" | ICO high-risk examples | DSFA-V (BGBl II 278/2018) | DSK Muss-Liste |
| School's legal basis | Public task, Art 6(1)(e) | Public task via Bildungsdokumentationsgesetz / Schulgesetze | Public task via Landesschulgesetze + Landesdatenschutzgesetze |

> **Open question — unresolved.** Which jurisdiction governs. If Germany, there is a further unresolved sub-question: **which Bundesland**, because school data protection is state-level competence and each state has its own school law, its own DPA, and in several cases its own list of approved/permitted digital tools for schools. I did not research individual Länder rules because the state is unknown.

> **Open question — unresolved.** Whether the ICO Children's Code is in scope at all is contingent on deployment model, not just jurisdiction. Even in the UK it may not bind you (see Q4).

---

## 1. Is a display name + join code personal data?

**Yes. Confirmed. Pseudonymisation does not change the obligations.**

### The definition is met

UK GDPR Art 4(1) defines personal data as "any information relating to an identified or identifiable natural person ('data subject')" ([legislation.gov.uk, Art 4](https://www.legislation.gov.uk/eur/2016/679/article/4)). The EU GDPR text is identical.

The pupil is *identifiable* on the design as described, for several independent reasons, any one of which is sufficient:

1. **The join code scopes them to a known, small, enumerable group.** A class of ~12 pupils is a closed set. The teacher knows who is in it.
2. **The teacher can attribute work to a pupil.** That is the point of the tool — a teacher seeing "Danny H." or even "SpaceCat42" alongside submitted work can identify the individual. Identifiability is assessed by reference to means "reasonably likely to be used" by the controller *or another person*, not by the general public.
3. **Display names chosen by 12-year-olds frequently contain real names.** This is an empirical near-certainty, not a hypothetical.
4. **The content itself is personal data.** Even with a perfectly opaque handle, everything the pupil types — their questions, their answers, their misunderstandings, their writing — is information *relating to* them. Free-text pupil work is personal data about that pupil's learning and ability, independent of the identifier attached to it.

Point 4 is the one most often missed and it is the most important for this project: **you could remove the display name entirely and the data would still be personal data**, because the substance of what is stored is a record of an identifiable child's academic performance.

### Pseudonymisation changes risk, not scope

The ICO is unambiguous: pseudonymised data "is personal data in the hands of someone who holds the additional information, and it does not change the status of the data as personal data when you process it in this way" ([ICO, Pseudonymisation](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/pseudonymisation/)).

Art 4(5) defines pseudonymisation as processing such that data can no longer be attributed to a subject "without the use of additional information, provided that such additional information is kept separately" ([Art 4(5)](https://www.legislation.gov.uk/eur/2016/679/article/4)). The class roster *is* that additional information, and you hold it.

**Practical consequence for schema decisions:** pseudonymisation is still worth doing — it is an Art 32 security measure, it is explicitly credited as a risk-reducer, and it limits what leaks in a breach. But do not architect on the assumption that "no email, no real name" puts you outside GDPR. It does not. Design for full compliance and treat pseudonymisation as defence-in-depth.

> **Note on anonymisation.** Genuinely anonymous data *is* out of scope — but the bar is that re-identification must be reasonably impossible for anyone, including you. A tool where a teacher must see per-pupil progress cannot be anonymous by construction. Do not pursue this as an escape route.

---

## 2. Legal basis and consent

### Who consents? Probably nobody — consent is the wrong basis

This is the most commonly misunderstood point in edtech and it materially simplifies the design.

**For a publicly-funded school, the ICO expects public task, not consent:** "In most cases, the ICO would expect publicly-funded schools to be looking at public task as their lawful basis for processing pupils' personal information" ([ICO, Children's code and edtech](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/the-children-s-code-and-education-technologies-edtech/)). Public task is Art 6(1)(e): processing necessary for the performance of a task carried out in the public interest or in the exercise of official authority. The underlying task must have a basis in law, but the ICO confirms this "does not have to be an explicit statutory provision, as long as the application of the law is clear and foreseeable" ([ICO, Public task](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/public-task/)).

**Consent from pupils would likely be invalid anyway.** The EDPB's consent guidelines address exactly this. Recital 43 states consent is not a valid ground "where there is a clear imbalance between the data subject and the controller, in particular where the controller is a public authority." The guidelines give a directly on-point school example:

> "**Example 4:** A public school asks students for consent to use their photographs in a printed student magazine. Consent in these situations would be a genuine choice as long as students will not be denied education or services and could refuse the use of these photographs without any detriment."
>
> — [EDPB Guidelines 05/2020 on consent](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf), para 24 and footnote 17 (which defines a public school as "a publically funded school or any educational facility that qualifies as a public authority or body by national law")

The critical inference: consent is only valid in a school setting where the pupil can **refuse without detriment**. A tool that is part of the lesson — where refusing means not doing the coursework — fails that test. Consent would be coerced and therefore invalid. **Trying to rely on consent would make the processing unlawful, not more lawful.**

**Austria explicitly frames school processing as statutory, not consent-based.** The Austrian education ministry states the purpose of processing pupil data is determined by law and oriented to the school's statutory tasks, with categories set out in the Bildungsdokumentationsgesetz; the controller is the school principal per §4(1)(1) BilDokG 2020 ([bmb.gv.at, Datenschutz in Schulen](https://www.bmb.gv.at/Themen/schule/schulrecht/ds.html)).

> **Important caveat.** Public task covers the school's *core educational function*. It does **not** automatically stretch to every optional feature. If the tool does anything beyond delivering the lesson — analytics, product improvement, telemetry, any secondary use — that needs its own basis and public task likely will not cover it. This is a strong argument for keeping the feature set tight.

### The Article 8 age threshold — verified, and probably irrelevant

The ticket asked me to verify the Art 8 ages. **The ticket's premise is partly wrong.**

| Jurisdiction | Age | Source |
|---|---|---|
| GDPR default | 16 | Art 8(1); Member States may lower, "not below 13 years" |
| **Austria** | **14** | §4(4) DSG — **ticket's assumption correct** |
| **Germany** | **16** | No opening-clause provision in BDSG — **ticket's assumption incorrect** |
| UK | 13 | DPA 2018 s9 |

**Austria — verified against statutory text.** §4(4) DSG: *"Bei einem Angebot von Diensten der Informationsgesellschaft, das einem Kind direkt gemacht wird, ist die Einwilligung gemäß Art. 6 Abs. 1 lit. a DSGVO zur Verarbeitung der personenbezogenen Daten des Kindes rechtmäßig, wenn das Kind das vierzehnte Lebensjahr vollendet hat."* — the child must have **completed their fourteenth year** ([Art 2 §4 DSG via JUSLINE](https://www.jusline.at/gesetz/dsg/paragraf/artikel2zu4)).

> *Sourcing note:* the authoritative source is RIS (ris.bka.gv.at), the official Austrian legal information system, which returned HTTP 503 on repeated attempts. JUSLINE is a legal-database republisher, not the official gazette — **treat as high-quality secondary**. The German text quoted is consistent across multiple independent republishers and with the DSFA-V explanatory notes (below), which independently reference the 14-year threshold. **Recommend confirming against RIS directly before relying on this.**

**Germany — verified by absence.** I examined the full table of contents of the BDSG 2018 on [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/) (the official Federal Ministry of Justice portal). Across all 86 paragraphs there is **no provision implementing the Art 8 opening clause** — no children's consent age, no information-society-services age threshold. Germany therefore falls back to the GDPR default of **16**. This is corroborated by secondary sources but the primary-source finding is the absence itself.

> **Confidence note.** Proving a negative from a table of contents is weaker than reading a positive provision. I did not read all 86 paragraph bodies. I am confident (the opening clause would be a headline provision and its absence is widely reported), but this is stated as a well-supported inference rather than a direct quotation.

### Does Article 8 even apply when a school is the controller? Almost certainly not

**No — and this is decisive.** The EDPB states the conditions plainly:

> "It is clear from the foregoing that Article 8 shall only apply when the following conditions are met:
> - The processing is related to the offer of information society services directly to a child.
> - **The processing is based on consent.**"
>
> — [EDPB Guidelines 05/2020](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf), para 127

Both conditions must hold. In the school deployment:

- The processing is based on **public task**, not consent → condition 2 fails.
- The service is offered to **the school**, which then deploys it to pupils — not "directly to a child" → condition 1 is at best doubtful.

**Therefore the 14/16 threshold does not gate the core classroom flow, and you do not need to collect parental consent as a lawfulness precondition, and you do not need age verification for GDPR Art 8 purposes.** This is a significant simplification — it means no parental-consent capture flow in the schema for the core product.

> **Three important qualifications.**
>
> 1. **This flips entirely if pupils can sign up themselves.** If the tool is ever offered direct-to-consumer — a pupil finds it, enters a code, and starts using it outside a school-mediated deployment — then it *is* an information society service offered directly to a child, consent likely becomes the basis, and the full Art 8 machinery (parental consent, "reasonable efforts" to verify age per EDPB para 132–134) engages. **The join-code design makes this a live risk**: a code that circulates outside the classroom is exactly the direct-to-consumer scenario. Consider binding codes to a teacher-provisioned roster rather than allowing open self-registration.
> 2. **Art 8 being inapplicable does not remove child-specific protection.** Recital 38 requires enhanced protection for children generally; the EDPB notes this "is not confined to marketing or profiling but includes the wider 'collection of personal data with regard to children'" (para 124). Transparency obligations in particular must be met in age-appropriate language.
> 3. **Provider terms are contractual and are unaffected by any of this.** Even if GDPR imposes no age gate, OpenAI's and Google's terms independently do. See Q3.

### Legitimate interests

Legitimate interests (Art 6(1)(f)) is **not available to a public authority** performing its tasks — Art 6(1) final sentence disapplies it. If the school is the controller, this basis is closed. It could theoretically be available to the developer acting as an independent controller, but that is the deployment model you should be trying to avoid (see Q4), and the ICO warns public task "is unlikely to be an appropriate lawful basis for edtech providers when they act independently" ([ICO edtech guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/the-children-s-code-and-education-technologies-edtech/)).

> **Open question — unresolved.** Whether the school or the developer is the controller. This is the hinge for most of section 2 and section 4 and it is a factual question about the deployment, not a legal-research question. Resolve it explicitly.

---

## 3. Model provider terms regarding minors

**This section is the most operationally urgent.** Provider terms are contract, they bind you independently of data protection law, and one of the three providers currently prohibits this use case outright.

### Summary table

| | **OpenAI** | **Anthropic** | **Google (Gemini API)** |
|---|---|---|---|
| **(a) Min. age of end user** | 13, and under-18 requires parent/guardian permission | No age floor in Commercial Terms; minors expressly contemplated via API | **18** — hard floor |
| **(b) Minors permitted where business is customer?** | **Yes, with conditions** | **Yes, with conditions** | **No** — expressly prohibited |
| **(c) Training off by default on API?** | **Yes** — since 2023-03-01 | **Yes** — "Anthropic may not train models on Customer Content" | **Paid tier: yes. Free tier: NO** |
| **(d) DPA / zero-retention** | DPA available; ZDR by approval | DPA auto-incorporated; ZDR by approval | DPA via Cloud terms |
| **Default retention** | 30 days (abuse monitoring) | 30 days | Limited period for abuse detection (paid) |
| **Verdict for this project** | Usable **only with ZDR** | **Most viable** | **Blocked as drafted** |

### Google (Gemini API) — currently prohibited

The Gemini API Additional Terms of Service state, under **Age Requirements**:

> "You must be 18 years of age or older to use the APIs. You also will not use the Services as part of a website, application, or other service (collectively, "API Clients") that is directed towards or is likely to be accessed by individuals under the age of 18."

— [ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms)

Two separate restrictions. The second is the one that bites: it is not about who holds the API key, it is about **who the downstream product reaches**. A classroom tool for 12-year-olds is not merely "likely to be accessed by" under-18s — it is *exclusively* accessed by them. I found no educational carve-out and no indication the restriction varies by paid/free tier; it appears in the general terms preceding the tier distinction.

On training, the same terms distinguish tiers sharply — **relevant even if you resolve the age issue**:

- **Unpaid/free tier:** "Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services." → **Free-tier Gemini must never touch pupil data.**
- **Paid tier:** "Google doesn't use your prompts (including associated system instructions, cached content, and files such as images, videos, or documents) or responses to improve our products," with logging "for a limited period of time, solely for detecting and preventing violations."

> **Possible route, UNVERIFIED.** Google Cloud **Vertex AI** is governed by the Google Cloud Platform Terms plus the Cloud Data Processing Addendum, *not* the AI Studio Gemini API terms quoted above. Separately, **Gemini for Education** is documented as "available to students of all ages with enterprise-grade data protection," with under-18 users getting a restricted experience ([Google for Education](https://edu.google.com/intl/ALL_us/ai/gemini-for-education/)). I could **not** locate an equivalent age clause in the Cloud Service Specific Terms — but absence in the sections I read is **not** proof of absence. **Do not treat Vertex AI as cleared.** If Google is wanted, this needs direct confirmation from Google, in writing, before any integration work.

### OpenAI — usable, but Zero Data Retention is a precondition

Base age terms: "You must be at least 13 years old or the minimum age required in your country to consent to use the Services. If you are under 18 you must have your parent or legal guardian's permission to use the Services" ([OpenAI Terms of Use](https://openai.com/policies/row-terms-of-use/)).

The operative document is OpenAI's under-18 API guidance, which contains this requirement:

> "You should not use OpenAI services to process any personal data of children under 13 or the applicable age of digital consent without first implementing zero data retention in our API."

— [Under 18 API Guidance](https://developers.openai.com/api/docs/guides/safety-checks/under-18-api-guidance)

**Applying this to 12-year-olds:** the applicable age of digital consent is 14 (Austria), 16 (Germany), or 13 (UK). Pupils aged 12 are below all three. **ZDR is therefore required on every jurisdictional path.** In the UK a 12-year-old is also under 13, so the first limb applies directly too.

Other stated obligations: age-appropriate disclosures about AI tools; content filters and monitoring; "using age assurance systems to ensure only intended users can access the product" where appropriate; using current flagship models; and compliance with child protection and privacy laws. OpenAI "reserves the right to audit organizations for compliance," with suspension or termination for repeated or serious non-compliance.

Data controls ([Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data)):

- Training: "As of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)." → **off by default; nothing to disable.**
- Default retention: "By default, abuse monitoring logs are generated for all API feature usage and retained for up to 30 days, unless longer retention is required by law."
- ZDR: "subject to prior approval by OpenAI and acceptance of additional requirements" — obtained via OpenAI sales, covering endpoints including `/v1/chat/completions`, `/v1/responses`, `/v1/embeddings`, and the audio endpoints.

> **Practical consequence.** ZDR is a **commercial negotiation with lead time**, not a setting. If OpenAI is the intended provider, start that conversation now — it is on the critical path and cannot be unblocked by writing code. Until ZDR is in place, do not send pupil data to OpenAI.

### Anthropic — most permissive, minors expressly contemplated

The Usage Policy defines a minor as "any individual under the age of 18 years old, regardless of jurisdiction," and rather than prohibiting them, routes them to extra requirements:

> "Products serving minors, including organizations providing minors with the ability to directly interact with products that incorporate our API(s), must comply with the additional guidelines"

— [Anthropic Usage Policy](https://www.anthropic.com/legal/aup)

The referenced guidelines require ([Guidelines for Organizations Serving Minors](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)):

- "Age verification systems to ensure only intended users can access the product"
- "Content moderation and filtering to block inappropriate or harmful content"
- Monitoring and reporting mechanisms
- Educational resources on safe use
- Implementation of Anthropic's child-safety system prompt "as part of a comprehensive suite of safety measures"
- **"Organizations must disclose to their users that they are interacting with an AI system rather than a human."**
- "It is the responsibility of organizations to comply with all applicable child safety and data privacy regulations"

Anthropic reserves audit rights and may suspend for failure to implement safeguards.

I checked the [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) directly for "age", "18", "minor", "child" — **no age restriction appears**. The Commercial Terms note these services "are not for consumer use" and that consumer offerings (Claude.ai) are governed separately; the consumer product is 18+, but **that restriction does not propagate to API customers**.

Training and retention:

- Training: "Anthropic may not train models on Customer Content from Services" ([Commercial Terms](https://www.anthropic.com/legal/commercial-terms)) → **contractually off; nothing to disable.**
- Retention: inputs and outputs are automatically deleted "on our backend within 30 days of receipt or generation," subject to exceptions. Content flagged as violating the Usage Policy may be retained "for up to 2 years and trust and safety classification scores for up to 7 years" ([Anthropic, data retention](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-personal-data)).
- DPA: "Anthropic's DPA with Standard Contractual Clauses (SCCs) is automatically incorporated into the Commercial Terms of Service" ([Anthropic DPA](https://support.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa)) — **no separate signature step**, which is a genuine procurement advantage.
- ZDR available for approved Claude API customers.

> **Note the tension.** Anthropic requires "age verification systems." Section 2 concluded GDPR Art 8 does *not* require age verification here. Both are true — the GDPR obligation is absent but the **contractual** obligation is present. In a teacher-provisioned classroom, roster-based provisioning (the teacher vouches for who is in the class) is the natural way to satisfy "ensure only intended users can access the product." **Whether Anthropic accepts teacher-mediated roster provisioning as satisfying its age-verification requirement is not stated in the guidance and is an open question worth confirming with Anthropic.**

### Cross-cutting

- **The 2-year / 7-year Anthropic retention on flagged content deserves attention.** A 12-year-old triggering a false-positive safety classifier could have their content retained far longer than 30 days. This is worth surfacing in the DPIA and to the school.
- **Self-hosting does not avoid any of this.** Open Notebook's self-hosting story protects the *database*, but the moment a prompt leaves for a third-party LLM, the provider's terms and a processor relationship apply. Self-hosting plus a local model (Ollama etc.) would avoid provider terms entirely — worth evaluating as a genuine architectural alternative given how constrained the hosted options are.
- **All three providers reserve audit rights and termination.** Non-compliance risks losing the provider mid-term, which for a classroom deployment means the tool stops working during a school term.

> **Open question — unresolved.** Whether the project intends a hosted deployment (developer as controller/processor, provider terms apply directly) or self-hosted-per-school (school holds its own API keys and accepts provider terms itself). This changes who is contractually bound.

---

## 4. What a school would require

### DPIA — mandatory, on every path

**UK:** the ICO states that "the nature and context of online services within the scope of children's codes mean they inevitably involve a type of processing likely to result in a high risk to the rights and freedoms of children," and requires a DPIA where you "intend to offer online services directly to children" ([ICO, DPIAs](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/)). DPIA is also **Standard 2** of the Children's Code itself.

**EU:** EDPB WP248 rev.01 lists nine criteria; "in most cases, a data controller can consider that a processing meeting two criteria would require a DPIA." This project meets at least two comfortably:

- **Vulnerable data subjects** — children are the canonical example.
- **Innovative use of technological solutions** — LLM/AI processing.

Add **large-scale** if deployed beyond one class, and arguably **evaluation/scoring** if quiz results are used to assess pupils.

**Austria:** the DSFA-V (BGBl II 278/2018) explanatory notes explicitly define children under 14 as vulnerable data subjects: *"Als schutzbedürftige Betroffene gelten Kinder bis zum vollendeten 14. Lebensjahr (bei ihnen kann nicht davon ausgegangen werden, dass sie in der Lage sind, der Verarbeitung ihrer Daten wissentlich und überlegt zu widersprechen bzw. zuzustimmen)"* ([Erläuterungen zur DSFA-V](https://dsb.gv.at/sites/site0344/media/downloads/erlaeuterungen_zur_dsfa-v.pdf)). The notes stress that absence from the list does not mean no DPIA is required — the controller must assess under Art 35(1) regardless.

**Germany:** the DSK Muss-Liste states in terms: *"Diese Liste ist nicht abschließend, sondern ergänzt die in den Absätzen 1 und 3 des Artikels 35 DSGVO enthaltenen allgemeinen Regelungen"* ([DSK Muss-Liste, LDA Bayern](https://www.lda.bayern.de/media/dsfa_muss_liste_dsk_de.pdf)). No listed entry covers AI-in-schools directly, so the obligation arises from Art 35(1) plus WP248 criteria rather than the blacklist.

**Conclusion: assume a DPIA is required. Do it early** — it is the artefact a school's DPO will ask for first, and it is far cheaper to write alongside the schema than to retrofit. The ICO publishes a [DPIA template annexed to the Children's Code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/annex-d-dpia-template/) which is usable as a starting structure even outside the UK.

### ICO Children's Code — probably not binding, but read it anyway

The ticket assumes the Code applies. **It may well not** — this is a correction worth flagging.

**Schools are out of scope:** the Code "does not apply to schools and educational and training institutions processing the information of people under the age of 18 for the purposes of education," because schools do not meet the definition of an Information Society Service ([ICO edtech guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/the-children-s-code-and-education-technologies-edtech/)).

**Edtech providers are out of scope where all three of these hold:**

1. The service is not accessed on a direct-to-consumer basis;
2. The provider only processes children's data to fulfil the school's public tasks and educational functions, as determined by the school;
3. The provider acts solely on the school's instruction and does not process children's data beyond those instructions.

Critically, the ICO warns that role "is not determined by your designation as a processor or controller as set out in a contract, but whether you in fact exercise control over the means and purposes of processing." **You cannot contract your way out of controllership.** Any product analytics, telemetry, model-improvement use, or feature the school did not ask for could pull the project back into scope.

Note also the DPA 2018 s123 basis: the Code covers "information society services which involve the processing of personal data to which the UK GDPR applies" ([DPA 2018 s123](https://www.legislation.gov.uk/ukpga/2018/12/section/123)). An ISS is a service "normally provided for remuneration" — an unpaid open-source tool may fall outside on that ground too, though the "normally" qualifier means free-at-point-of-use services can still qualify if the sector is normally paid.

**Recommendation regardless:** build to the Code's standards. It is the best-articulated statement anywhere of what good looks like for children's services, an EU school's DPO will recognise its logic even without UK jurisdiction, and conforming is cheap if done from the start. The standards that bite hardest here: **best interests of the child** (Standard 1), **DPIA** (2), **age-appropriate application** (3), **transparency in language a child understands** (4), **data minimisation** (6), **high-privacy default settings** (7), and **no nudge techniques** (13) ([ICO, Code standards](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/code-standards/)).

### Data processing agreement

Art 28 GDPR requires a written contract between controller and processor. Two layers here:

1. **School ↔ this project.** If the school is controller and the project is processor, the school will require a DPA from you. Schools typically have a standard template; expect to sign theirs rather than propose your own.
2. **This project ↔ LLM provider.** You need a DPA in place with each provider, and the school will ask to see it, because the provider is a **sub-processor** and Art 28(2) requires the controller's authorisation for sub-processors.
   - Anthropic: DPA with SCCs auto-incorporated on accepting Commercial Terms.
   - OpenAI: DPA available; ZDR requires separate approval.
   - Google: via Cloud Data Processing Addendum.

**International transfers.** All three providers are US-headquartered. Transfers out of the UK/EEA need a mechanism — SCCs, the UK IDTA/Addendum, or reliance on the EU-US Data Privacy Framework where the provider is certified. Anthropic's SCCs are incorporated automatically.

> **Open question — unresolved.** Whether the specific providers are currently DPF-certified, and whether EU data residency / regional processing endpoints are available and would satisfy the school. I did not verify certification status; DPF participation changes over time and should be checked against the official DPF list at the point of procurement.

### Retention and deletion

No fixed statutory period applies to this kind of data; the requirement is Art 5(1)(e) storage limitation — keep it no longer than necessary. In practice a school will expect:

- A **stated retention period** tied to the academic year or course.
- **Automatic deletion** at the end of it, not manual cleanup.
- **Deletion on pupil departure** — a pupil leaving the school should have data removed.
- **Deletion on request** without disproportionate effort.
- Consideration of what happens **at contract termination** — the school will want data returned or destroyed.

Children's data attracts a stricter reading here. Under the Children's Code, minimisation means collecting and retaining "only the minimum amount of personal data you need." An explicit, short, automated retention policy is one of the cheapest ways to look credible to a DPO.

### Subject access requests

Data subject rights apply in full: access (Art 15), rectification (16), erasure (17), restriction (18), portability (20), objection (21).

- **The child is the data subject and holds the rights**, not the parent. Depending on maturity, a competent child can exercise their own rights; a parent may exercise them on the child's behalf where the child lacks capacity or authorises it. The ICO addresses this in [Accessing pupils' information](https://ico.org.uk/for-the-public/schools/pupils-info/).
- **The school, as controller, receives and answers the request** — but it can only do so if your system lets it. **This is a schema requirement:** you must be able to export everything associated with a pupil, and delete it, on demand. If pupil work is scattered across notebooks, sources, notes, generated flashcards, quiz answers, and chat sessions with no single pupil key, SARs become extremely painful. **Design a clean per-pupil ownership key now.**
- One month is the standard response deadline, so the export must be operationally practical, not a database archaeology exercise.
- Note that data sent to an LLM provider and retained in abuse-monitoring logs is **not** practically retrievable or deletable by you — another argument for zero-retention arrangements.

### Approved-supplier lists

**Yes, realistically.** Schools generally cannot adopt arbitrary software. Expect some combination of: the school's or trust's own procurement/DPO approval; a completed supplier data protection questionnaire; evidence of the DPIA; the DPA; security assurances; and in Germany, potentially a state-level (Land) approved-tools list, since school data protection is a Länder competence and several states publish explicit rulings on which cloud tools schools may use.

> **Open question — unresolved.** Whether the specific target school sits under a formal approved-supplier regime, and in Germany which Bundesland's rules apply. Also unverified: whether any relevant authority has published a position on US-hosted LLM providers in schools specifically — several German state DPAs have published critical positions on US cloud services in education, which could be decisive. **This is worth a dedicated follow-up once the jurisdiction is known.**

---

## 5. Practical minimums

The smallest defensible set. Ordered by whether it blocks the build.

### Blocking — resolve before schema and auth are frozen

1. **Confirm jurisdiction** (UK / Austria / Germany, and if Germany, which Bundesland). Everything in section 2 and 4 keys off this.
2. **Confirm who the controller is** — school or developer. Write it down and make the deployment match it.
3. **Pick the provider against the terms, not preference.** Google Gemini API is prohibited as drafted. OpenAI requires ZDR approval (start now — it has lead time). Anthropic is the least constrained. A local model avoids provider terms entirely.
4. **Design a single per-pupil ownership key** across every record type — pupil work, generated flashcards, quiz answers, chat sessions. Without it, SARs and deletion are impractical. This is the single most important schema consequence of this research.
5. **Decide the join-code model.** Open self-registration risks converting the tool into a direct-to-consumer ISS offered directly to children, which re-engages Art 8, the ICO Children's Code, and parental-consent requirements. **Teacher-provisioned rosters avoid this.** Codes should be single-class, expiring, and revocable.

### Technical measures

6. **Collect nothing you do not need.** No email, no real name, no DOB, no avatar upload, no geolocation, no analytics on pupils. Every field is a liability you must later export, delete, and justify.
7. **Zero data retention with the LLM provider** where available — required for OpenAI, worth requesting from Anthropic.
8. **Automated retention expiry** — delete pupil data at the end of the academic year by default, as a scheduled job, not a manual chore.
9. **Encryption in transit and at rest**, and a hosting location the school will accept (EU/UK region if EU/UK school).
10. **Access control**: a teacher sees only their own class; a pupil sees only their own work; no pupil-to-pupil visibility unless the feature explicitly requires it and the school agrees.
11. **Content moderation / safety filtering** on both prompts and model output — this is a contractual requirement of both Anthropic and OpenAI for minors, not optional.
12. **Implement the provider's child-safety system prompt** if using Anthropic.
13. **Audit logging** of access to pupil data, retained separately from the pupil data itself.
14. **No training, no secondary use, no telemetry on pupil content** — and never a free/unpaid Gemini tier.
15. **Export function** producing everything held about one pupil, in a readable format.

### Organisational measures

16. **Write the DPIA.** Use the ICO Annex D template. Do it now, not at deployment.
17. **Sign DPAs** — with the provider, and with the school.
18. **Age-appropriate privacy notice** — written so a 12-year-old can actually understand it. This is a Children's Code standard and an EDPB expectation (Recital 58), and it is genuinely useful regardless of jurisdiction.
19. **Disclose clearly that pupils are talking to an AI, not a human** — explicit Anthropic requirement, and good practice generally.
20. **Documented retention and deletion policy**, and a **documented SAR procedure** naming who does what within one month.
21. **Breach procedure** — 72-hour notification to the supervisory authority under Art 33; as processor you must notify the school "without undue delay."
22. **Record of processing activities** (Art 30).
23. **Keep the feature set tight to the educational purpose.** Public task covers the lesson. It does not cover everything you might like to build. Scope creep is a legal risk here, not just a product one.

---

## Confidence and gaps

Stated plainly, because these findings will carry weight in design decisions.

**High confidence — verified against primary sources:**
- Display name + join code is personal data; pseudonymisation does not exempt (ICO guidance + Art 4 text).
- Art 8 applies only where processing is consent-based and offered directly to a child (EDPB para 127, direct quotation).
- Consent in a school context is constrained by imbalance of power (EDPB Example 4, direct quotation).
- Austrian digital-consent age is 14 (statutory text, though via a republisher — see caveat).
- Google Gemini API prohibits under-18-directed services (direct quotation from Google's own terms).
- OpenAI's ZDR requirement for under-digital-consent-age data (direct quotation from OpenAI's docs).
- Anthropic permits minors subject to additional guidelines (direct quotations from Anthropic's policy and help centre).
- Training defaults and retention periods for all three providers (direct quotations).
- ICO position that schools are not ISS and edtech-on-school-instruction is out of Code scope (ICO guidance).
- DSK Muss-Liste and Austrian DSFA-V are non-exhaustive (direct German quotations).

**Medium confidence — well-supported inference, not a direct positive citation:**
- Germany's digital-consent age is 16. Established by *absence* of an opening-clause provision in the BDSG table of contents rather than by a positive provision. I did not read all 86 paragraph bodies.
- Austrian §4(4) DSG text via JUSLINE, not RIS (RIS returned 503 repeatedly). Corroborated by the DSFA-V explanatory notes.

**Explicitly NOT verified — do not rely on these:**
- **Whether Vertex AI / Gemini for Education escapes the 18+ restriction.** I could not find an equivalent clause in Cloud terms, but absence-in-what-I-read is not absence. **Confirm with Google in writing before building.**
- **Whether the providers are currently DPF-certified** and what transfer mechanism each relies on today.
- **Whether Anthropic accepts teacher-mediated roster provisioning** as satisfying its "age verification systems" requirement.
- **Any German Bundesland's specific school-IT rules or approved-tool lists**, or state DPA positions on US LLM providers in schools. Not researched because the state is unknown, and potentially decisive.
- **Whether the target school has an approved-supplier regime.**
- **The full text of the ICO Children's Code standards pages.** ico.org.uk returned HTTP 403 to direct fetches throughout; ICO content here comes from ICO-domain search result summaries rather than full page reads. The substance is consistent across multiple ICO pages, but I did not read the standards pages end to end. **Read them directly before relying on standard-by-standard detail.**
- **Austrian/German school-law provisions** establishing the precise statutory basis for the public-task argument. I confirmed the framing via the Austrian ministry but did not read the Schulgesetze or Bildungsdokumentationsgesetz directly.

**Correction to the ticket's premises:**
- The ticket (via the task brief) assumed Germany sets the Art 8 age at 14. **It is 16.**
- The ticket assumed the ICO Age Appropriate Design Code applies. **It likely does not**, on either the jurisdictional path or the school-deployment path — though building to it is still recommended.

---

## Sources

All accessed **2026-07-29**. Marked **[P]** primary (legislation, regulator, or the provider's own terms), **[S]** secondary.

### Legislation and regulatory guidance

- **[P]** UK GDPR Article 4 (definitions of personal data, pseudonymisation) — https://www.legislation.gov.uk/eur/2016/679/article/4
- **[P]** Data Protection Act 2018, s123 (age-appropriate design code) — https://www.legislation.gov.uk/ukpga/2018/12/section/123
- **[P]** BDSG 2018, full table of contents (Bundesministerium der Justiz) — https://www.gesetze-im-internet.de/bdsg_2018/
- **[S]** Austrian DSG §4 (Art 2 §4), via JUSLINE — https://www.jusline.at/gesetz/dsg/paragraf/artikel2zu4 *(republisher; RIS unavailable — verify against ris.bka.gv.at)*

### EDPB

- **[P]** EDPB Guidelines 05/2020 on consent under Regulation 2016/679, v1.1 — https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf *(Example 4 school/consent at para 24 and fn 17; Art 8 conditions at para 127; age verification at paras 130–134)*

### ICO (UK)

- **[P]** The Children's code and education technologies (edtech) — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/the-children-s-code-and-education-technologies-edtech/
- **[P]** Code standards (the 15 standards) — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/code-standards/
- **[P]** Introduction to the Children's code — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/introduction-to-the-childrens-code/
- **[P]** Pseudonymisation — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/pseudonymisation/
- **[P]** What is personal data? — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/what-is-personal-data/
- **[P]** Public task (lawful basis) — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/public-task/
- **[P]** When do we need to do a DPIA? — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/
- **[P]** Annex D: DPIA template — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/annex-d-dpia-template/
- **[P]** Accessing pupils' information — https://ico.org.uk/for-the-public/schools/pupils-info/

> *Access caveat: ico.org.uk returned HTTP 403 to direct page fetches. ICO content above is drawn from ICO-domain search result summaries. Substance was consistent across multiple ICO pages, but full-page verification was not possible.*

### Austria / Germany DPA materials

- **[P]** Erläuterungen zur DSFA-V, Datenschutzbehörde (Austria) — https://dsb.gv.at/sites/site0344/media/downloads/erlaeuterungen_zur_dsfa-v.pdf *(children under 14 as vulnerable data subjects; non-exhaustiveness of the list)*
- **[P]** DSK Muss-Liste — Liste der Verarbeitungstätigkeiten, für die eine DSFA durchzuführen ist (LDA Bayern) — https://www.lda.bayern.de/media/dsfa_muss_liste_dsk_de.pdf *("Diese Liste ist nicht abschließend")*
- **[P]** Datenschutz in Schulen, BMB Austria — https://www.bmb.gv.at/Themen/schule/schulrecht/ds.html
- **[P]** Verordnungen in Österreich, Datenschutzbehörde — https://www.dsb.gv.at/recht-entscheidungen/verordnungen-in-oesterreich.html

### Provider terms — OpenAI

- **[P]** Under 18 API Guidance — https://developers.openai.com/api/docs/guides/safety-checks/under-18-api-guidance
- **[P]** Data controls in the OpenAI platform — https://developers.openai.com/api/docs/guides/your-data
- **[P]** Terms of Use — https://openai.com/policies/row-terms-of-use/
- **[P]** Usage policies — https://openai.com/policies/usage-policies/
- **[P]** Enterprise privacy — https://openai.com/enterprise-privacy/

### Provider terms — Anthropic

- **[P]** Usage Policy — https://www.anthropic.com/legal/aup
- **[P]** Commercial Terms of Service — https://www.anthropic.com/legal/commercial-terms
- **[P]** Responsible Use of Anthropic's Models: Guidelines for Organizations Serving Minors — https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors
- **[P]** How long do you store personal data (commercial) — https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-personal-data
- **[P]** How do I view and sign your Data Processing Addendum (DPA)? — https://support.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa
- **[P]** Zero retention agreement scope — https://privacy.anthropic.com/en/articles/8956058-i-have-a-zero-retention-agreement-with-anthropic-what-products-does-it-apply-to

### Provider terms — Google

- **[P]** Gemini API Additional Terms of Service — https://ai.google.dev/gemini-api/terms *(the 18+ clause)*
- **[P]** Google Cloud Service Specific Terms — https://cloud.google.com/terms/service-terms
- **[P]** Gemini for Education — https://edu.google.com/intl/ALL_us/ai/gemini-for-education/
- **[P]** Generative AI in Google Workspace Privacy Hub — https://support.google.com/a/answer/15706919

### Secondary (used only for corroboration, not as sole basis for any claim)

- **[S]** Library of Congress, *Children's Online Privacy and Data Protection in Selected European Countries* — https://tile.loc.gov/storage-services/service/ll/llglrd/2021680641/2021680641.pdf *(fetch returned 403; cited from search result metadata only)*
- **[S]** EuConsent, Digital Age of Consent under the GDPR — https://euconsent.eu/digital-age-of-consent-under-the-gdpr/
