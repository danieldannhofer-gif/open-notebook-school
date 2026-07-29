# Which commercial LLM processors will DE/AT state authorities accept for schools?

Research for [issue #18](https://github.com/danieldannhofer-gif/open-notebook-school/issues/18). All sources accessed **2026-07-30**.

> **Scope note.** This is engineering research against primary sources, not legal advice. It answers the question [#14](https://github.com/danieldannhofer-gif/open-notebook-school/issues/14) left unverified: whether its **Mistral** recommendation survives contact with actual authority positions, and whether guidance should name vendors or describe categories.

---

## Answer

**Mistral does not survive as the recommendation, and the reason is not the one anyone was looking for.** The transfer analysis in #14 was correct — Mistral is EU-established, so there is no Chapter V problem. But nobody had read Mistral's commercial terms. Clause 2.2(c) prohibits the customer from including "*any personal information of children under 13 or the applicable age of digital consent as Customer Data*" and from allowing "*minors to use the Mistral AI Products without legally adequate consent from their parent or guardian*". A class of 12-year-olds fails **both limbs**, and the second is unfixable: [#11](https://github.com/danieldannhofer-gif/open-notebook-school/issues/11) established that consent in a classroom is invalid for want of freely-given choice, so the consent the clause demands is precisely the thing this project cannot lawfully obtain. Mistral publishes **no minors-serving programme** of the kind OpenAI and Anthropic both have — no under-18 guidance, no exception route, no ZDR-conditioned carve-out. Unlike OpenAI's ZDR (a negotiation with a known counterparty and a known ask), there is nothing to negotiate *toward*. See [Q3](#3-mistral-specifically).

**The answer is categorical, not provider-specific — with exactly one named exception, and that exception is the actual answer to the ticket.** No German or Austrian authority publishes an approved-provider list. The DSK's AI guidance names **zero** vendors across 15 pages; Hessen's HBDI guidance on non-EU AI providers names zero; the Austrian DSB names zero. They reason in categories: EU-established vs third-country, processor-relationship-with-a-DPA vs not, training-excluded vs not, pseudonymised vs identifiable. **But** LDI NRW's 31st activity report (2026) does something no other document does — it names, and welcomes, a specific offering. See [Q1](#1-do-authorities-name-providers-or-categories).

**The thing authorities actually accept is not a provider — it is a state-brokered intermediary, and all 16 Länder have built one.** `AIS.chat` (until 19 May 2026: `telli`), built by the **FWU** — the Länder's own media institute — on behalf of all 16 German states. The school is controller, FWU is the Art 28 processor, and the model vendors (OpenAI, Meta, **Mistral**, Google) are FWU's *sub*-processors, all EU-hosted. LDI NRW says in terms that it *welcomes* the project, and gives the reason that decides this ticket: individual schools are "*häufig überfordert*" — frequently overwhelmed — by implementing the required technical and organisational measures themselves. The supervisory authority's own diagnosis is that **a single school is not a viable counterparty for this class of processing**, and the remedy the Länder built is to put a state body in the middle. See [Q2](#2-what-authorities-actually-accept).

**Mistral *is* accepted for schools — but only as FWU's sub-processor, never as a school's direct counterparty.** This is the sharpest finding in the document. #14 reasoned toward the right vendor by the wrong route and drew the wrong conclusion about the *contracting shape*. Mistral appears in the state-sanctioned stack (`Mistral Nemo Instruct` in AIS.chat's model picker; current Mistral models in Baden-Württemberg's **F13** on state-controlled BITBW hardware) precisely because a state body absorbed the Art 28 relationship and the minors problem. A Gymnasium pointing an endpoint at `api.mistral.ai` is in a **different legal position** from the same Gymnasium using AIS.chat, even when the same Mistral weights answer the prompt. See [Q3](#3-mistral-specifically).

**Nobody has to answer "will Mistral contract with one Gymnasium?", because the correct answer is that a Gymnasium should not try.** Mistral's DPA is genuinely self-serve — auto-incorporated by reference, no signature step, no sales gate — so mechanically a school *could* get one. That is a trap of the exact kind Baden-Württemberg FAQ 44 warns about (providers letting people without authority accept DPAs), and it does not cure clause 2.2(c) anyway. The DPA a school can actually obtain is **FWU's**, and every Land provides it free. See [Q4](#4-will-providers-contract-with-a-single-school) and [Q5](#5-musterverträge-and-framework-agreements).

**Austria is the gap, and it is a real one.** Austria has a school Muster-AVV template (BMB) and a DSB that names no providers, but **no state-brokered AI tool** — no AIS.chat equivalent, no framework licence, no approved list. An Austrian Gymnasium is left exactly where the German ones were before the Länder built FWU: needing an Art 28 DPA it must source itself, from a vendor pool whose terms mostly exclude 12-year-olds. See [Q6](#6-austria).

### The one-sentence version for the map

The product's guidance should not name a vendor at all: it should tell a German school to point the endpoint slot at **its Land's AIS.chat / state AI offering**, tell an Austrian school that **no equivalent exists and the DPA problem is therefore unresolved**, and drop Mistral-the-direct-vendor entirely on its own terms of service — not on transfer grounds.

---

## Jurisdiction

Still formally unconfirmed on the map (flagged since #8, again in #11). **Unlike #11, it now matters, and it changes the answer.**

| | Germany | Austria |
|---|---|---|
| State-brokered AI tool for schools | **Yes** — `AIS.chat` (ex-`telli`), all 16 Länder, free | **No equivalent found** |
| Who is the school's Art 28 counterparty | **FWU** (Länder's own media institute) | The school must find one itself |
| Model vendors' role | FWU's sub-processors | n/a |
| Authority names providers? | No — except LDI NRW *welcoming* telli | No |
| Muster-AVV for schools from the state | Yes (Bayern, Sachsen-Anhalt templates) | Yes (BMB "Vorlage Auftragsverarbeitervereinbarung (AVV) Schulen") |
| Approved-provider list | None published | None published |
| Practical status for a single Gymnasium | **Solved** — use the Land offering | **Unsolved** |

> **This flips the jurisdiction question from cosmetic to load-bearing.** #11 concluded the controller analysis converged across candidates so the open jurisdiction question did not bite. Here it does: the same product, in Germany, has a documented lawful path a Schulleitung can walk in an afternoon; in Austria it does not. Guidance that does not distinguish them is wrong for one of the two audiences.

> **Germany — Bundesland dependency persists but narrows.** Every Land offers AIS.chat, but the *model list varies by Land* — AIS.chat's own FAQ says "*Stand und Verfügbarkeit kann je Bundesland variieren*" — and some Länder run additional or alternative tools (BW's **F13**, Bayern's **ByLKI** and ByCS AI, Rheinland-Pfalz and Mecklenburg-Vorpommern licensing **fobizz**). The *shape* is uniform; the menu is not.

**UK**: fell out cheaply only as a negative — no comparable state-brokered offering was found, and the UK path was not researched. Do not infer anything.

---

## 1. Do authorities name providers, or categories?

**Categories. Overwhelmingly and deliberately.** This disposes of the ticket's question about how #14's guidance should be written.

### The DSK names no vendor at all

The Datenschutzkonferenz — all German federal and state DPAs jointly — published *Orientierungshilfe Künstliche Intelligenz und Datenschutz* on 6 May 2024. I extracted the full 15-page text and searched it. **`OpenAI`, `ChatGPT`, `Mistral`, `Anthropic` appear zero times.** The guidance is structured entirely around controller duties and system properties.

Its operative passage on the processor relationship:

> "Setzt eine Stelle zu eigenen Zwecken eine KI-Anwendung eines externen Anbieters zum Beispiel als Cloud-Lösung ein, agiert der externe Anbieter als verlängerter Arm im Auftrag des Verantwortlichen. Dann besteht zwischen dem Anbieter der Anwendung und dem Verantwortlichen häufig ein Auftragsverarbeitungsverhältnis gemäß Art. 28 f. DS-GVO mit der Folge, dass mit dem Anbieter eine Vereinbarung gemäß Art. 28 Abs. 3 DS-GVO abzuschließen ist."

— [DSK, *Orientierungshilfe KI und Datenschutz*](https://www.datenschutz.rlp.de/fileadmin/datenschutz/Dokumente/Orientierungshilfen/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz_web.pdf), §2.1

And its by-default configuration requirement, which is the categorical version of "ZDR":

> "können für Accounts, die Beschäftigte nutzen sollen, die Funktionen zur Nutzung von Eingaben für das KI-Training und zur Eingabe-Historie bereits bei Inbetriebnahme eines Accounts so gewählt werden, dass keine Eingabedaten zu Trainingszwecken verarbeitet werden und keine Eingabe-Historie über die Sitzung hinaus gespeichert wird."

— *ibid.*, §2.5

Note this is **exactly** what AIS.chat implements (no training, session-scoped chat deletion). The state tool is built to the DSK's own specification.

The guide also states a categorical architectural preference relevant to the conduit:

> "Technisch geschlossene Systeme sind daher aus datenschutzrechtlicher Sicht vorzugswürdig."

— *ibid.*, §1.7

### Hessen (HBDI) reasons purely by establishment, not identity

The HBDI's dedicated page is titled *Empfehlungen zum Einsatz von KI-Anwendungen von Anbietern **außerhalb der EU*** — the category is in the title. Its five recommendations turn on transparency, documentation, Art 45 adequacy, Art 27 representatives, and never on vendor identity. Two are directly operative here:

> "Achten Sie bei der Auswahl einer KI-Anwendung auf Transparenz des Anbieters und eine entsprechende Dokumentation..."

> "Wenn Sie eine Online-Schnittstelle verwenden, sollten Sie niemals personenbezogene oder vertrauliche Daten eingeben..."

— [HBDI, *Empfehlungen zum Einsatz von KI-Anwendungen von Anbietern außerhalb der EU*](https://datenschutz.hessen.de/datenschutz/kuenstliche-intelligenz/empfehlungen-zum-einsatz-von-ki-anwendungen-von-anbietern-ausserhalb-der-eu)

**No providers named.** The threshold is Art 45 adequacy — a category.

### Austria's DSB likewise

The DSB's AI pages restate GDPR principles running parallel to the AI Act and name **no commercial vendors**. Notably it takes the position that a body deploying a third-party AI system is typically the **controller** — consistent with #11 and with AIS.chat's own construction.

— [DSB, *Künstliche Intelligenz & Datenschutz*](https://dsb.gv.at/kuenstlichebrintelligenz/kuenstliche-intelligenz-datenschutz)

### The one exception, and it is not a permission

LDI NRW's 31st activity report **does** name commercial products — but as the *problem*, not the permission:

> "Bei unmittelbarer Nutzung frei zugänglicher LLMs wie GPT-4 oder Gemini erhält der*die Anbieter*in allerdings Kenntnis von den bei der Nutzung anfallenden Daten. Und das bringt datenschutzrechtliche Probleme mit sich."

— [LDI NRW, *31. Bericht* (2026)](https://www.ldi.nrw.de/system/files/media/document/file/31_bericht_2026.pdf), §6.1

Its three required measures are stated as categories, not names:

> "Hierzu zählen insbesondere, zuverlässige Anbieter*innen auszuwählen, so wenig personenbezogene Daten wie möglich einzugeben und die Verarbeitung personenbezogener Daten zu eigenen Zwecken der Anbieter*innen auszuschließen."

— *ibid.*

**Consequence for #14's guidance: write it in categories.** The criteria authorities actually apply are (a) EU establishment or Art 45 adequacy, (b) a real Art 28 DPA, (c) training and own-purpose processing contractually excluded, (d) no identifiable user reaching the vendor, (e) session-scoped retention, (f) a DPIA. A vendor name is never the test — with the single, decisive exception in Q2.

### What LDI NRW supplies that #11 flagged as unverified

#11 listed "NRW's §§ 120(1)/121(1) SchulG NRW + Art 6(1)(e) as the basis for classroom AI platforms" as **medium confidence**, sourced from a practitioner site rather than the authority. **Now upgraded to high confidence from the supervisory authority itself** — and slightly corrected:

> "Soweit dennoch personenbezogene Daten verarbeitet werden, bieten § 120 Abs. 5 bzw. § 121 Abs. 1 Satz 1 und 2 SchulG (Einsatz von Lehr- und Lernsystemen) einstweilen eine mögliche Rechtsgrundlage."

— *ibid.*

Note the differences from #11's secondary source: **§ 120 Abs. 5** (not Abs. 1), and the hedged "*einstweilen eine mögliche Rechtsgrundlage*" — provisionally *a possible* legal basis. The authority is markedly less confident than the practitioner site was. It goes further:

> "Die beim Einsatz von KI-Technologien durchzuführende Datenschutz-Folgenabschätzung (Art. 35 DS-GVO) kann möglicherweise jedoch auch zu dem Ergebnis führen, dass einzelne Aspekte der KI-Nutzung einer speziellen rechtlichen Regelung bedürfen."

— *ibid.*

So NRW's own regulator thinks the statutory basis for classroom LLM use may be **insufficient** and may need purpose-built legislation. That is weaker than #8 or #11 assumed. It also independently re-confirms the DPIA as mandatory (#8, #11), from a supervisory authority, for this exact processing.

---

## 2. What authorities actually accept

**A state-brokered intermediary — `AIS.chat`, formerly `telli`.** This is the answer to the ticket.

### What it is

Built by the **FWU – Institut für Film und Bild in Wissenschaft und Unterricht gGmbH** (Grünwald, Bavaria), the Länder's own media institute, under the cross-state Digitalpakt project **AIS** (Adaptives Intelligentes System), on behalf of **all 16 Bundesländer**. Renamed from `telli` to `AIS.chat` on 20 May 2026 for trademark reasons. Open source at [github.com/FWU-DE/telli-dialog](https://github.com/FWU-DE/telli-dialog).

Rollout is complete and free: NRW from 5 December 2025 for all public and Ersatzschulen; Bayern from 15 December 2025; Baden-Württemberg from 13 October 2025 via SCHULE@BW; Hessen from 1 October 2025 via Schulportal Hessen; Saarland, Schleswig-Holstein, Berlin-Brandenburg and others alongside.

### The legal construction — it matches #11 exactly

AIS.chat's privacy notice states the controller/processor split in one sentence:

> "Verantwortlich ist jeweils die nutzende Schule. Das FWU betreibt das System als Auftragsverarbeiter im Auftrag der Schule."

— [AIS.chat, *Datenschutzerklärung*, Stand 12. Mai 2026](https://ais-chat.schule/datenschutzerklaerung/), §B.1

And the lawful basis, in the same terms #11 derived and #8 first proposed:

> "Art. 6 Abs. 1 lit. e DSGVO i. V. m. den jeweiligen Schulgesetzen (Verarbeitung zur Wahrnehmung einer Aufgabe im öffentlichen Interesse – staatlicher Bildungs- und Erziehungsauftrag)
> Eine Einwilligung ist hierfür nicht erforderlich."

— *ibid.*, §B.4

Its child-facing version explains *why* consent is excluded, and the reasoning is EDPB Example 4's detriment test in plain German — independent corroboration of #8 and #11:

> "Denn Einwilligungen müssen freiwillig sein. Zur Schule zu gehen und am Unterricht teilzunehmen kann man sich aber nicht aussuchen."

— *ibid.*, child-friendly version §B.4

**This is a state-built tool, reviewed by the supervisory authorities, that independently reaches every one of #11's conclusions**: school is controller, Art 6(1)(e) via Schulgesetze, consent unavailable because attendance is compulsory. #11's controller/basis analysis is now corroborated by an artefact rather than only by inference.

### The contracting chain — the load-bearing part

The school appoints **FWU**, and FWU appoints everyone else:

> "Damit app.ais-chat.schule betrieben werden kann, beauftragt die jeweils verantwortliche Schule zunächst das FWU – Institut für Film und Bild in Wissenschaft und Unterricht gGmbH ... als technischen Hauptdienstleister im Sinne eines Auftragsverarbeiters nach Art. 28 DSGVO. Das FWU verarbeitet die personenbezogenen Daten ausschließlich auf dokumentierte Weisung der Schule und nicht zu eigenen Zwecken."

— *ibid.*, §B.5

The declared **sub-processors**, verbatim, with their stated activities:

| Sub-processor | Seat | Stated activity |
|---|---|---|
| **Xitaso GmbH** | Augsburg, DE | "Technische Entwicklung, Wartung und Weiterentwicklung des Systems" |
| **IONOS SE** | Montabaur, DE | "Bereitstellung von KI-Infrastruktur und -Diensten (z. B. große Sprachmodelle zur Generierung von Antworten) innerhalb europäischer Rechenzentren" |
| **Microsoft Ireland Operations Ltd** | Dublin, IE | "Bereitstellung von KI-Infrastruktur und -Diensten (z. B. große Sprachmodelle wie ChatGPT zur Generierung von Antworten) innerhalb europäischer Rechenzentren" |
| **T-Systems International GmbH** | Frankfurt, DE | Server infrastructure + "zusätzliche KI-Infrastruktur aus der Open Telekom Cloud, insbesondere für den Betrieb großer Sprachmodelle" |
| **Google Germany GmbH** | München, DE | "Bereitstellung von KI-Diensten (z. B. Sprachmodelle, Bildgenerierung) auf Infrastruktur innerhalb der EU" |

> **Note the surprise.** The state-sanctioned, authority-welcomed school tool routes pupil prompts through **Microsoft Ireland (ChatGPT)** and **Google Germany**. #8 found the Gemini API "blocked as drafted" and OpenAI "usable only with ZDR". Both are *in* the accepted stack — because the contracting entities are EU establishments, FWU holds the Art 28 chain, and the school never touches the vendors' own consumer/API terms. **What made them acceptable was the contracting structure, not a change in the vendors.** This is the strongest available evidence that the ticket's "categories, not vendors" hypothesis is right.

The uniform sub-processor obligations:

> "Mit allen genannten Unternehmen bestehen Verträge zur Auftragsverarbeitung nach Art. 28 DSGVO. Sie sind insbesondere dazu verpflichtet, personenbezogene Daten ausschließlich zur Bereitstellung von app.ais-chat.schule zu verarbeiten, Daten nicht für Werbung, Profilbildung oder andere eigene Zwecke zu nutzen, Daten nicht zum Training eigener KI-Modelle zu verwenden, technische und organisatorische Maßnahmen zum Schutz der Daten zu ergreifen und nur auf dokumentierte Weisung des FWU bzw. der verantwortlichen Schule zu handeln."

— *ibid.*, §B.5

And on transfers:

> "Eine Übermittlung in Drittstaaten findet nicht statt. Die Verarbeitung erfolgt ausschließlich innerhalb der EU."

— *ibid.*, §B.6

### The models on offer

> "OpenAI: GPT-5, GPT-5 mini, GPT-5.5
> Meta: Llama-3.3-70B, Llama-3.1-8B
> Mistral: Mistral Nemo Instruct
> Google: Gemini 3.1. Lite"

— [AIS.chat FAQ](https://ais-chat.schule/faq/), "Welche Sprachmodelle sind in AIS.chat verfügbar?", with the caveat "*Stand und Verfügbarkeit kann je Bundesland variieren*"

Image generation via `Imagen 4` and `GPT-Image-1.5`, teacher-only, and notably: "*die Generierung von Bildern bei Imagen 4, die Kinder zeigen, ist ausgeschlossen*".

### Minimisation by construction — the design lesson for this project

Pupils are pseudonymous end-to-end. Login is via **VIDIS**, which passes only:

> "anonyme Benutzerkennung / Rolle (Schülerin/Schüler oder Lehrkraft) / Schule"

— [Datenschutzerklärung](https://ais-chat.schule/datenschutzerklaerung/), §B.2

with "*Es besteht keine Pflicht zur Angabe des Klarnamens*", and chat content deleted at session end:

> "Die im Rahmen der Nutzung des Chats eingegebenen Inhalte werden nicht dauerhaft gespeichert, sondern nach Beendigung der jeweiligen Sitzung automatisch gelöscht. Dies erfolgt spätestens mit dem Schließen des Webbrowsers."

— *ibid.*, §B.7

> **⚠️ This is where the product structurally diverges from the accepted model, and it is a DPIA item.** AIS.chat is acceptable partly *because* it is stateless per session and never learns who a pupil is. This project is the opposite by design: [#12](https://github.com/danieldannhofer-gif/open-notebook-school/issues/12) mints printed name-and-code sheets for named children, and #8's per-pupil ownership key exists so progress persists across a school year. **The project cannot borrow AIS.chat's minimisation argument.** It must carry its own justification for persistent, attributable pupil records — which #8 already identified as making real anonymity impossible by construction. Worth stating plainly in adoption guidance rather than implying the state tool's posture transfers.
>
> One inconsistency worth noting: the FAQ says "*Lediglich die Chatverläufe werden lokal auf Servern innerhalb der Europäischen Union gespeichert*", which sits awkwardly with the privacy notice's session-end deletion. Low-stakes here; flagged for accuracy.

### The regulator's own words — why a single school is not a viable counterparty

This is the passage that decides the ticket:

> "Da die einzelnen Schulen mit der Umsetzung hinreichender technischer und organisatorischer Maßnahmen häufig überfordert sein dürften, begrüßt die LDI NRW das länderübergreifende Projekt „telli". Diese KI-Chatbot-Anbindung ermöglicht die Nutzung verschiedener LLMs über pseudonymisierte Accounts. Die Datenverarbeitung erfolgt im Rahmen eines Auftragsverarbeitungsvertrags mit dem Medieninstitut der Länder der Bundesrepublik Deutschland."

— [LDI NRW, *31. Bericht*](https://www.ldi.nrw.de/system/files/media/document/file/31_bericht_2026.pdf), §6.1

And the authority is *inside* the project, not merely commenting on it:

> "Die LDI NRW wurde vom Schulministerium NRW in das Projekt eingebunden und berät das beauftragte Medieninstitut gemeinsam mit anderen Datenschutzaufsichtsbehörden in datenschutzrechtlichen Fragen."

— *ibid.*

Two things follow, and both matter more than any provider comparison:

1. **This is as close to an authority endorsement as exists in this space** — "*begrüßt*", from the competent supervisory authority, of a named offering, in an official activity report, with multiple DPAs advising its construction. Nothing comparable exists for any commercial vendor.
2. **The stated rationale is school capacity.** The regulator's view is that individual schools cannot be expected to implement the TOMs this processing requires. That is a direct, sourced answer to #18's "will providers contract with a single school" — reframed: the authority thinks the single-school configuration is the *problem*, and the Länder built an intermediary to remove it. Any guidance that tells a Gymnasium to source its own LLM DPA is advising the shape the regulator identified as unworkable.

### Other state offerings

- **Baden-Württemberg — F13.** A "digital sovereign" assistant on the Land's own **BITBW** hardware, using "*offene Open-Source Sprachmodelle*" — reported as current **Mistral** and **Llama** versions. Both models and application run on state-controlled infrastructure. **Teachers only** ("für Lehrkräfte"), so it is not a pupil-facing precedent. ([IBBW](https://ibbw-bw.de/,Lde/Startseite/IT_Anwendungen_Support/ki-assistenz-f13), [KM BW](https://km.baden-wuerttemberg.de/de/schule/digitalisierung/kuenstliche-intelligenz-im-unterricht))
- **Bayern — ByLKI + ByCS AI**, released statewide "*nach umfassender rechtlicher und technischer Prüfung*", plus AIS.chat. Pupil access is teacher-gated: "*Schülerinnen und Schüler können die Funktionen nutzen, sobald die Lehrkraft die Nutzung im Unterricht oder für selbstständige Lernphasen freigibt*". ByCS materials are scoped **Jgst. 5–8** — i.e. 12-year-olds are squarely in the intended population, which is directly reassuring for this project's age band. ([KM Bayern](https://www.km.bayern.de/meldung/ki-fuer-alle-bayern-stellt-neue-ki-systeme-fuer-alle-schulen-bereit), [ByCS](https://www.bycs.de/ki-systeme/index.html))
- **Rheinland-Pfalz, Mecklenburg-Vorpommern** license commercial tools (**fobizz**, **FelloFish**) as Landeslizenzen. fobizz concludes the AVV automatically on registration via the platform/VIDIS. *(Secondary sourcing — see confidence.)*

---

## 3. Mistral specifically

**Present in the state-sanctioned stack as a sub-processor. Unsuitable as a school's direct counterparty. Never examined by any authority as a named provider.** All three statements are true simultaneously and #14 conflated them.

### It is not endorsed, because nothing is

`Mistral` appears in **none** of: the DSK orientation guide, HBDI's non-EU guidance, the Austrian DSB pages, or LDI NRW's report as a named permission. #14's Mistral recommendation has **no authority backing** — not because authorities rejected it, but because authorities do not work that way (Q1).

### It is tolerated — inside someone else's Art 28 chain

- **AIS.chat** offers `Mistral Nemo Instruct`, served EU-side via IONOS/Open Telekom Cloud, under FWU's sub-processor contract.
- **BW's F13** runs current Mistral models on BITBW state hardware.

In both, the school's counterparty is a **state body**. Mistral is not the processor the school appoints; Mistral (or an EU host running Mistral weights) is a sub-processor two steps down, bound by terms FWU negotiated. #14's transfer reasoning was sound and is *why* Mistral is a comfortable choice for the state integrator. It says nothing about a school contracting directly.

### And directly, its own terms exclude this project

This is the finding that unseats the recommendation. **#8 never examined Mistral's terms** — it covered only OpenAI, Anthropic and Google. That gap was doing real work.

**Use Restriction 2.2(c):**

> "Customer will not, and will not permit any other person (including any End User) to: ... (c) include any personal information of children under 13 or the applicable age of digital consent as Customer Data or allow minors to use the Mistral AI Products without legally adequate consent from their parent or guardian;"

— [Mistral AI, *Commercial Terms of Service*, effective 28 May 2026](https://legal.mistral.ai/terms/commercial-terms-of-service), §2.2(c)

Applied to a class of 12-year-olds:

| Limb | Result |
|---|---|
| "children under 13 or the applicable age of digital consent" | **Fails.** Per #8/#11 the digital-consent age is 16 (DE) / 14 (AT). 12-year-olds are below both, and below 13 outright. Their coursework *is* Customer Data. |
| "allow minors to use ... without legally adequate consent from their parent or guardian" | **Fails, and is unfixable.** Pupils are End Users. #11 established classroom consent is invalid under EDPB 05/2020 Example 4's detriment test — AIS.chat's own notice says the same ("*Einwilligungen müssen freiwillig sein*"). Where the lawful basis is Art 6(1)(e), no valid consent exists to obtain. |

The second limb is a genuine catch-22 and worth stating precisely: **the contractual precondition Mistral imposes is one that data protection law prevents this deployment from satisfying.** A school cannot obtain "legally adequate consent" for compulsory coursework, so it cannot comply with 2.2(c) even in principle.

**Consumer terms are worse, not better:** the general Mistral ToS sets a floor of 13 with parental permission for minors ([help.mistral.ai](https://help.mistral.ai/en/articles/347631-can-children-use-mistral-ai-s-products-and-services)) — "*You must be at least thirteen (13) years old*". Still above 12.

### No minors programme — the asymmetry that decides it

| | Under-18 programme? | Route for a school |
|---|---|---|
| **OpenAI** | **Yes** — under-18 API guidance; ZDR precondition, disclosures, filters, age assurance (#8) | A defined, if effortful, ask: request ZDR, meet the conditions |
| **Anthropic** | **Yes** — *Guidelines for Organizations Serving Minors*; minors expressly contemplated; child-safety system prompt (#8) | A defined ask: implement the guidelines |
| **Google (Gemini API)** | No — 18+ as drafted, i.e. prohibited (#8) | None as drafted |
| **Mistral** | **None found** | **None.** Nothing to request, nothing to comply with |

Mistral's own help centre says only "*You must be at least thirteen (13) years old*" and "*We will delete any Mistral account found to violate these requirements*". There is no organisational-use carve-out, no education programme, no equivalent of Anthropic's minors guidelines.

**This inverts #14's ranking.** #14 preferred Mistral over "OpenAI-with-ZDR" as "a materially easier DPIA story". On transfers, yes. But #14 weighed only the transfer axis. On the **minors axis** — the axis that actually matters for 12-year-olds, and the one #8 spent most of its provider analysis on — Mistral is the *weakest* of the four: OpenAI and Anthropic have paths, Google has a prohibition, and Mistral has a prohibition **with no path**. A vendor that has not thought about minors is not a safer bet than one that has; it is an unexamined one.

### The residual possibility, stated fairly

Mistral's terms permit an `Order Form` and use on customer-controlled infrastructure with express authorisation. **In principle** an Order Form could vary 2.2(c). No public evidence of any education or minors offering was found, and this is speculation — do not build guidance on it. If Mistral-direct ever became strategically necessary, the concrete ask is a written variation of 2.2(c), not ZDR.

---

## 4. Will providers contract with a single school?

The ticket's framing was "a DPA the school cannot obtain is the same blocker as no DPA". The finding is sharper: **for the DPA a school can most easily obtain, obtainability is a trap; for the one it should obtain, the state already provides it.**

### Mistral's DPA is trivially obtainable — and that is the problem

> "The DPA is hereby incorporated to the Agreement by reference."

— [Mistral DPA](https://legal.mistral.ai/terms/data-processing-addendum), §1(a); reinforced at §11.2: "*The Data Processing Addendum is incorporated in the Agreement by reference and forms an integral part of the Agreement.*"

Counterparty: **Mistral AI**, French société, RCS Paris 952 418 325, 15 rue des Halles, 75001 Paris. Sub-processors listed at `trust.mistral.ai/subprocessors` with a 10-day objection window. Module 4 SCCs only for "Restricted Countries" — irrelevant for a DE/AT school, confirming #14's no-transfer-problem reasoning. Training excluded by default (§4.2), with named exceptions (free tier, Feedback, moderation-flagged content, `Labs` models). ZDR exists as a toggle referenced in the terms.

So: **no signature step, no sales gate, no minimum size.** Mechanically, a single Gymnasium can obtain a Mistral DPA in minutes. **That is precisely the failure mode #11 quoted Baden-Württemberg on:**

> "Manche Softwareanbieter eröffnen Lehrkräften die Möglichkeit einen Auftragsverarbeitungsvertrag direkt abzuschließen oder fordern die jeweiligen Nutzer ohne Prüfung von deren Befugnis sogar aktiv dazu auf. In diesen Fällen darf der Vorgang nicht abgeschlossen werden!"

— BW *FAQ Datenschutz an Schulen*, FAQ 44 (via #11)

Frictionless self-serve DPA acceptance is the mechanism BW warns about, and it does not cure 2.2(c) regardless of who signs. **Obtainability was never the binding constraint on Mistral. Permissibility is.**

### The DPA that is both obtainable and correct is FWU's

Every Land provides AIS.chat free, and the school accepts an AVV with FWU to use it. The Schulleitung signs one agreement, with a German gGmbH acting for the Länder, and FWU carries the entire vendor chain. Saarland records an AVV concluded for use within the Online-Schule Saarland; NRW/BW/Hessen/Bayern route it through their state platforms.

**The counterparty question therefore dissolves in Germany**: the school's counterparty is a state media institute that exists to be that counterparty, and no school needs to approach OpenAI, Google, Meta or Mistral at all.

### What was not established

Whether **Anthropic** or **OpenAI** will contract with a single German or Austrian school directly, and at what minimum size — #8 established the terms, #18 asked who may sign. **Still unverified**, and now largely moot for Germany (the state route bypasses it) but **live for Austria** (Q6). Anthropic is absent from the AIS.chat stack entirely, which is itself notable given #8 ranked it "most viable".

---

## 5. Musterverträge and framework agreements

**Germany.** Model AVVs for public bodies exist and are published — a Bayern template (`mustervertrag_auftragsverarbeitung_final.docx`) and a Sachsen-Anhalt template (`Muster_Auftragsverarbeitungsvertrag_nach_DS-GVO_öffentliche_Stelle.docx`), collated at [datenschutz-schule.info](https://datenschutz-schule.info/service-downloads/vertraege-mit-dritten/). **Neither names any AI/LLM provider** — they are generic Art 28 shells. The AI-specific instrument is not a template but the **AIS.chat AVV** itself, supplied per-Land as part of the free offering. Beyond that, Landeslizenzen: RLP and MV with fobizz, MV with FelloFish, BW's F13, Bayern's ByLKI.

**Austria.** The BMB publishes a **`Vorlage Auftragsverarbeitervereinbarung (AVV) Schulen`** (Word, ~36 KB), alongside `Vorlage Art. 32 Kurzformular` and `Vorlage Feststellung der Schutzbedarfsklasse` — [bmb.gv.at/datenschutzschulen](https://www.bmb.gv.at/datenschutzschulen). Named-provider documentation on that page covers **Apple School Manager, Google G-Suite, Microsoft Office 365**, with declarations dated **April–May 2022** — i.e. pre-generative-AI. **No AI/LLM guidance and no AI provider documentation.**

> **The asymmetry in one line.** Germany gives a school a *finished* AI arrangement; Austria gives it a *blank* AVV template. A template is only useful against a counterparty willing to sign it — which returns Austria to the unresolved question of Q4.

---

## 6. Austria

**No state-brokered AI tool for schools was found, and this is the most consequential gap in the document.**

- **BMB / BMBWF** publishes AI guidance framed pedagogically, not as a procurement route: "*KI wird nicht „einfach genutzt", sondern verstanden und bewusst eingesetzt*" ([bmb.gv.at/ki](https://www.bmb.gv.at/ki)). It names **no centrally provided tool**. The only named product is **Teachino**, and only as a completed PH Wien **pilot report** — not an offering.
- **DSB** names no providers (Q1) and takes the deploying-body-is-controller position, consistent with #11's statutory § 4 Abs 1 Z 1 BilDokG 2020 finding (principals are controllers).
- **The school datenschutz page** provides the Muster-AVV but its named-provider documentation stops at 2022 cloud suites (Q5).

An Austrian Gymnasium is therefore in the position German schools occupied before FWU: it must find its own Art 28 counterparty, from a vendor pool where — per #8 and Q3 — Google prohibits under-18 services, OpenAI requires ZDR by approval, Mistral prohibits under-digital-consent-age data with no exception route, and only Anthropic has an affirmative minors programme. And per #11, only the *Schulleiter/in* can validly sign, by statute.

> **Open question, and it should be flagged on the map rather than guessed at.** Whether an Austrian school can join AIS.chat, or whether an Austrian equivalent is in progress, was **not established**. AIS.chat is constitutionally a *German* Länder project (Digitalpakt, "*im Auftrag aller 16 Bundesländer*"), so cross-border access is not to be assumed. If the jurisdiction turns out to be Austria, **this is the blocker and it is unresolved** — and it makes the jurisdiction question urgent rather than cosmetic.

---

## Consequences for the project

Stated as decisions this research supports, not as schema changes — #10's untyped conduit and #14's assertion gate both stand.

1. **Drop Mistral as the named recommendation.** Not on transfer grounds (#14 was right there) but on its own terms of service, §2.2(c), whose second limb this deployment cannot satisfy in principle. Replacing it with another vendor name repeats the category error.
2. **Write guidance in categories, plus one signpost.** The categorical criteria are in Q1. The signpost is: *a German school should point the endpoint at its Land's AIS.chat / state AI offering, and accept the AVV the Land provides.* That is the only configuration with an authority's published welcome behind it.
3. **State the Austrian gap explicitly rather than papering over it.** Guidance that reads the same for both jurisdictions is wrong for Austria. Austria has a Muster-AVV and no counterparty; that is a genuine adoption blocker, not a paperwork step.
4. **#14's assertion sentence gets more answerable, and one clause gets easier.** A German admin can truthfully complete "*a DPA is signed with the processor named below*" with **FWU**, because that is exactly the arrangement the Land supplies. This is a real improvement on the pre-#18 position, where the sentence had no plausible completion for a single Gymnasium. It also strengthens #14's rejection of **OpenRouter** by analogy: FWU is a router *with* a named Art 28 counterparty and a published sub-processor list, which is precisely what OpenRouter lacks. **The distinction #14 drew is a real one and now has a worked example on both sides.**
5. **Do not borrow AIS.chat's minimisation argument.** It is stateless per session and pseudonymous by construction; this project is persistent and attributable by design (#8, #12). The DPIA must carry that difference explicitly. Adoption guidance that gestures at "the state tool does this too" would be false assurance of the kind #11 and #14 both warned against.
6. **⚠️ A genuine tension worth surfacing.** If the recommendation becomes "use your Land's AIS.chat", a school already has an approved, free, pupil-facing LLM chat with a signed AVV. That is not a competitor to this project — flashcards, quizzes, courses and per-pupil progress are not what AIS.chat does — but it does mean **this project's marginal ask of a school is a second processor relationship for capability the state route does not cover.** Adoption guidance should be honest about that rather than presenting the AVV as a formality. There is also a live architectural question, out of scope here: whether the conduit could point at a Land AI endpoint at all, or whether AIS.chat is a closed web application with no OpenAI-compatible API a third-party tool may call. **If it has no such API, recommendation 2's signpost is not actually reachable through #10's conduit** — worth checking before the guidance is written.

---

## Corrections and confirmations to #8 and #11

### Confirmed, and upgraded from inference to artefact

- **#11: the school is the controller, represented by the Schulleitung.** ✅ Confirmed by the state tool's own privacy notice: "*Verantwortlich ist jeweils die nutzende Schule.*" This is now corroborated by a Länder-built, DPA-advised artefact, not only by EDPB para 19 plus Länder guidance.
- **#8/#11: lawful basis is Art 6(1)(e) via the Schulgesetze; no consent required.** ✅ Confirmed verbatim by AIS.chat, and by LDI NRW citing §§ 120/121 SchulG NRW.
- **#11: classroom consent is invalid on the detriment test.** ✅ Independently confirmed in the state tool's own child-facing reasoning.
- **#8/#11: the DPIA is mandatory.** ✅ Confirmed by LDI NRW for this exact processing, with the added point that a DPIA may reveal the need for *new legislation*.
- **#11: NRW's §§ 120/121 SchulG + Art 6(1)(e)** — was **medium confidence** from a practitioner site. ✅ **Now high confidence from LDI NRW directly**, with two corrections: it is **§ 120 Abs. 5** (not Abs. 1), and the authority calls it only "*einstweilen eine mögliche Rechtsgrundlage*".
- **#8: Google Gemini API is "blocked as drafted"; OpenAI needs ZDR.** ✅ Survives *as a statement about those vendors' direct terms* — and is now shown to be **routable around** via an EU-established reseller in a state Art 28 chain. Not a contradiction; a scope clarification.

### Corrected

- **#14: "Guidance recommends Mistral."** ❌ **Unseated.** Correct on transfers, but Mistral's Commercial ToS §2.2(c) prohibits the data and the users this project is built for, with no minors programme and no exception route. #14's reasoning was sound on the axis it examined and did not examine the decisive axis.
- **#14's ranking of Mistral above "OpenAI-with-ZDR".** ❌ **Inverted on the minors axis.** OpenAI and Anthropic have defined under-18 paths; Mistral has a prohibition with none.
- **#8's provider analysis was incomplete in a load-bearing way.** ❌ It examined OpenAI, Anthropic and Google but **not Mistral** — the vendor #14 went on to recommend. The gap is the direct cause of #14's error. *Lesson for the map: a recommendation adopted from first-principles reasoning should trigger a terms check on that specific vendor before it is written down.*
- **#8's open question "whether any state DPA has published a position on US LLM providers in schools", flagged as potentially decisive.** ❌ **Resolved, and it is not decisive in the way #8 feared.** Authorities do not publish provider verdicts; they publish criteria. The one thing they *did* endorse routes pupil data through Microsoft Ireland and Google Germany — so the feared "US provider veto" does not exist as such. The operative test is the **contracting structure and establishment of the counterparty**, not the vendor's nationality.
- **#11's framing of "whether a school would in fact approve" as practically uncertain.** ⚠️ **Softened for Germany.** A school does not need to evaluate an LLM vendor; it accepts a Land-supplied AVV for a tool its own ministry rolled out. Unchanged for Austria.

### New, not previously on the map

- **The state-brokered-intermediary pattern** — school → state body → vendors — as the configuration authorities actually accept. Neither #8 nor #11 anticipated it. It is a **fourth option** alongside #10's self-hosted / direct-commercial / router trichotomy, and it is the only one with a published regulator welcome.
- **LDI NRW's capacity finding** — individual schools "*häufig überfordert*" by the required TOMs — as a sourced reason the single-school configuration is disfavoured *by the regulator*, independent of any vendor's willingness to sign.
- **The Austria/Germany asymmetry** as an adoption blocker, which makes the long-deferred jurisdiction question load-bearing for the first time.

---

## Confidence and gaps

**High confidence — primary sources read directly this session:**

- AIS.chat *Datenschutzerklärung* (Stand 12 May 2026) — controller/processor split, Art 6(1)(e) basis, full sub-processor list with activities, no-third-country statement, retention, VIDIS pseudonymisation. Full HTML extracted and read locally.
- AIS.chat FAQ — model list by vendor, per-Land variability, image models.
- Mistral *Commercial Terms of Service* (eff. 28 May 2026) §2.2(c), §4.1, §4.2, §1.1; *Data Processing Addendum* §1(a), §10.1, §11.2, sub-processor and SCC clauses; contracting entity details. Full HTML extracted and read locally.
- DSK *Orientierungshilfe KI und Datenschutz* (6 May 2024) — 15-page PDF extracted locally; §§1.7, 1.8, 2.1, 2.5 quoted; **verified by search that no vendor is named**.
- LDI NRW *31. Bericht* (2026) §6.1 — 164-page PDF extracted locally; the "*begrüßt*", "*häufig überfordert*", § 120 Abs. 5 and DPIA passages quoted directly.
- HBDI non-EU AI recommendations; Austrian DSB AI pages; BMB `datenschutzschulen` template list; BMB `/ki` page.

**Medium confidence — reliable but single-sourced or secondary:**

- **BW F13's specific models (Mistral + Llama).** IBBW says only "*offene Open-Source Sprachmodelle*"; the Mistral/Llama identification is from press/secondary reporting. The BITBW state-hosting claim is first-party.
- **Per-Land rollout dates and Landeslizenz arrangements** (RLP/MV–fobizz, MV–FelloFish; Oct–Dec 2025 dates). Ministry press releases and Deutsches Schulportal; not individually verified per Land.
- **fobizz AVV concluded automatically on registration.** From fobizz/secondary sources, not read in the platform terms.
- **Bayern's ByCS model list** (`gpt-5.5`, `meta-Llama`, `o3-mini`, `dall-e-3`). Secondary; ByCS's own pages did not enumerate providers.
- **AIS.chat retention.** Privacy notice says session-end deletion; FAQ says chat histories stored on EU servers. Unreconciled minor inconsistency.

**Explicitly NOT established — do not rely on these:**

- **Whether AIS.chat exposes an OpenAI-compatible API a third-party tool could call.** Directly load-bearing for recommendation 2 — if it is a closed web app, the signpost is not reachable through #10's conduit. **Check before writing guidance.** (The source is public at `github.com/FWU-DE/telli-dialog`, so this is cheaply answerable.)
- **Whether Austrian schools may use AIS.chat, or whether an Austrian equivalent exists or is planned.** The decisive open question if the jurisdiction is Austria.
- **Whether Anthropic or OpenAI will contract with a single DE/AT school**, and at what size. Carried over unresolved from #8/#11. Now moot for Germany via the state route; live for Austria. Anthropic's absence from the AIS.chat stack was not explained by any source.
- **Whether Mistral would vary §2.2(c) in an Order Form**, or has any unpublished education/minors offering. Speculation; no evidence either way.
- **The Bavarian DPA's own AI orientation guide (`datenschutz-bayern.de/ki/OH_KI.pdf`).** Fetched (2.5 MB) but not text-extracted; **not read**. It is a public-sector AI guide and could contain a Bavaria-specific position. A remaining cheap check.
- **Positions of Berlin, Niedersachsen, Rheinland-Pfalz DPAs specifically on schools + LLMs.** Not found as dedicated documents. RLP's Kugelmann co-leads the DSK AI task force, so the DSK guide is likely his substantive position, but that is inference.
- **The AIS.chat AVV text itself.** Its existence and parties are documented; the clauses were not read.
- **UK.** Not researched. No comparable state-brokered offering surfaced incidentally.
- **EU AI Act interaction.** Secondary sources flag August 2026 high-risk obligations for education platforms. Not verified against the Regulation and outside this ticket's scope, but plausibly a new constraint on the whole category.

---

## Sources

All accessed **2026-07-30**. **[P]** primary (legislation, regulator, ministry, or the operator's own legal text), **[S]** secondary.

### German supervisory authorities

- **[P]** DSK, *Orientierungshilfe Künstliche Intelligenz und Datenschutz* (6 May 2024) — https://www.datenschutz.rlp.de/fileadmin/datenschutz/Dokumente/Orientierungshilfen/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz_web.pdf — *§2.1 Art 28 relationship; §2.5 no-training/no-history defaults; §1.7 closed systems preferred; names no vendor*
- **[P]** LDI NRW, *31. Bericht* (2026), §6.1 *„Ich frag' einfach Chatty" – Einsatz von KI macht Schule* — https://www.ldi.nrw.de/system/files/media/document/file/31_bericht_2026.pdf — *welcomes telli; schools "häufig überfordert"; § 120 Abs. 5 / § 121 SchulG NRW; DPIA may require new legislation; §6.2 Apple/iCloud for comparison*
- **[P]** HBDI (Hessen), *Empfehlungen zum Einsatz von KI-Anwendungen von Anbietern außerhalb der EU* — https://datenschutz.hessen.de/datenschutz/kuenstliche-intelligenz/empfehlungen-zum-einsatz-von-ki-anwendungen-von-anbietern-ausserhalb-der-eu — *categorical, Art 45 threshold, no vendor named*
- **[P]** DSK, *Orientierungshilfen* index — https://www.datenschutzkonferenz-online.de/orientierungshilfen.html
- **[P]** BayLDA, *Datenschutz bei KI-Projekten in der bayerischen Verwaltung* — https://www.datenschutz-bayern.de/ki/OH_KI.pdf — *fetched but NOT read; see gaps*

### The state-brokered tool (AIS.chat / telli)

- **[P]** AIS.chat, *Datenschutzerklärung* (Stand 12 May 2026) — https://ais-chat.schule/datenschutzerklaerung/ — *the central document: school as controller, FWU as Art 28 processor, five named sub-processors, Art 6(1)(e), no third-country transfer, session-end deletion, VIDIS*
- **[P]** AIS.chat, *FAQ* — https://ais-chat.schule/faq/ — *model list: OpenAI GPT-5 family, Meta Llama, Mistral Nemo Instruct, Google Gemini 3.1 Lite; per-Land variability*
- **[P]** FWU, *Aus telli wird AIS.chat* — https://fwu.de/presse/neuer-name-fuer-den-ki-chatbot-aus-telli-wird-ais-chat/
- **[P]** Source code — https://github.com/FWU-DE/telli-dialog
- **[P]** MSB NRW, *Bereitstellung des ländergemeinsamen KI-Chatbots „telli"* (4 Dec 2025) — https://www.schulministerium.nrw/04122025-bereitstellung-des-laendergemeinsamen-ki-chatbots-telli — *all 16 Länder; AVV acceptance; models; EU-only*
- **[P]** MSB NRW, *Umbenennung … „telli" wird „AIS.chat"* (18 May 2026) — https://www.schulministerium.nrw/18052026-umbenennung-des-laendergemeinsamen-ki-chatbotstelli-wird-aischat
- **[P]** KM Bayern, *KI für alle* — https://www.km.bayern.de/meldung/ki-fuer-alle-bayern-stellt-neue-ki-systeme-fuer-alle-schulen-bereit — *"umfassende rechtliche und technische Prüfung"; teacher-gated pupil access*
- **[P]** ByCS, *Neue KI-Systeme für Schulen in Bayern* — https://www.bycs.de/ki-systeme/index.html — *KI-Kompass Jgst. 5–8*
- **[P]** KM Baden-Württemberg, *KI-Chatbot für Schulen geht an den Start* — https://km.baden-wuerttemberg.de/de/service/pressemitteilung/pid/ki-chatbot-fuer-schulen-geht-an-den-start
- **[P]** IBBW, *KI-Assistenz F13* — https://ibbw-bw.de/,Lde/Startseite/IT_Anwendungen_Support/ki-assistenz-f13 — *BITBW hosting; open-source models; teachers only*
- **[S]** Deutsches Schulportal, *AIS.chat, fobizz und Co* — https://deutsches-schulportal.de/unterricht/fobizz-schulki-und-co-welche-ki-tools-koennen-schulen-nutzen/ — *"Alle Bundesländer stellen … Landeslizenzen … kostenlos bereit"; per-Land tools*
- **[S]** datenschutz-schule.info, *LDI NRW zu KI in Schulen* — https://news.datenschutz-schule.info/2026/06/03/ldi-nrw-zu-ki-in-schulen/ — *pointer to the LDI primary document*
- **[S]** FWU press, *telli an weiteren Schulen im Einsatz* — https://fwu.de/presse/telli-an-weiteren-schulen-im-einsatz/

### Mistral (the unseating evidence)

- **[P]** Mistral AI, *Commercial Terms of Service*, eff. 28 May 2026 — https://legal.mistral.ai/terms/commercial-terms-of-service — ***§2.2(c) the decisive clause***; §4.1 no-training licence carve-out; §4.2 training exceptions; §1.1 Order Form / customer infrastructure
- **[P]** Mistral AI, *Data Processing Addendum* — https://legal.mistral.ai/terms/data-processing-addendum — *§1(a) and §11.2 auto-incorporation; §10.1 30-day deletion; Module 4 SCCs; contracting entity RCS Paris 952 418 325*
- **[P]** Mistral AI help centre, *Can children use Mistral AI's products and services?* — https://help.mistral.ai/en/articles/347631-can-children-use-mistral-ai-s-products-and-services — *13+ with parental permission; no organisational/education carve-out*
- **[P]** Mistral AI legal index — https://legal.mistral.ai/terms — *no minors or education programme listed*
- **[P]** Mistral AI sub-processors — https://trust.mistral.ai/subprocessors *(JS-rendered; not enumerated)*

### Austria

- **[P]** BMB, *Datenschutz in Schulen* — https://www.bmb.gv.at/datenschutzschulen — *`Vorlage Auftragsverarbeitervereinbarung (AVV) Schulen`; Art 32 Kurzformular; Schutzbedarfsklasse; named-provider docs stop at 2022 cloud suites; **no AI guidance***
- **[P]** DSB, *Künstliche Intelligenz & Datenschutz* — https://dsb.gv.at/kuenstlichebrintelligenz/kuenstliche-intelligenz-datenschutz — *no vendor named; deploying body is controller*
- **[P]** BMB, *Künstliche Intelligenz – Chance für Österreichs Schulen* — https://www.bmb.gv.at/ki — *pedagogical framing; no centrally provided tool; Teachino as pilot report only*
- **[P]** BMBWF, *KI* — https://www.bmbwf.gv.at/Themen/schule/zrp/ki.html

### Model contracts

- **[S]** datenschutz-schule.info, *Verträge mit Dritten* — https://datenschutz-schule.info/service-downloads/vertraege-mit-dritten/ — *Bayern and Sachsen-Anhalt public-body Muster-AVVs; no AI provider named*

### Prior research in this repo

- `docs/research/data-protection-for-minors.md` — #8: provider terms for OpenAI / Anthropic / Google (**not Mistral** — the gap this document closes), DPIA, personal-data analysis
- `docs/research/controller-and-lawful-basis.md` *(branch `research/controller-and-lawful-basis`)* — #11: school as controller, Art 6(1)(e), teacher cannot sign a DPA, BW FAQ 44/45
