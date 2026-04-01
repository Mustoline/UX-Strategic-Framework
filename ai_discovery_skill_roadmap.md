# AI discovery skill roadmap

Internal note: This is a planning document for building an AI-powered workflow that supports delivery of Package A, Package B, and Package C. The roadmap is split into two layers:

* Activity-facing skills that mirror the package activities directly
* Shared helper skills that avoid duplicating interview, workshop, synthesis, mapping, and review logic

Two existing assets should shape the roadmap:

* `discovery-interview` should be adapted into a reusable interview helper rather than used as-is
* `ux-strategy-reviewer` should stay unchanged and remain the final quality gate

## Priority guide

* **P1:** Build first. Foundational skills that unlock Package A and the core workflow structure
* **P2:** Build next. Skills that expand the workflow to cover Package B and deepen the research and concept workflow
* **P3:** Build after that. Skills needed for the more complex cross-functional work in Package C

## Activity-facing skills

| Skill name | Supports activities | Inputs | Outputs | Priority |
| --- | --- | --- | --- | --- |
| `sponsor-workshop-facilitator` | `A1.1` Run a 90-minute sponsor workshop | Business context; problem area; sponsor roles; known constraints; existing evidence | Workshop agenda; critical questions; note structure; decision summary; target users; success measures; constraints register | P1 |
| `evidence-baseline-reviewer` | `A1.2` Review analytics, support issues, sales input, and prior research | Analytics summary; support themes; sales input; prior research; problem statement | Evidence inventory; known-versus-assumed view; strongest signals summary; evidence gaps; questions to test next | P1 |
| `journey-step-mapper` | `A1.3` Run a 60-90 minute mapping session of the selected journey step | Selected journey step; stakeholder notes; evidence baseline; touchpoints; dependencies | One-page journey-step map; breakdown list; friction summary; participant readout | P1 |
| `option-review-facilitator` | `A2.1` Run a 2-hour option review | Solution directions; agreed criteria; known risks; constraints; evidence summary | Comparison scorecard; tradeoff summary; preferred-direction rationale; unresolved questions | P1 |
| `recommendation-packager` | `A3.1` Prepare a short recommendation document with a simple concept view or clickable prototype | Decision summary; preferred direction; target users; success criteria; risks; dependencies | Recommendation document; concept brief or prototype brief; what to build now; what to defer; validation list | P1 |
| `scoping-workshop-facilitator` | `B1.1` Run a 2-hour scoping workshop | Opportunity area; sponsor goals; business case; journey scope; known stakeholders | Scoping agenda; aligned scope statement; business case summary; success criteria; key discovery questions | P2 |
| `user-research-runner` | `B1.2` Conduct 4-6 semi-structured user interviews | Research goals; participant criteria; available evidence; interview constraints; interview type | Recruitment brief; interview guide; note template; interview summaries; needs, barriers, and decision-point synthesis | P2 |
| `current-journey-synthesizer` | `B2.1` Map the current journey | Interview summaries; evidence review; touchpoints; teams; systems; pain points | Current-state journey map; breakdowns across users, teams, and systems; opportunity areas; decision criteria | P2 |
| `future-state-concept-facilitator` | `B3.1` Run a 2-3 hour concept working session | Current-state findings; opportunity areas; design principles; constraints; stakeholders | Future-state journey; concept principles; service-change list across process, content, ownership, and data | P2 |
| `prototype-and-prioritization-facilitator` | `B4.1` Build a clickable prototype and run a 2-hour prioritization workshop | Future-state concept; core flow; opportunity list; business relevance; user value; implementation effort | Prototype brief; prioritization matrix; build-first recommendation; defer list; validation priorities | P2 |
| `executive-and-service-owner-interviewer` | `C1.1` Conduct 5-7 executive and service-owner interviews | Strategic context; business case; stakeholder list; investment questions; known service pressures | Interview guide; executive summaries; strategic themes; risk summary; investment-question brief | P3 |
| `ecosystem-workshop-facilitator` | `C1.2` Run a half-day ecosystem workshop | Service area; departments; touchpoints; systems; operational actors; strategic objectives | Ecosystem workshop agenda; ecosystem map; agreed service scope; critical service moments; study focus | P3 |
| `contextual-fieldwork-runner` | `C2.1` Conduct contextual interviews, observations, or shadowing sessions | Fieldwork goals; service context; user or staff profiles; operational data; observation constraints | Fieldwork guide; observation template; session summaries; workarounds; hidden-effort log; ownership-gap summary | P3 |
| `service-blueprint-builder` | `C2.2` Build a current-state service blueprint | Fieldwork summaries; process steps; teams; systems; dependencies; operational issues | Current-state service blueprint; delay points; duplication summary; cost or effort hotspots; ownership gaps | P3 |
| `future-state-service-model-and-validation` | `C3.1` Run a future-state service model workshop and validate the concept | Current-state blueprint; opportunity areas; service principles; validation participants; feasibility constraints | Target-state service model; validation guide; feedback synthesis; refinement log; feasibility signals | P3 |
| `roadmap-and-business-case-framer` | `C4.1` Run a roadmap and business case session | Target-state model; dependencies; change implications; investment questions; outcome hypotheses | Phased roadmap; dependency view; operating-model implications; ownership changes; ROI hypothesis summary | P3 |

## Shared helper skills

| Skill name | Supports activities | Inputs | Outputs | Priority |
| --- | --- | --- | --- | --- |
| `workshop-design-kit` | `A1.1`, `A1.3`, `A2.1`, `B1.1`, `B3.1`, `B4.1`, `C1.2`, `C3.1`, `C4.1` | Workshop objective; participant mix; duration; decisions to reach; current evidence | Agenda; facilitation prompts; timeboxes; note-capture structure; playback summary format | P1 |
| `evidence-ingest` | `A1.2`, `B1.2`, `C2.1`, `C4.1` | Analytics extracts; support issues; sales input; research notes; operational data | Normalized evidence log; signal summary; source-by-source findings; gap list; assumption list | P1 |
| `artifact-writer` | `A3.1`, `B2.1`, `B4.1`, `C2.2`, `C4.1` | Notes; synthesis outputs; structure template; audience; document purpose | Client-ready draft; concise summary; decision-oriented framing; next-step language | P1 |
| `map-structure-generator` | `A1.3`, `B2.1`, `C1.2`, `C2.2`, `C3.1` | Map type; actors; touchpoints; process steps; systems; dependencies | Consistent journey-map, ecosystem-map, and blueprint structure; section prompts; labeling rules | P1 |
| `discovery-interview` (adapted) | `B1.2`, `C1.1`, `C2.1`, `C3.1` validation interviews | Interview purpose; participant type; evidence baseline; interview constraints; desired decisions | Interview guide; probe questions; note template; synthesis prompts; interview-summary structure | P2 |
| `insight-synthesizer` | `B1.2`, `B2.1`, `C1.1`, `C2.1`, `C3.1` | Interview notes; observation notes; evidence summaries; workshop outputs | Clustered findings; top needs; barriers; decision criteria; opportunity areas; confidence notes | P2 |
| `decision-and-prioritization-framer` | `A2.1`, `B4.1`, `C4.1` | Options; criteria; effort estimates; value signals; constraints; dependencies | Decision criteria set; prioritization model; tradeoff framing; ranked recommendations | P2 |
| `prototype-brief-generator` | `A3.1`, `B4.1`, `C3.1` | Chosen concept; target users; key decisions; assumptions to test | Prototype brief; screen or flow list; test scenarios; validation questions | P2 |
| `ux-strategy-reviewer` | All package outputs | Draft artifact; package context; intended audience; offer logic | Review comments on tone, clarity, ROI logic, package alignment, and markdown quality | P1 |

## Suggested build sequence

1. Build the `P1` helper skills first so every later skill can share the same workshop, evidence, mapping, writing, and review logic.
2. Build the `P1` activity-facing skills next so Package A can run end to end as the first usable workflow.
3. Adapt `discovery-interview`, then build the `P2` skills to cover Package B and strengthen interview-based research and prioritization.
4. Build the `P3` skills last to support the broader service-model, fieldwork, and roadmap work in Package C.

## What this roadmap should enable

When these skills are in place, the workflow should be able to:

* Prepare each workshop, interview, or mapping session with the right agenda, questions, and note structure
* Turn raw evidence and session notes into consistent synthesis outputs rather than isolated transcripts
* Produce the concrete package deliverables in a format clients can recognize and use
* Apply the same decision logic, mapping structure, and tone across all three packages
* Keep the final artifacts aligned with the upstream discovery offer and the `ux-strategy-reviewer` standard
