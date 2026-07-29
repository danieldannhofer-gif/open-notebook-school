# Who is the data controller, and what lawful basis survives?

Research for [issue #11](https://github.com/danieldannhofer-gif/open-notebook-school/issues/11). All sources accessed **2026-07-29**.

> **Scope note.** This is engineering research against primary sources, not legal advice. This ticket re-derives the lawful-basis conclusion from [#8](https://github.com/danieldannhofer-gif/open-notebook-school/issues/8) (`docs/research/data-protection-for-minors.md`) under changed facts established by [#3](https://github.com/danieldannhofer-gif/open-notebook-school/issues/3): the tool is **self-hosted by an individual teacher, on their own infrastructure, for a real class of other people's children, outside the school's IT estate**.

---

## Answer

The decision-relevant conclusions, ordered by how much they change the build:

- **The unsanctioned deployment shape is not lawful, and no schema change can fix it.** This is the headline finding and it is stronger than expected. Baden-Württemberg's Kultusministerium states flatly that a teacher may not conclude an Art 28 processing agreement, and that one concluded by a teacher **is invalid** — *"Ein solcher Vertrag, der durch eine Lehrkraft abgeschlossen wurde, ist ungültig. Die Datenübermittlung an den Anbieter ist damit unzulässig und stellt ggf. einen meldepflichtigen Datenschutzverstoß dar."* Since this project necessarily sends pupil data to an LLM provider (a processor), and only the Schulleitung can validly sign that DPA, **the teacher-operated deployment is unlawful at the point the first prompt leaves the box** — independent of consent, schema, or basis. See [Q4](#4-does-school-sanction-re-establish-public-task) and [Q6](#6-the-honest-risk-picture).
- **The correct engineering answer is that this must be school-sanctioned before it can lawfully run.** Not "should be". The project owner asked for this plainly and the sources support it plainly. The deployment shape itself must change. See [Q6](#6-the-honest-risk-picture).
- **The teacher is almost certainly NOT the controller — the school is, even for unsanctioned shadow IT.** This is the counter-intuitive core finding and it cuts *against* the ticket's premise. EDPB Guidelines 07/2020 para 19: *"any processing of personal data by employees which takes place within the realm of activities of an organisation may be presumed to take place under that organisation's control"*, with employees being *"persons acting under the authority of the controller"* (Art 29). Teaching a class is squarely within the school's realm of activities. Three German Länder and Austria state expressly that the school/Schulleitung remains controller **even when teachers process pupil data on their own private IT**. See [Q1](#1-who-is-the-controller).
- **Therefore public task (Art 6(1)(e)) SURVIVES — but conditionally, and it is the school's basis, not the teacher's.** #8's finding is not void; it is *relocated*. The basis attaches to the institution discharging its statutory education function, and the teacher acts under its authority. NRW practice grounds classroom AI tools in §§ 120(1), 121(1) SchulG NRW + Art 6(1)(e). But this only holds if the school in fact accepts the processing as its own — which an unsanctioned deployment denies it the chance to do. See [Q2](#2-what-is-the-lawful-basis).
- **Consent is NOT the answer and would not rescue the deployment.** #8's imbalance finding survives the change of controller intact, because EDPB Example 4's test is **detriment**, not the controller's public-authority status: consent is valid *"as long as students will not be denied education or services and could refuse ... without any detriment."* Coursework you must do fails that test whoever hosts it. Consent would make the processing *less* lawful, not more.
- **Legitimate interests does NOT reopen.** The Art 6(1)(f) public-authority bar is disapplied only for the *controller* — and the controller is the school. Even entertaining the teacher-as-controller branch, Art 6(1)(f) expressly subordinates the interest *"in particular where the data subject is a child"*, and the balancing fails on children's coursework processed through US LLM providers. See [Q2](#2-what-is-the-lawful-basis).
- **Schema consequence: DO NOT build a parental-consent table.** Consent is the wrong basis under both the sanctioned (public task) and unsanctioned (unlawful regardless) branches. Building consent machinery would encode a legally wrong model and create a false assurance that the deployment is fixable by capturing signatures. Keep the per-pupil ownership key from #8. **Q3's answer is "no new table".** See [Q3](#3-if-consent-is-required-whose-and-what-must-the-schema-hold).
- **The DPIA is still mandatory and it is the SCHOOL's to do**, not the teacher's — Art 35(1) places it on the controller. This is another artefact the teacher cannot validly produce alone. See [Q5](#5-is-a-dpia-still-mandatory-and-who-must-do-it).
- **The Art 2(2)(c) household exemption does not apply and is not arguable.** Recital 18 confines it to activity *"with no connection to a professional or commercial activity"*. Teaching one's own class is the teacher's profession. See [Q1](#the-household-exemption-art-22c--dismissed).

**What the teacher must actually obtain** (the concrete artefact list) is in [Q4](#4-does-school-sanction-re-establish-public-task). The minimum is: written authorisation from the Schulleitung, an Art 28 DPA signed *by the school* with the LLM provider, and involvement of the school's DPO.

---

## Jurisdiction

Austria and Germany are the live candidates; UK is secondary comparison. **The controller answer is the same in all three.** What varies is the statutory hook.

| Question | Austria | Germany | UK |
|---|---|---|---|
| Who is controller for pupil data | **School principal**, expressly by statute — § 4 Abs 1 Z 1 BilDokG 2020 | **School, represented by the Schulleitung** — per Land guidance (NI, NRW, BW, BY) | The school / academy trust |
| Statutory hook for public task | Schulgesetze + BilDokG 2020 | **Landesschulgesetze** (e.g. §§ 120, 121 SchulG NRW) | Public task, Art 6(1)(e) |
| Level of competence | Federal (BilDokG) | **Bundesland** — varies by state | National |
| Art 8 digital-consent age | 14 (§ 4(4) DSG) | 16 (no opening-clause law) | 13 (DPA 2018 s9) |
| Regulator | DSB | Landesbeauftragte (per Land) | ICO |
| Teacher may sign a DPA? | No (principal is controller) | **No — expressly invalid** (BW FAQ 44) | No (school is controller) |

> **Germany — Bundesland dependency.** School data protection is Länder competence. The *controller* finding is consistent across the four states I checked (Niedersachsen, NRW, Baden-Württemberg, Bayern) and I regard it as safe. What is **state-specific** and would need checking for the actual state: the precise school-law provision supplying the Art 6(1)(e) hook; whether the Land mandates particular platforms (NRW pushes LOGINEO NRW); whether the Land has published a position on US LLM providers in schools; and the exact authorisation form for private-device processing.

> **Open question — unresolved.** The specific jurisdiction and (if Germany) the Bundesland remain unconfirmed, carried over from #8. The load-bearing conclusions of this document do **not** turn on it, which is a change from #8 — the controller analysis converges.

---

## 1. Who is the controller?

**The school is. Not the teacher.** This is the opposite of the ticket's working assumption, and it is well supported.

### The general rule: employees are not controllers

EDPB Guidelines 07/2020 set out the controller concept in three building blocks. On *who* can be a controller (para 17):

> "Under the GDPR, a controller can be 'a natural or legal person, public authority, agency or other body'. This means that, in principle, there is no limitation as to the type of entity that may assume the role of a controller. It might be an organisation, but it might also be an individual or a group of individuals. In practice, however, it is usually the organisation as such, and not an individual within the organisation (such as the CEO, an employee or a member of the board), that acts as a controller within the meaning of the GDPR."

— [EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR](https://www.edpb.europa.eu/system/files/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf), para 17

So *a* teacher could in principle be a controller — the entity type is no obstacle. But the operative presumption is para 19, which is the single most important passage for this ticket:

> "In principle, any processing of personal data by employees which takes place within the realm of activities of an organisation may be presumed to take place under that organisation's control. In exceptional circumstances, however, it may occur that an employee decides to use personal data for his or her own purposes, thereby unlawfully exceeding the authority that he or she was given. (e.g. to set up his own company or similar). It is therefore the organisation's duty as controller to make sure that there are adequate technical and organizational measures, including e.g. training and information to employees, to ensure compliance with the GDPR."

— *ibid.*, para 19

And its footnote 9:

> "Employees who have access to personal data within an organisation are generally not considered as 'controllers' or 'processors', but rather as 'persons acting under the authority of the controller or of the processor' within the meaning of article 29 GDPR."

— *ibid.*, fn 9

Art 29 GDPR itself:

> "The processor and any person acting under the authority of the controller or of the processor, who has access to personal data, shall not process those data except on instructions from the controller, unless required to do so by Union or Member State law."

— [Art 29 GDPR](https://gdpr-info.eu/art-29-gdpr/)

### Applying para 19 to unsanctioned shadow IT

The exception in para 19 is narrow and its stated trigger is **the employee pursuing their own purposes** — the example given is *"to set up his own company or similar"*. That is not these facts. A teacher building a flashcard tool to teach their own class is pursuing **the school's purpose** (educating those pupils), using the school's data, on the school's roster, during the school's lessons. The purpose is institutional even though the infrastructure is personal.

That distinction — *whose purpose*, not *whose server* — is what para 19 turns on, and it is reinforced by para 18's marketing-department example, where a department acting *"with considerable independence"* still does not become the controller, because the activity *"takes place within the realm of its business activities and for its purposes."*

**This means unsanctioned shadow IT does not transfer controllership to the teacher.** It makes the school a controller that is in breach — processing it has failed to govern, secure, document, or lawfully contract for. The school does not escape controllership by being unaware; controllership is factual, not consensual.

Note the asymmetry this creates, which is the uncomfortable heart of the ticket: **the teacher gets the school's liability exposure without the school's authority to discharge it.** The school is on the hook for a system it cannot see; the teacher personally holds the risk described in [Q6](#6-the-honest-risk-picture) without being able to sign the paperwork that would make it lawful.

### National guidance confirms it — including for private IT

This is not merely an inference from EDPB text. Four German Länder and Austria say it directly, and several address teachers' *private* systems specifically.

**Niedersachsen** — squarely on the private-IT point:

> "'Verantwortlicher' im Sinne der DSGVO ist daher auch in diesen Fällen die Schule, vertreten durch die Schulleiterin oder den Schulleiter."
>
> *("The 'controller' within the meaning of the GDPR is therefore, in these cases too, the school, represented by the head teacher.")*

— [Landesbeauftragte für den Datenschutz Niedersachsen / NiBiS, *Verarbeitung personenbezogener Daten auf privaten IT-Systemen von Lehrkräften*](https://datenschutz.nibis.de/2020/02/24/verarbeitung-personenbezogener-daten-auf-privaten-informationstechnischen-systemen-it-systemen-von-lehrkraeften/) (basis: RdErl. d. MK v. 01.01.2020, Nds. MBl. 2020 S. 153; § 31 NSchG). The same page provides an *"Antrag auf Genehmigung"* — an application form for authorisation — confirming that private-IT processing is permitted only with the head's prior approval.

**Nordrhein-Westfalen:**

> "Grundsätzlich ist die Schulleitung die für die Verarbeitung personenbezogener Daten verantwortliche Stelle."
>
> "Dies ist nur zulässig, soweit es zur Erfüllung schulischer Aufgaben erforderlich ist. Dazu bedarf es einer qualifizierten Genehmigung der Schulleitung."

— [Medienberatung NRW, *Dienstliche Verarbeitung personenbezogener Daten auf privaten Endgeräten*](https://www.medienberatung.schulministerium.nrw.de/de/themen/datenschutz_1/anwendung/fragen_zur_dienstlichen_verarbeitung_personenbezogener_daten_auf_privaten_endgeraeten.html)

**Baden-Württemberg:**

> "Auch bei einer Verarbeitung von personenbezogenen Daten zu schulischen Zwecken auf privaten Geräten bleibt die Schule, diese vertreten durch die Schulleiter, datenschutzrechtlich verantwortlich."

— [Kultusministerium Baden-Württemberg, *FAQ Datenschutz an Schulen*, Stand 05/2024](https://it.kultus-bw.de/site/pbs-bw-rebrush2024/get/documents_E1205840066/KULTUS.Dachmandant/KULTUS/Dienststellen/it.kultus-bw/Datenschutz%20an%20Schulen%20nach%20neuer%20EU%20DSGVO/dl-service/FAQ%20Datenschutz%20an%20Schulen%20EUDSGVO.pdf), FAQ 37

BW also grounds the head's control rights in the controller role itself: *"Das Kontrollrecht ergibt sich aus der Rolle der Schulleitung als verantwortliche Stelle nach Art. 24 Abs. 1 i.V. Art. 4 Abs. 7 EU-DSGVO."*

**Austria — controller is fixed by statute:**

> "Verantwortlicher im Sinne des Art. 4 Nr. 7 DSGVO sind nach der ausdrücklichen Festlegung des § 4 Abs. 1 Z 1 BilDokG 2020 die Schulleiterinnen und Schulleiter."

— [BMBWF, *Datenschutz-Folgenabschätzungen zum Bildungsdokumentationsgesetz 2020*](https://www.bmb.gv.at/dam/jcr:48645b5d-c90e-4dd8-8216-6b8b370d6bfd/dsfa_bil_dok_g_2020.pdf), p. 22

Corroborated by the ministry's public page: *"Verantwortlicher im Sinne der DSGVO ist grundsätzlich die jeweilige Schulleiterin beziehungsweise der jeweilige Schulleiter"* ([BMB, *Datenschutz in Schulen*](https://www.bmb.gv.at/Themen/schule/schulrecht/ds.html)).

Austria is the strongest case of the three: controllership is **defined by law** (which EDPB para 20 expressly contemplates: *"This controllership may be defined by law or may stem from an analysis of the factual elements"*), so a teacher cannot become controller by unilateral act — the statute has already allocated the role to the principal.

### Joint controllership with the school (Art 26)?

**Unlikely on the unsanctioned facts, and it is not a useful escape route.**

Art 26(1): *"Where two or more controllers jointly determine the purposes and means of processing, they shall be joint controllers."* ([Art 26 GDPR](https://gdpr-info.eu/art-26-gdpr/))

The EDPB test (para 53):

> "The overarching criterion for joint controllership to exist is the joint participation of two or more entities in the determination of the purposes and means of a processing. More specifically, joint participation needs to include the determination of purposes on the one hand and the determination of means on the other hand."

— EDPB Guidelines 07/2020, para 53

Joint participation can arise from *"a common decision"* or from *"converging decisions ... where the decisions complement each other and are necessary for the processing to take place"* (paras 54–55, and the Executive Summary). The assessment is *"carried out on a factual, rather than a formal, analysis of the actual influence"* (para 52).

Applying this:

| Scenario | Analysis |
|---|---|
| **School doesn't know** | No joint controllership — the school has made no decision at all, so there is nothing to converge with. The school is nonetheless **sole controller** via para 19 (employee acting within its realm of activities). The teacher is a person acting under its authority who has exceeded that authority. |
| **School knows and approves** | Cleanest case: school is controller, teacher acts under its authority (Art 29), tool is school-sanctioned. **Not** joint controllership — the teacher isn't determining purposes in their own right, they are executing the school's. |
| **School knows, tolerates, doesn't formally adopt** | The messy middle. Arguably converging decisions — the school decides the pupils/curriculum/roster, the teacher decides the tool/infrastructure/provider. A joint-controllership finding is *conceivable* here. But it is the worst outcome for the teacher, not a shelter: Art 26(3) says *"The data subject may exercise his or her rights under this Regulation in respect of and against each of the controllers."* Joint controllership means joint exposure, plus an Art 26 arrangement obligation nobody has drafted. |

**Does school knowledge/approval change the answer?** It changes the *lawfulness*, not the *identity* of the controller. In all three scenarios the school is a controller. Approval is what makes the school's controllership *compliant* — because approval is the gateway to the DPA, the DPIA, and the Art 6(1)(e) hook. See [Q4](#4-does-school-sanction-re-establish-public-task).

### The household exemption (Art 2(2)(c)) — dismissed

The ticket asked for this to be addressed and dismissed with reasoning. It does not apply, and the dismissal is not close.

Art 2(2)(c) disapplies the GDPR to processing *"by a natural person in the course of a purely personal or household activity"* ([Art 2 GDPR](https://gdpr-info.eu/art-2-gdpr/)).

Recital 18 supplies the operative limit:

> "This Regulation does not apply to the processing of personal data by a natural person in the course of a purely personal or household activity and thus **with no connection to a professional or commercial activity**. Personal or household activities could include correspondence and the holding of addresses, or social networking and online activity undertaken within the context of such activities. However, this Regulation applies to controllers or processors which provide the means for processing personal data for such personal or household activities."

— [Recital 18 GDPR](https://gdpr-info.eu/recitals/no-18/) (emphasis added)

Four independent reasons it fails, any one sufficient:

1. **It is professional activity by definition.** The teacher is teaching their own class as their job. Recital 18's "no connection to a professional activity" is not satisfied — the connection *is* the activity.
2. **The data subjects are third parties, not the operator's household.** These are other people's children, enumerated from a school roster.
3. **The word "purely" is doing work.** The CJEU requires narrow construction. In *Ryneš* the Court held the exception *"must be narrowly construed"*, since provisions governing processing liable to infringe fundamental freedoms *"must necessarily be interpreted in the light of the fundamental rights set out in the Charter"*, and that an activity *"directed outwards from the private setting of the person processing the data ... cannot be regarded as an activity which is a purely 'personal or household' activity"* — [CJEU C-212/13 *František Ryneš*, ECLI:EU:C:2014:2428](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62013CJ0212_SUM). A classroom of 12 other households' children is as "directed outwards" as it gets.
4. **Recital 18's last sentence closes the remaining gap.** Even where the exemption *does* apply to an end user, it *"applies to controllers or processors which provide the means for processing"* — so the software and the LLM provider remain in scope regardless.

> **Sourcing caveat.** EUR-Lex and InfoCuria returned bot-challenge responses (HTTP 202/403) on repeated direct fetch attempts, so the *Ryneš* language above is quoted from search-result extracts of the judgment rather than a full-text read of the official report. The propositions (narrow construction; "directed outwards") are stable, widely reported, and consistent across sources, but **treat the exact wording as medium confidence** and verify against the official report if it becomes load-bearing. It is not load-bearing here — reasons 1 and 2 dispose of the point on the Recital 18 text alone, which I did verify.

---

## 2. What is the lawful basis?

### Public task survives — attached to the school, exercised through the teacher

**#8's public-task conclusion is not void. It is relocated and made conditional.** The reasoning in #8 was right that public task is the basis; what #8 didn't test is that the basis belongs to the **institution**, and that the teacher's personal hosting doesn't detach it — because, per [Q1](#1-who-is-the-controller), the teacher isn't the controller.

Art 6(1)(e) covers processing *"necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller"* ([Art 6 GDPR](https://gdpr-info.eu/art-6-gdpr/)). Art 6(3) requires that basis be laid down in Union or Member State law.

**Can a teacher exercise a public task personally?** Essentially no — and the question is slightly malformed. The official authority is *vested in the controller* (Art 6(1)(e)'s own words), and the controller is the school. The teacher exercises it **as** the school, under Art 29, not in their own right. A teacher who steps outside the school's authority doesn't take the public task with them; they simply lose the cover of it. The task stays with the institution.

This is exactly how German practice grounds classroom AI tools. For NRW, the legal basis given for AI platform use with pupils is:

> "§ 120 Abs. 1 Satz 1 und § 121 Abs. 1 Satz 1 SchulG NRW ... Art. 6 Abs. 1 lit. e DS-GVO — Verarbeitung zur Wahrnehmung einer Aufgabe im öffentlichen Interesse – staatlicher Bildungs- und Erziehungsauftrag"

with the explicit corollary that *"Eine Einwilligung ist hierfür nicht erforderlich"* (no consent required) — [datenschutz-schule.info, KI-Plattformen (NRW)](https://datenschutz-schule.info/tag/ki-plattformen/).

Two things follow. First, **AI tooling in classrooms is not inherently outside public task** — a state-level practice treats it as within the educational mission. Second, **the hook is a state school-law provision**, which only the school can invoke. A privately hosted instance has no §120 SchulG to point at until the school adopts it.

Austria works the same way: processing rests on statute, and consent is reserved for genuinely optional extras — *"Serviceleistungen auf Schülerwunsch (zum Beispiel Kopiersystem, Essensbestellung)"* ([BMB](https://www.bmb.gv.at/Themen/schule/schulrecht/ds.html)).

> **The condition on public task.** It covers the school's educational function as adopted by the school. It does **not** self-apply to a tool the school has not adopted, and #8's caveat still holds: it does not stretch to analytics, telemetry, product improvement, or secondary use.

### Consent — still invalid, and the change of controller doesn't rescue it

**#8's finding survives intact.** This is worth being precise about, because one might expect the imbalance argument to weaken once the controller is arguably not a public authority. It doesn't, for two reasons.

**Reason 1: Example 4's test is detriment, not public-authority status.**

> "**Example 4:** A public school asks students for consent to use their photographs in a printed student magazine. Consent in these situations would be a genuine choice as long as students will not be denied education or services and could refuse the use of these photographs without any detriment."

— [EDPB Guidelines 05/2020 on consent](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf), para 24

The operative condition is *"could refuse ... without any detriment"*. That test is controller-agnostic. A pupil who refuses a tool that delivers the lesson misses the lesson — detriment — whoever owns the server. The photograph example works precisely because a school magazine photo is severable from the education; coursework is not.

**Reason 2: the imbalance is compounded, not relieved.** The EDPB's imbalance analysis extends beyond public authorities to relationships of dependency, most explicitly employment:

> "An imbalance of power also occurs in the employment context. Given the dependency that results from the employer/employee relationship, it is unlikely that the data subject is able to deny his/her employer consent to data processing without experiencing the fear or real risk of detrimental effects as a result of a refusal."

— *ibid.*, para 24 (continuing)

The teacher–pupil relationship carries at least as much dependency as employer–employee: the teacher grades the child. Adding "and the teacher personally operates the system" makes the child's position *worse*, not freer. And per para 16, *"there are other lawful bases that are, in principle, more appropriate"*.

**So: if public task is gone AND consent is coerced, what is left? Nothing — and that is the finding.** The ticket anticipated this crux correctly. The absence of a valid basis is not a gap to paper over with a consent form; it is the signal that **the deployment shape is wrong**. The lawful configuration is not "teacher-hosted plus consent", it is "school-sanctioned under public task". See [Q6](#6-the-honest-risk-picture).

### Legitimate interests — the door does not reopen

The ticket asked whether Art 6(1)(f), closed to public authorities, becomes available to a private individual. **No**, on two independent grounds.

**Ground 1 — the carve-out follows the controller, and the controller is the school.** Art 6(1) final sentence: *"Point (f) of the first subparagraph shall not apply to processing carried out by public authorities in the performance of their tasks."* ([Art 6 GDPR](https://gdpr-info.eu/art-6-gdpr/)). Per [Q1](#1-who-is-the-controller) the controller is the school — a public authority performing its educational task. Art 6(1)(f) is therefore barred for the same reason #8 gave. The premise that "a private individual is not a public authority" is true but doesn't engage, because the private individual isn't the controller.

**Ground 2 — even on the teacher-as-controller branch, the balancing fails.** Art 6(1)(f) permits legitimate interests *"except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data, **in particular where the data subject is a child**"* (emphasis added — the caveat is in the Article text itself). Recital 38 reinforces that children *"merit specific protection"*.

Running the three-part test on these facts:

| Limb | Assessment |
|---|---|
| **Purpose** — is there a legitimate interest? | Weakly yes: educating pupils. But note the interest being asserted would be the *teacher's own*, and their legitimate interest in personally operating infrastructure (as opposed to the school's interest in educating) is thin. |
| **Necessity** — is processing necessary for it? | **Fails.** A school-sanctioned deployment achieves the identical educational purpose. Where a less intrusive route to the same end exists, the processing is not "necessary". |
| **Balancing** — do the child's rights override? | **Fails decisively.** 12-year-olds; academic performance data; reasonable expectations of pupils and parents that schoolwork stays within the school's governed estate, not a teacher's personal server and a US LLM provider; no transparency; no ability to object meaningfully; Art 6(1)(f)'s express child caveat; Recital 38. |

Legitimate interests is not available, and pursuing it would be a poor use of the project's time.

---

## 3. If consent is required: whose, and what must the schema hold?

**Consent is not required, and the recommendation is: do not build a consent table.** This is a concrete schema decision and I am stating it plainly because the ticket asked for one.

### Why the question dissolves

The ticket's framing — Art 8 ages are 16 (DE) / 14 (AT) / 13 (UK), all above 12, so parental consent would be needed for *every* pupil — is arithmetically correct but conditional on consent being the basis. It isn't:

- **Sanctioned deployment:** basis is public task. EDPB Guidelines 05/2020 para 127 confirms Art 8 applies *only* where *"The processing is related to the offer of information society services directly to a child"* **and** *"The processing is based on consent."* Neither limb is met. NRW states it directly for AI platforms: *"Eine Einwilligung ist hierfür nicht erforderlich."*
- **Unsanctioned deployment:** consent cannot cure it. Parental consent does not create the school's Art 28 DPA, does not supply the Art 6(3) legal hook, and is invalid anyway under Example 4's detriment test. A consent record here would be **evidence of a defective process**, not a defence.

### The schema recommendation

**No new table. Do not model consent as a first-class entity.**

Rationale:

1. **It would encode a legally wrong model.** The schema would assert consent-as-basis, which is wrong on both branches. Schemas are load-bearing documentation; a `parental_consent` table tells every future contributor that consent is how this system is lawful.
2. **It creates false assurance** — the most dangerous outcome. A green "consent captured" column invites the belief that the deployment is now lawful. It is not; the blocker is the DPA and the school's adoption, neither of which a parent can supply.
3. **It is the wrong party's artefact.** Where consent *is* genuinely needed at a school (photos, optional services), it is the **school's** record, held by the school, under its own retention rules — as BW's guidance shows, with ministry-supplied `Mustervorlagen` and paper/electronic declarations. It is out-of-band paperwork by design.
4. **Art 5(1)(c) minimisation cuts against it.** Consent records are themselves personal data about parents (names, signatures, timestamps) that the tool has no need to hold.

**What to build instead:** keep #8's recommendation — a single per-pupil ownership key across every record type, so export and erasure are practical. That serves the rights obligations that genuinely apply under public task.

**Where consent legitimately appears out-of-band**, the school holds it, on paper or in its own systems. Note BW's rule that consent is not a *Rechtsgeschäft*, so the parent's consent is required only where the pupil lacks *Einsichtsfähigkeit*, with a graduated scale — under 14 parents only; 14–16 both; from 16 the pupil usually exercises rights themselves ([BW FAQ 38](https://it.kultus-bw.de/site/pbs-bw-rebrush2024/get/documents_E1205840066/KULTUS.Dachmandant/KULTUS/Dienststellen/it.kultus-bw/Datenschutz%20an%20Schulen%20nach%20neuer%20EU%20DSGVO/dl-service/FAQ%20Datenschutz%20an%20Schulen%20EUDSGVO.pdf)). At 12, that is parents — but again, for the school's optional-extras processing, not for this tool's lawfulness.

> **The one scenario that would flip this:** if the tool were ever offered direct-to-consumer — pupils signing themselves up outside a school-mediated deployment — it becomes an information society service offered directly to a child, consent becomes the basis, and full Art 8 machinery engages. #8 flagged this; the teacher-provisioned roster (no self-registration, no email) is what keeps it shut. **Preserve that property.** It is now doing double duty: it keeps Art 8 out *and* it keeps the processing inside the school's realm of activities for para 19 purposes.

---

## 4. Does school sanction re-establish public task?

**Yes — and it is the only route that makes the deployment lawful.** Here is concretely what the teacher must obtain.

### The three artefacts, from primary guidance

Baden-Württemberg answers this question almost verbatim (FAQ 45, *"Dürfen Lehrkräfte alleine über den Einsatz von Software für den Unterricht entscheiden?"*):

> "Aus der Sicht des Datenschutzes: Ja, soweit damit keine personenbezogenen Daten verarbeitet werden. Grundsätzlich steht es Lehrkräften frei, Mittel und Methoden - auch Software - für ihren Unterricht bzw. ihre dienstliche Tätigkeit selbst zu wählen. **Werden durch die Software jedoch personenbezogene Daten verarbeitet, insbesondere online etwa durch Speicherung in einer Cloud, so bedarf dies immer der Genehmigung durch die Schulleitung sowie eines Auftragsverarbeitungsvertrags** ... Zusätzlich muss der von der Schule benannte Datenschutzbeauftragte einbezogen werden."

— [BW FAQ Datenschutz an Schulen](https://it.kultus-bw.de/site/pbs-bw-rebrush2024/get/documents_E1205840066/KULTUS.Dachmandant/KULTUS/Dienststellen/it.kultus-bw/Datenschutz%20an%20Schulen%20nach%20neuer%20EU%20DSGVO/dl-service/FAQ%20Datenschutz%20an%20Schulen%20EUDSGVO.pdf), FAQ 45 (emphasis added)

Note the boundary it draws: teachers *may* freely choose software that processes **no** personal data (the example given is generating worksheets). The moment pupil data is processed — and especially stored in a cloud — the three requirements bite. This project is unambiguously on the wrong side of that line.

**Minimum artefact list:**

1. **Written authorisation from the Schulleitung** (*Genehmigung*) — NRW requires a *"qualifizierte Genehmigung der Schulleitung"*, obtained **before** processing begins; Niedersachsen publishes an *Antrag auf Genehmigung* form for exactly this. This is the "written instruction from the head" the ticket asked about, and it is the realistic minimum entry ticket.
2. **An Art 28 DPA with the LLM provider, signed by the school** — not by the teacher. This is the hard blocker; see below.
3. **Involvement of the school's DPO** (*Datenschutzbeauftragter*) — mandatory per BW FAQ 45, and public bodies must designate one under Art 37(1)(a).

Realistically also: the DPIA ([Q5](#5-is-a-dpia-still-mandatory-and-who-must-do-it)); entry in the school's Art 30 record of processing activities; a privacy notice to parents/pupils; and in some Länder, checking the tool against a state-approved list (NRW steers toward LOGINEO NRW).

### The DPA is the hard blocker — a teacher cannot sign one

This is the finding that decides the ticket, and it deserves its own quotation (BW FAQ 44, *"Dürfen Lehrkräfte Verträge zur Auftragsverarbeitung abschließen?"*):

> "**Nein!** Werden im Zuge der dienstlichen Tätigkeit personenbezogene Daten von einem externen (Software-)Anbieter verarbeitet, so handelt es sich regelmäßig um eine Auftragsverarbeitung. Die Datenverarbeitung ist nur zulässig, wenn zuvor ein entsprechender Auftragsverarbeitungsvertrag nach den Vorgaben des Art. 28 EU-DSGVO abgeschlossen wurde. **Zuständig hierfür ist ausschließlich die Schulleitung** als für den Datenschutz verantwortliche Stelle im Sinne der DSGVO (Art. 4 Nr. 7 EU-DSGVO). **Ein solcher Vertrag, der durch eine Lehrkraft abgeschlossen wurde, ist ungültig. Die Datenübermittlung an den Anbieter ist damit unzulässig und stellt ggf. einen meldepflichtigen Datenschutzverstoß dar.**"
>
> "Manche Softwareanbieter eröffnen Lehrkräften die Möglichkeit einen Auftragsverarbeitungsvertrag direkt abzuschließen oder fordern die jeweiligen Nutzer ohne Prüfung von deren Befugnis sogar aktiv dazu auf. **In diesen Fällen darf der Vorgang nicht abgeschlossen werden!** Die Lehrkraft muss vielmehr den Vertrag der Schulleitung vorlegen. **Die Software darf bis zum Vertragsabschluss nicht genutzt werden.**"

— *ibid.*, FAQ 44 (emphasis added)

Read against this project's architecture, that paragraph is close to dispositive:

- Every LLM provider is an **Auftragsverarbeiter** (processor) the moment a prompt containing pupil data leaves the instance. #8 established this — self-hosting protects the database but not the provider hop.
- Clicking "I accept" on Anthropic's or OpenAI's terms as an individual **is** a teacher concluding a DPA. BW says such a contract is `ungültig`.
- Consequence: transmission to the provider is `unzulässig` and may itself be a **notifiable breach**.
- BW even anticipates the exact failure mode here: providers that let individual users accept DPAs *"ohne Prüfung von deren Befugnis"* — precisely how Anthropic's auto-incorporated DPA (#8, Q3) works. The convenience that #8 flagged as a procurement *advantage* becomes a trap for an individual teacher.

**And the standing instruction is explicit: the software may not be used until the contract is concluded.**

### Does sanction restore public task in practice?

Yes. Once the school adopts the tool, the school is knowingly the controller, the Art 6(3) hook is its own school law (§§120/121 SchulG NRW or equivalent, or the Austrian Schulgesetze/BilDokG framework), the DPA is validly signed, the DPO is engaged, and the DPIA is the school's. That is a coherent, defensible configuration — and it is materially the configuration #8 assumed.

> **Open question — unresolved.** Whether a school would *in fact* approve a teacher-built, teacher-hosted tool sending pupil data to a US LLM provider. Approval is legally necessary but not automatic; several German state DPAs have published critical positions on US cloud services in schools (#8 flagged this and it remains unverified for the relevant state). The school may well require hosting on its own estate or a Land-approved platform — which would change the deployment architecture again.

---

## 5. Is a DPIA still mandatory, and who must do it?

**Still mandatory. And the controller answer changes who must do it — it is the school's obligation, not the teacher's.**

Art 35(1) is explicit that the duty sits on the controller:

> "Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, **the controller** shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data."

— [Art 35 GDPR](https://gdpr-info.eu/art-35-gdpr/) (emphasis added)

Since the school is the controller ([Q1](#1-who-is-the-controller)), the school must carry out the DPIA, with its DPO's advice (Art 35(2)). A DPIA written by the teacher alone is not the controller discharging its obligation — it is useful input, not compliance. **This is a third artefact the teacher cannot validly produce alone**, alongside the DPA and the Genehmigung. Note also *"prior to the processing"*: a DPIA after launch is already late.

The substantive high-risk analysis from #8 is unchanged and I re-checked its anchors rather than re-deriving them:

- **EDPB/WP248 two-criteria threshold** met comfortably: vulnerable data subjects (children) + innovative technology (LLM). Add evaluation/scoring if quiz results assess pupils.
- **Austria** — the DSFA-V explanatory notes treat under-14s as *schutzbedürftige Betroffene*, and the BilDokG DPIA itself records that pupil data engages *"Daten zu schutzbedürftigen Betroffenen, worunter insbesondere Kinder zu verstehen sind"* ([BMBWF DSFA](https://www.bmb.gv.at/dam/jcr:48645b5d-c90e-4dd8-8216-6b8b370d6bfd/dsfa_bil_dok_g_2020.pdf)). Notably, Austria conducted a full DPIA for *school-local pupil records* — a far less risky processing than LLM-mediated coursework.
- **Germany** — DSK Muss-Liste is non-exhaustive; obligation arises from Art 35(1) + WP248 criteria.

One genuine nuance worth flagging: **Art 35(10)** can disapply the DPIA duty where processing rests on Art 6(1)(c)/(e) with a Member State legal basis and a DPIA *"has already been carried out as part of a general impact assessment in the context of the adoption of that legal basis"*. Austria's BilDokG DPIA is exactly such a general assessment. **But it does not cover this tool** — it assesses statutory pupil-record processing, not LLM-mediated learning tools, and it predates them. Art 35(10) is not an escape here, and the school should not be told it is.

---

## 6. The honest risk picture

The ticket asked for this straight, unsoftened. Here it is.

### The good news, such as it is

**The teacher is probably not the controller**, so the headline fear — "I personally carry full controller liability" — is likely overstated as a matter of GDPR role allocation. Under EDPB para 19 the school is presumed controller for processing within its realm of activities, and Länder guidance says so explicitly even for private IT. In Austria the statute fixes it on the principal.

There is also a public-sector shield in some jurisdictions: BW notes that in the external relationship *"haftet grundsätzlich der Dienstherr für eine schuldhafte Pflichtverletzung bei öffentlich-rechtlichem Handeln des Beamten"*, with recourse against the official only for *"vorsätzlichem oder grob fahrlässigem Handeln"*; and Art 83(7)/§28 LDSG mean administrative fines generally do not run against public bodies in BW.

### The bad news, which is worse

**None of that makes the deployment lawful, and the teacher's exposure is real.**

1. **The processing is unlawful from the first prompt.** Not "risky" — unlawful. There is no valid Art 28 DPA (only the Schulleitung can sign; a teacher's is `ungültig`), so transmission to the LLM provider is `unzulässig` and *"stellt ggf. einen meldepflichtigen Datenschutzverstoß dar"*. That is a breach that exists on day one, independent of anything going wrong.
2. **The shield protects the *Dienstherr*, and it has holes exactly where this sits.** Recourse against the official survives for **gross negligence**. Deploying an unapproved cloud-connected tool processing children's data to a US LLM provider, without the head's authorisation, without a DPA, and without involving the DPO — after state guidance says in terms that the software *"darf bis zum Vertragsabschluss nicht genutzt werden"* — is a strong candidate for gross negligence. The shield is weakest precisely in this scenario.
3. **Employment/disciplinary consequences are separate from GDPR and not shielded at all.** Processing outside the head's authorisation is a *Dienstpflichtverletzung*. The BW guidance contemplates inspection of a teacher's private device *"um einen Missbrauch bzw. eine Dienstpflichtverletzung aufzuklären"*. This risk is borne personally and is arguably the most likely one to actually materialise.
4. **Personal criminal/penalty exposure exists in the UK path.** A former headteacher was prosecuted and fined for unlawfully obtaining pupil data from previous schools and putting it on another school's server — data he said he took *"for professional purposes"* ([The Register](https://www.theregister.com/2018/12/05/ico_fines_former_headteacher_for_pupil_data_dump/); [Harrison Clark Rickerbys](https://www.hcrlaw.com/blog/former-headteacher-fined-for-breach-of-data-protection-legislation/)). Good professional motives were no defence. *(Secondary sources; prosecuted under s55 DPA 1998, the predecessor to s170 DPA 2018 — see confidence note.)*
5. **The teacher has the exposure without the authority to cure it.** They cannot sign the DPA, cannot supply the Art 6(3) hook, and cannot validly perform the DPIA. Every instrument that would make this lawful requires the Schulleitung.
6. **Third-party consequences land on children.** If it goes wrong, the harmed parties are 12-year-olds whose coursework, misunderstandings and performance sit on an ungoverned server and in a US provider's logs, with no notice to parents and no route to exercise rights.

### The recommendation, stated plainly

**This deployment shape is not defensible and must change. The correct engineering answer is that the tool must be school-sanctioned before it can lawfully run.**

Concretely:

- **Do not run it on a real class of other people's children until the Schulleitung has authorised it in writing, the school has signed the Art 28 DPA with the provider, and the school's DPO has been involved.** That is not a hardening backlog item; it is the precondition for lawful operation.
- **Until then, the lawful development paths are:** synthetic/fictional pupil data; the teacher's own data; a local model with no pupil data leaving the machine; or a genuinely anonymous mode with no per-pupil attribution (though #8 correctly notes per-pupil progress tracking makes real anonymity impossible by construction).
- **Reframe the product's target from "a teacher" to "a school."** This is a real product consequence: onboarding must have a school-adoption step (head's authorisation, DPA, DPO sign-off) rather than a teacher signing up alone. Any design that lets an individual teacher self-serve a class of real pupils is designing the unlawful configuration into the product.
- **Do not let the provider's frictionless DPA acceptance reassure you.** BW warns specifically about providers that let unauthorised users accept DPAs — Anthropic's auto-incorporated DPA is convenient for an organisation and a trap for an individual teacher.

**If a single sentence goes into the map: the blocker is not the schema, it is the deployment shape — and no consent flow, table, or field can fix it.**

---

## Corrections to #8

Explicitly, since #8's lawful-basis finding was presumed void pending this ticket.

### Survives — reinstated, with a corrected rationale

- **Public task (Art 6(1)(e)) is the lawful basis.** ✅ Survives. #8's *conclusion* was right; its *reasoning* was incomplete. #8 assumed the school is controller as a fact about deployment. The stronger position is that the school is controller **as a matter of law and EDPB presumption, even when a teacher self-hosts**. The basis is therefore more robust than #8 realised — but it is the school's, and it requires the school to actually adopt the tool.
- **No parental-consent flow in the schema.** ✅ Survives, and is now **doubly** supported: consent isn't the basis on the sanctioned branch, and consent can't cure the unsanctioned branch. See [Q3](#3-if-consent-is-required-whose-and-what-must-the-schema-hold).
- **Article 8 does not engage.** ✅ Survives. EDPB para 127's two conditions still both fail. NRW states directly that no consent is required for classroom AI platforms.
- **Consent would be invalid in a classroom.** ✅ Survives — and importantly, survives *the change of controller*, because Example 4's test is detriment, not public-authority status.
- **Legitimate interests is unavailable.** ✅ Survives, with an additional independent ground (the child caveat in Art 6(1)(f) plus a failed balancing test) that holds even on the teacher-as-controller branch.
- **Art 8 ages: DE 16, AT 14, UK 13.** ✅ Survives. Austrian §4(4) DSG re-verified this session.
- **A DPIA is effectively mandatory.** ✅ Survives — with the addition that Art 35(1) puts it on the **school**, and that Art 35(10) does not exempt it.
- **Provider terms findings (Gemini blocked, OpenAI needs ZDR, Anthropic most permissive).** ✅ Survives — not re-derived, per the brief. One correction of emphasis: #8 called Anthropic's auto-incorporated DPA "a genuine procurement advantage". Under this ticket's facts that is **inverted for an individual teacher** — it is the exact mechanism BW warns about, where a provider lets someone without authority conclude a DPA. It remains an advantage *for a school*.
- **"Display name is personal data".** ✅ Survives, unchanged and uncontested. Brief re-check only, per the brief.
- **Per-pupil ownership key is the key schema consequence.** ✅ Survives and is now the *only* schema consequence from this line of research.

### Overturned

- **#8: "Open question — whether the school or the developer is the controller ... a factual question about the deployment."** ❌ **Overturned as framed.** It is not purely factual, and the framing offered a false binary. Controllership is a legal characterisation that does not follow the infrastructure. A teacher self-hosting does **not** thereby become the controller; the school remains controller by presumption (EDPB para 19), by national guidance, and in Austria by statute. The developer-as-controller branch #8 worried about does not arise on these facts.
- **The ticket's premise that "the teacher-operator is now, on the face of it, the controller."** ❌ **Overturned.** This was the ticket's working assumption and the sources contradict it. The consequence is not that the risk disappears — it relocates and, for the teacher, largely persists via the gross-negligence carve-out and disciplinary exposure.
- **#8's implicit assumption that the school-as-controller path is a deployment *choice*.** ❌ Overturned. Where a teacher deploys for their own class, school controllership is not opted into; it is presumed. The choice is only whether the school's controllership is *compliant*.

### Now conditional

- **Public task is conditional on school adoption.** The basis exists but is not self-executing. Without the school's Genehmigung, DPA, and DPO involvement, there is no valid Art 6(3) hook the deployment can point to and the processing is unlawful notwithstanding that public task is theoretically the right basis.
- **#8's compliance checklist assumes a sanctioned deployment throughout.** Items 16–23 (DPIA, DPAs, privacy notice, retention policy, SAR procedure, breach procedure, Art 30 record) are all **controller** obligations — the school's. On the current deployment shape they have no valid author. They are not wrong; they are unperformable by the teacher alone.
- **#8's "the ICO Children's Code probably does not bind this project."** Conditional and unchanged. It rested on the school-deployment/not-direct-to-consumer path, which this ticket reinforces — but the UK path is secondary and the Code was not re-examined.

---

## Confidence and gaps

**High confidence — verified against primary sources this session:**

- EDPB Guidelines 07/2020 paras 17, 19 (+ fn 9), 20, 52–55, 150 — direct quotations from the PDF, extracted and read locally.
- Art 29, Art 26, Art 6(1) (incl. the (f) public-authority bar and the child caveat), Art 6(3), Art 35(1)/(3)/(10), Art 2(2)(c), Recital 18 — direct quotations.
- EDPB Guidelines 05/2020 paras 16, 24 (Example 4 + the employment-imbalance passage), 125, 127 — extracted from the PDF and read locally.
- Austria: § 4 Abs 1 Z 1 BilDokG 2020 designates school principals as controllers — quoted from the BMBWF's own DPIA document, corroborated by the ministry's public page.
- Germany: school/Schulleitung remains controller for pupil data on teachers' **private** IT — independently stated by Niedersachsen, NRW and Baden-Württemberg.
- Germany (BW): teachers may not conclude Art 28 DPAs; such a contract is `ungültig`; transmission is `unzulässig` and possibly notifiable; software must not be used until the contract is concluded; teacher-chosen software processing personal data always requires Schulleitung approval + DPA + DPO involvement. Direct quotations, FAQ 44 and 45.
- Austria: § 4(4) DSG digital-consent age of 14 (re-verified; same JUSLINE caveat as #8 — RIS remains the authoritative source).

**Medium confidence — well-supported but with a sourcing caveat:**

- ***Ryneš* C-212/13 wording.** EUR-Lex and InfoCuria returned bot-challenge responses (HTTP 202/403) on repeated attempts. The "narrowly construed" and "directed outwards" language is quoted from search-result extracts, not a full-text read of the official report. The propositions are stable and widely reported. **Not load-bearing** — the household exemption is dismissed on Recital 18's verified text and the facts alone.
- **NRW's §§ 120(1)/121(1) SchulG NRW + Art 6(1)(e) as the basis for classroom AI platforms.** From a specialist practitioner site (datenschutz-schule.info), not the Schulministerium directly. The *pattern* (state school law + public task, no consent) is corroborated by Austria's statutory approach and general Länder guidance. **Verify the specific provisions against SchulG NRW if NRW turns out to be the jurisdiction.**
- **UK headteacher prosecution.** Secondary sources (The Register, HCR, Tes); under s55 DPA 1998, the predecessor to s170 DPA 2018. Illustrative of personal exposure, not a controllership authority. Do not cite it as a controller-identity precedent.
- **The joint-controllership analysis of the "school tolerates but doesn't adopt" middle case.** My application of EDPB paras 52–55 to hypothetical facts, not a regulator's finding on this scenario. Flagged as *conceivable*, not established.

**Explicitly NOT verified — do not rely on these:**

- **Which jurisdiction, and if Germany which Bundesland.** Carried over unresolved from #8. The controller conclusion converges across all candidates, but the *statutory hook* for public task, the applicable DPA, any state-approved-tools regime, and the authorisation form are all state-specific.
- **Whether any state DPA has published a position on US LLM providers in schools.** Flagged as potentially decisive in #8, still unchecked, and it could independently block the provider choice even in a fully sanctioned deployment.
- **Whether a school would in fact approve this tool** — legally necessary, practically uncertain.
- **Whether Anthropic/OpenAI will contract with a *school* as counterparty**, and on what terms. #8 established the terms; who may sign them for a school is unexamined.
- **The Austrian position on teachers' private IT specifically.** Austria's controller rule is statutory and clear, but I did not find an Austrian equivalent of the German Länder guidance on private-device processing. The BMB page mentions private cloud services in IT-supported teaching under conditions I did not fully retrieve.
- **UK-specific guidance on teacher shadow IT.** The UK path was treated as secondary; ICO pages continued to return HTTP 403 to direct fetches, as in #8.
- **Whether the school's own insurance/indemnity would cover a teacher-hosted instance.** Not researched; relevant to the personal-risk picture.

---

## Sources

All accessed **2026-07-29**. Marked **[P]** primary (legislation, regulator, ministry, or court), **[S]** secondary.

### GDPR text

- **[P]** Art 2 GDPR — material scope, incl. 2(2)(c) household exemption — https://gdpr-info.eu/art-2-gdpr/
- **[P]** Recital 18 GDPR — "no connection to a professional or commercial activity" — https://gdpr-info.eu/recitals/no-18/
- **[P]** Art 6 GDPR — lawful bases; (f) public-authority bar; "in particular where the data subject is a child" — https://gdpr-info.eu/art-6-gdpr/
- **[P]** Art 26 GDPR — joint controllers, incl. 26(3) — https://gdpr-info.eu/art-26-gdpr/
- **[P]** Art 29 GDPR — processing under the authority of the controller — https://gdpr-info.eu/art-29-gdpr/
- **[P]** Art 35 GDPR — DPIA; 35(1) controller duty; 35(10) — https://gdpr-info.eu/art-35-gdpr/

### EDPB

- **[P]** **Guidelines 07/2020 on the concepts of controller and processor in the GDPR** (final, after public consultation) — https://www.edpb.europa.eu/system/files/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf — *paras 17–20 (controller, employees, Art 29), 50–55 (joint controllership), 150 (processor determining purposes → controller)*
- **[P]** Guidelines 05/2020 on consent under Regulation 2016/679, v1.1 — https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf — *paras 16 (imbalance/public authority), 24 (Example 4 + employment imbalance), 125–127 (Art 8 conditions)*

### CJEU

- **[P/S]** C-212/13 *František Ryneš v Úřad pro ochranu osobních údajů*, ECLI:EU:C:2014:2428 — https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:62013CJ0212_SUM — *narrow construction of the household exemption; "directed outwards". Direct fetch blocked (HTTP 202/403); quoted from search-result extracts — see confidence note.*
- **[P]** C-210/16 *Wirtschaftsakademie*, C-25/17 *Jehovan todistajat*, C-40/17 *Fashion ID* — cited within EDPB Guidelines 07/2020 fn 18 as the joint-controllership line of authority.

### Austria

- **[P]** BMBWF, *Datenschutz-Folgenabschätzungen zum Bildungsdokumentationsgesetz 2020* — https://www.bmb.gv.at/dam/jcr:48645b5d-c90e-4dd8-8216-6b8b370d6bfd/dsfa_bil_dok_g_2020.pdf — *§ 4 Abs 1 Z 1 BilDokG 2020: principals are controllers; children as schutzbedürftige Betroffene; DSFA-V analysis*
- **[P]** BMB, *Datenschutz in Schulen* — https://www.bmb.gv.at/Themen/schule/schulrecht/ds.html — *principal as controller; statutory basis; consent limited to optional services*
- **[S]** Austrian DSG § 4 (Art 2 § 4), via JUSLINE — https://www.jusline.at/gesetz/dsg/paragraf/artikel2zu4 — *§4(4): consent age 14. Republisher; RIS is authoritative.*

### Germany

- **[P]** Kultusministerium Baden-Württemberg, *FAQ Datenschutz an Schulen*, Stand 05/2024 — https://it.kultus-bw.de/site/pbs-bw-rebrush2024/get/documents_E1205840066/KULTUS.Dachmandant/KULTUS/Dienststellen/it.kultus-bw/Datenschutz%20an%20Schulen%20nach%20neuer%20EU%20DSGVO/dl-service/FAQ%20Datenschutz%20an%20Schulen%20EUDSGVO.pdf — *FAQ 37 (private devices), 38 (consent age scale), 44 (teacher DPAs invalid), 45 (software choice), 20 (liability/Regress), 6 (cloud)*
- **[P]** LfD Niedersachsen / NiBiS, *Verarbeitung personenbezogener Daten auf privaten IT-Systemen von Lehrkräften* (Stand 2023-02-23) — https://datenschutz.nibis.de/2020/02/24/verarbeitung-personenbezogener-daten-auf-privaten-informationstechnischen-systemen-it-systemen-von-lehrkraeften/ — *school as controller; Genehmigung form; RdErl. d. MK v. 01.01.2020; § 31 NSchG*
- **[P]** Medienberatung NRW, *Dienstliche Verarbeitung personenbezogener Daten auf privaten Endgeräten* — https://www.medienberatung.schulministerium.nrw.de/de/themen/datenschutz_1/anwendung/fragen_zur_dienstlichen_verarbeitung_personenbezogener_daten_auf_privaten_endgeraeten.html — *Schulleitung as verantwortliche Stelle; qualifizierte Genehmigung*
- **[P]** Bayerischer Landesbeauftragter für den Datenschutz, *FAQ Schulen* — https://www.datenschutz-bayern.de/datenschutzreform2018/FAQ_Schulen.pdf — *school as responsible entity (corroborating)*
- **[S]** datenschutz-schule.info, *KI-Plattformen* (NRW focus) — https://datenschutz-schule.info/tag/ki-plattformen/ — *§§ 120(1), 121(1) SchulG NRW + Art 6(1)(e); "Eine Einwilligung ist hierfür nicht erforderlich"*

### UK (secondary comparison)

- **[S]** The Register, *Former headteacher fined £700 after dumping old pupil data on server at new school* — https://www.theregister.com/2018/12/05/ico_fines_former_headteacher_for_pupil_data_dump/
- **[S]** Harrison Clark Rickerbys, *Former headteacher fined for breach of data protection legislation* — https://www.hcrlaw.com/blog/former-headteacher-fined-for-breach-of-data-protection-legislation/

### Prior research in this repo

- `docs/research/data-protection-for-minors.md` — issue #8 findings (provider terms, DPIA, personal-data analysis retained; lawful-basis section corrected by this document)
