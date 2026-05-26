# Package A template library

Use this file as the reusable template source for live Package A projects.

## Suggested live-project files

* `project_index.md`
* `01-inputs/package_a_stage_0_intake_input.md`
* `01-inputs/package_a_activity_1_1_input.md`
* `01-inputs/package_a_activity_1_2_input.md`
* `01-inputs/package_a_activity_1_3_input.md`
* `01-inputs/package_a_activity_2_1_input.md`
* `01-inputs/package_a_activity_3_1_input.md`
* `02-working/package_a_stage_0_intake_summary.md`
* `02-working/package_a_activity_1_1_decision_frame.md`
* `02-working/package_a_activity_1_2_evidence_synthesis.md`
* `02-working/package_a_activity_1_3_breakdown_map.md`
* `02-working/package_a_activity_2_1_direction_review.md`
* `02-working/package_a_activity_3_1_recommendation_draft.md`
* `03-reviews/package_a_stage_0_intake_check.md`
* `03-reviews/package_a_activity_1_1_review.md`
* `03-reviews/package_a_activity_1_2_review.md`
* `03-reviews/package_a_activity_1_3_review.md`
* `03-reviews/package_a_activity_2_1_review.md`
* `03-reviews/package_a_activity_3_1_review.md`
* `04-final/package_a_final_deliverable.md`
* `04-final/package_a_prototype_prompt_pack.md`
* `04-final/package_a_prototype_record.md`

Bootstrap generates the `02-working/` and `03-reviews/` files automatically from the Package A workflow metadata when a live project is started.

## Template design notes

Package A should feel lean in use.

That means:

* Each seeded input file is structured as a short step-based sequence rather than a long questionnaire.
* Earlier validated context should be carried forward by default.
* Only genuinely new or changed input should be captured in each activity.
* Prototype prompts and prototype approval notes should live in their own files so the main final deliverable stays readable.

## Stage 0 intake input template

```md
# Package A - Stage 0 intake input

## Sequence guide
Use this intake as 4 short steps:
1. Client and problem
2. Decision and why now
3. Evidence and stakeholders
4. Boundaries

## Step 1 of 4: Client and problem
### Client / context
[Text]

### Problem area in scope
[Text]

## Step 2 of 4: Decision and urgency
### Decision to support
[Text]

### Why this matters now
[Text]

## Step 3 of 4: Evidence and stakeholders
### Known evidence
[Text]

### Stakeholders or teams involved
* [Stakeholder or team]
* [Stakeholder or team]

## Step 4 of 4: Boundaries
### Combined boundary answer
[One short answer covering both known constraints and anything that should stay out of scope]

### Known constraints
* [Constraint]
* [Constraint]

### Out-of-scope items
* [Item]
* [Item]
```

## Activity 1.1 input template

```md
# Package A - Activity 1.1 input

## Sequence guide
Use this activity as 4 short steps:
1. Workshop setup and business question
2. Users and scope
3. Measures, baseline, and constraints
4. Tensions and open sprint questions

## Carried-forward context from Stage 0
### Current problem area
[Text]

### Current decision to support
[Text]

### Current why-now context
[Text]

### Stakeholder baseline carried forward from Stage 0
* [Stakeholder or team]
* [Stakeholder or team]

### Only note changes if the workshop changed the carried-forward context
[Text]

## Step 1 of 4: Workshop setup and business question
### Workshop participants confirmed from the carried-forward stakeholder baseline
* [Role]
* [Role]

### Additional workshop-specific participants needed
* [Role]
* [Role]

### Business question discussed
[Text]

## Step 2 of 4: Users and scope
### Target users
* [Group]
* [Group]

### In scope
* [Item]
* [Item]

### Out of scope
* [Item]
* [Item]

## Step 3 of 4: Measures and constraints
### Success measures discussed
* [Measure]
* [Measure]

### Known baseline metrics
* [Metric]
* [Metric]

### Constraints raised
* [Constraint]
* [Constraint]

## Step 4 of 4: Tensions and open sprint questions
### Assumptions or disagreements
* [Point]
* [Point]

### Open sprint questions
* [Question]
* [Question]
```

## Activity 1.2 input template

```md
# Package A - Activity 1.2 input

## Sequence guide
Use this activity as 3 short steps:
1. Evidence sources and coverage
2. Strongest signals and supported findings
3. Remaining uncertainty and next validation questions

## Carried-forward context from Activity 1.1
### Selected problem area in scope
[Text]

### Decision this evidence should support
[Text]

### Only note changes if the evidence review changed either of these
[Text]

## Step 1 of 3: Evidence sources and coverage
### Sources reviewed
* [Source]
* [Source]

### Segmentation available
* [Segment or not available]
* [Segment or not available]

## Step 2 of 3: Strongest signals and supported findings
### Strongest signals
1. [Signal]
2. [Signal]
3. [Signal]

### Well supported
* [Point]
* [Point]

### Directional but not yet proven
* [Point]
* [Point]

## Step 3 of 3: Remaining uncertainty
### Still assumption
* [Point]
* [Point]

### Conflicts or gaps
* [Gap or conflict]
* [Gap or conflict]

### Questions to validate next
* [Question]
* [Question]
```

## Activity 1.3 input template

```md
# Package A - Activity 1.3 input

## Sequence guide
Use this activity as 3 short steps:
1. Step in scope, actors, and current actions
2. Touchpoints, systems, and internal implications
3. Friction, biggest breakdowns, and validation gaps

## Carried-forward context from Activity 1.2
### Decision this map should support
[Text]

### Evidence implication to keep in mind
[Text]

## Step 1 of 3: Step in scope and current flow
### Selected step in scope
[Text]

### Actors
* [Actor]
* [Actor]

### Current actions
* [Action]
* [Action]

## Step 2 of 3: Touchpoints and dependencies
### Touchpoints and channels
* [Touchpoint]
* [Touchpoint]

### Systems and dependencies
* [Dependency]
* [Dependency]

### Internal implications
* [Point]
* [Point]

## Step 3 of 3: Breakdown pattern
### Friction points
* [Point]
* [Point]

### Biggest breakdowns
1. [Breakdown]
2. [Breakdown]
3. [Breakdown]

### Why these matter
* [Implication]
* [Implication]

### Validation gaps
* [Gap]
* [Gap]
```

## Activity 2.1 input template

```md
# Package A - Activity 2.1 input

## Sequence guide
Use this activity as 4 short steps:
1. Decision and options
2. Comparison criteria
3. Option notes and tradeoffs
4. Preferred direction and open checks

## Carried-forward context from Activity 1.3
### Problem area in scope
[Text]

### Breakdown pattern to respond to
[Text]

## Step 1 of 4: Decision and options
### Decision this review should support
[Text]

### Options compared
* Option A: [Text]
* Option B: [Text]

## Step 2 of 4: Comparison criteria
### User criteria
* [Criterion]
* [Criterion]

### Business criteria
* [Criterion]
* [Criterion]

### Delivery criteria
* [Criterion]
* [Criterion]

## Step 3 of 4: Option notes and tradeoffs
### Notes on Option A
* [Point]
* [Point]

### Notes on Option B
* [Point]
* [Point]

### Tradeoffs discussed
* [Tradeoff]
* [Tradeoff]

## Step 4 of 4: Preferred direction and open checks
### Preferred direction if one emerged
[Text]

### Risks and dependencies
* [Risk]
* [Risk]

### Open checks
* [Check]
* [Check]
```

## Activity 3.1 input template

```md
# Package A - Activity 3.1 input

## Sequence guide
Use this activity as 4 short steps:
1. Recommendation lock and sponsor notes
2. Scope and measures
3. Risks, validation, and next steps
4. Prototype brief

## Carried-forward context from Activity 2.1
### Preferred direction currently assumed
[Text]

### Problem focus currently assumed
[Text]

### Only note changes if sponsors changed the carried-forward direction or problem focus
[Text]

## Step 1 of 4: Recommendation lock and sponsor notes
### Decision to support
[Text]

### Why this direction is stronger
* [Reason]
* [Reason]

### Final sponsor comments or scope notes
* [Note]
* [Note]

## Step 2 of 4: Scope and measures
### Target users
* [Group]
* [Group]

### Success measures
* [Measure]
* [Measure]

### Build now
* [Item]
* [Item]

### Defer
* [Item]
* [Item]

## Step 3 of 4: Risks, validation, and next steps
### Validate next
* [Question]
* [Question]

### Risks and dependencies
* [Risk]
* [Risk]

### Immediate next steps
* [Action]
* [Action]

## Step 4 of 4: Prototype brief
### Prototype scope
* [Screen or moment]
* [Screen or moment]

### Prototype interactions to show
* [Interaction]
* [Interaction]

### Prototype constraints
* [Constraint]
* [Constraint]

### Optional visual reference screenshots or links
* [Optional screenshot, link, or note]
* [Optional screenshot, link, or note]

### Preferred tool
[Figma Make / Google Stitch / either]
```

## Final deliverable template

```md
# Package A final deliverable

## Executive summary
[Text]

## Decision to support
[Text]

## Recommended direction
[Text]

## Why this direction
* [Reason]
* [Reason]

## Recommended scope
* [Build now]
* [Build now]

## What not to build yet
* [Defer]
* [Defer]

## Target users
* [Group]
* [Group]

## Success criteria and measurement logic
* [Measure]
* [Measure]

## Final journey-step map summary
### Step in scope
[Text]

### Biggest breakdowns
1. [Breakdown]
2. [Breakdown]
3. [Breakdown]

### Why they matter
* [Implication]
* [Implication]

## Clickable prototype
### Prototype objective
[Text]

### Prototype scope summary
* [Screen or moment]
* [Screen or moment]

### Prototype record
See `package_a_prototype_record.md`.

### Prototype prompt pack
See `package_a_prototype_prompt_pack.md`.

## Risks and dependencies
* [Risk]
* [Risk]

## Validate next
* [Question]
* [Question]

## Immediate next steps
* [Action]
* [Action]

## Approval status
[Draft / Ready for review / Approved]
```

## Prototype prompt pack template

```md
# Package A prototype prompt pack

## Canonical prototype brief
[Text]

## Fresh generation prompt - Figma Make
[Text]

## Refinement prompt - Figma Make
[Text]

## Fresh generation prompt - Google Stitch
[Text]

## Refinement prompt - Google Stitch
[Text]

## Prompt notes
* [Note]
* [Note]

## Approval status
[Draft / Ready for review / Approved]
```

## Prototype record template

```md
# Package A prototype record

## Tool used
[Figma Make / Google Stitch / other]

## Prototype link or working file
[Text]

## Approved screenshots or references
* [Screenshot, URL, or note]
* [Screenshot, URL, or note]

## Iteration history
1. [Fresh generation or revision]
2. [Refinement round]

## Review outcome
[Text]

## Remaining polish notes
* [Note]
* [Note]

## Approval status
[Draft / Ready for review / Approved]
```
