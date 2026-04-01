# AI discovery P1 skill briefs

Internal note: This document defines the first implementation wave from [ai_discovery_skill_roadmap.md](ai_discovery_skill_roadmap.md). These are short design briefs for the `P1` skills, not the final `SKILL.md` files. Each brief covers purpose, prompt behavior, required templates, and artifact outputs.

The workflow assumption is the same across all briefs:

* `Prep` creates the agenda, questions, inputs, and working structure
* `Run` supports the live activity or structured analysis
* `Synthesize` turns the work into a usable internal or client-facing artifact

Activity-facing skills should call the shared helper skills rather than duplicate workshop, evidence, mapping, writing, or review logic.

## Activity-facing P1 skills

### `sponsor-workshop-facilitator`

**Purpose:** Support Activity `A1.1` by helping the team run a focused sponsor workshop that defines the decision to be made, the target users, the success measures, and the main business and technical constraints.

**Prompt behavior:**

* `Prep`: Confirm the decision this workshop must support, who is attending, what evidence already exists, and which constraints are already known. Generate a workshop agenda, question set, and note structure.
* `Run`: Guide the discussion toward the business question, target users, success measures, constraints, assumptions, and decision criteria. Push the group toward concrete language rather than vague ambition.
* `Synthesize`: Produce a clean workshop summary that captures the agreed decision frame, target users, success measures, constraints, and open questions.

**Required templates:**

* Sponsor workshop agenda
* Sponsor workshop note grid
* Decision framing template
* Target-user summary template
* Success-measure template
* Constraints register

**Artifact outputs:**

* Sponsor workshop summary
* Target-user and success-measure brief
* Business and technical constraints register
* Open-questions list for follow-up

### `evidence-baseline-reviewer`

**Purpose:** Support Activity `A1.2` by turning existing evidence into a practical baseline that separates known signals from assumption and makes the next discovery questions explicit.

**Prompt behavior:**

* `Prep`: Confirm the problem area, gather all available evidence sources, and identify what decisions the evidence needs to inform.
* `Run`: Review analytics, support issues, sales input, and prior research in a structured way. Rank source strength, pull out repeat patterns, and flag weak or conflicting evidence.
* `Synthesize`: Produce a concise evidence baseline showing what is known, what is still assumption, where the strongest signals sit, and what still needs validation.

**Required templates:**

* Evidence inventory
* Source review template
* Known-versus-assumed matrix
* Signal-strength summary
* Evidence-gap log

**Artifact outputs:**

* Evidence baseline summary
* Known-versus-assumed view
* Strongest-signal summary
* Evidence-gap and validation-question list

### `journey-step-mapper`

**Purpose:** Support Activity `A1.3` by helping the team map a selected journey step and identify where users or staff lose time, confidence, or momentum.

**Prompt behavior:**

* `Prep`: Confirm the selected journey step, the actors involved, the touchpoints in scope, and the evidence already gathered.
* `Run`: Structure the mapping session around actors, touchpoints, dependencies, and breakdowns. Push participants to describe the real current state rather than the intended process.
* `Synthesize`: Convert the session notes into a one-page map and a short list of the main breakdowns and friction points.

**Required templates:**

* Journey-step map canvas
* Actor and touchpoint template
* Breakdown capture sheet
* Friction scoring template

**Artifact outputs:**

* One-page journey-step map
* Top breakdowns summary
* Friction and dependency notes

### `option-review-facilitator`

**Purpose:** Support Activity `A2.1` by helping the team compare 1-2 solution directions against agreed business, user, and delivery criteria and reach a grounded recommendation.

**Prompt behavior:**

* `Prep`: Confirm which options are being compared, what criteria matter most, and which constraints or risks must be considered.
* `Run`: Facilitate a structured comparison of the options using the agreed criteria. Keep the group focused on practical tradeoffs rather than abstract preferences.
* `Synthesize`: Produce a scorecard, tradeoff summary, preferred-direction rationale, and list of unresolved risks or checks.

**Required templates:**

* Option comparison scorecard
* Decision-criteria template
* Tradeoff log
* Risk and dependency sheet

**Artifact outputs:**

* Option comparison summary
* Preferred-direction recommendation
* Risk and dependency list
* Outstanding validation questions

### `recommendation-packager`

**Purpose:** Support Activity `A3.1` by turning the discovery work into a clear recommendation document and a tangible concept brief that can support the next delivery decision.

**Prompt behavior:**

* `Prep`: Gather the agreed direction, target users, success measures, map findings, and unresolved risks.
* `Run`: Structure the recommendation around the decision, the rationale, the concept direction, what should be built next, and what should be deferred.
* `Synthesize`: Produce a concise recommendation document plus a simple concept brief or prototype brief and a clear next-step list.

**Required templates:**

* Recommendation document template
* Concept brief template
* Build-now, defer, validate template
* Risk and next-step template

**Artifact outputs:**

* 1-2 page recommendation document
* Concept brief or prototype brief
* Build-now, defer, validate summary
* Risk and next-step list

## Shared helper P1 skills

### `workshop-design-kit`

**Purpose:** Provide the reusable workshop scaffolding used by the activity-facing workshop skills so agendas, facilitation prompts, and outputs stay consistent across packages.

**Prompt behavior:**

* `Prep`: Take a workshop objective, participant mix, duration, and intended decision and generate the session structure.
* `Run`: Provide timeboxes, prompt language, breakout or discussion instructions, and note-capture guidance during the session.
* `Synthesize`: Produce a workshop playback structure that can be reused by the activity-facing skill after the session.

**Required templates:**

* Agenda template
* Timebox template
* Facilitation prompt bank
* Workshop note grid
* Playback summary template

**Artifact outputs:**

* Workshop pack
* Facilitation guide
* Structured notes shell
* Playback summary draft

### `evidence-ingest`

**Purpose:** Normalize evidence from different sources so later skills do not have to re-handle raw analytics, support issues, sales input, or research notes from scratch.

**Prompt behavior:**

* `Prep`: Confirm source types, source quality, date range, and why each source matters to the decision at hand.
* `Run`: Extract the relevant signals from each source, group them into patterns, and flag weak evidence, conflicts, or missing context.
* `Synthesize`: Produce a normalized evidence pack that downstream skills can use without re-reading every raw input.

**Required templates:**

* Evidence log
* Source summary template
* Signal extraction sheet
* Assumption log
* Evidence-gap template

**Artifact outputs:**

* Normalized evidence pack
* Source-by-source summary
* Signal summary
* Assumption and gap list

### `artifact-writer`

**Purpose:** Turn synthesis outputs into client-ready drafts that match the tone, structure, and decision-support logic of the upstream discovery offer.

**Prompt behavior:**

* `Prep`: Confirm the audience, artifact type, package context, and the decision the document needs to support.
* `Run`: Organize the available notes and synthesis into a clear narrative with the right level of business focus and practical detail.
* `Synthesize`: Produce a draft document that can go through `ux-strategy-reviewer` with minimal cleanup.

**Required templates:**

* Executive summary template
* Recommendation summary template
* Workshop readout template
* Evidence summary template
* Risk and next-step template

**Artifact outputs:**

* Client-ready draft
* Executive summary
* Recommendation or readout draft
* Risk and next-step section

### `map-structure-generator`

**Purpose:** Create consistent structures for journey maps, ecosystem maps, and service blueprints so all mapping outputs follow the same logic and labeling discipline.

**Prompt behavior:**

* `Prep`: Confirm the map type, scope, actors, touchpoints, systems, and the decision the map needs to support.
* `Run`: Generate the structure, sections, labels, and field prompts that the mapping skill should use while the team works.
* `Synthesize`: Produce a finished map scaffold with a consistent legend, breakdown areas, and output format.

**Required templates:**

* Journey map structure
* Ecosystem map structure
* Service blueprint structure
* Map legend template
* Breakdown and dependency prompt set

**Artifact outputs:**

* Map scaffold
* Section and label set
* Legend and annotation rules
* Breakdown capture structure

### `ux-strategy-reviewer`

**Purpose:** Act as the final quality gate for all P1 outputs. This skill already exists and should be reused without redesign.

**Prompt behavior:**

* `Prep`: Confirm the document type, audience, and package context.
* `Run`: Review the draft for Danish-pragmatic tone, ROI logic, buzzword removal, package completeness, and markdown quality.
* `Synthesize`: Produce a concise review summary with specific corrections and a clear readiness judgment.

**Required templates:**

* Review checklist
* Tone and ROI checklist
* Buzzword correction reference
* Package completeness checklist
* Markdown review checklist

**Artifact outputs:**

* Review comments
* Revision list
* Client-ready or revision-required recommendation

## Recommended next step after these briefs

Once these P1 briefs are agreed, the most practical next move is to create the actual helper skills first:

1. `workshop-design-kit`
2. `evidence-ingest`
3. `artifact-writer`
4. `map-structure-generator`

After that, build the five `P1` activity-facing skills on top of them so Package A becomes the first usable end-to-end workflow.
