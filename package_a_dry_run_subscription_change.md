# Package A dry run: Self-service subscription change flow

Internal note: This is an internal dry run showing how the current Package A skill set can work together on one realistic scenario. The example is illustrative, not client-specific. It is written to test whether the workflow produces a clear decision frame, a practical recommendation, and tangible next steps.

## Scenario

**Client type:** Telecom provider with a self-service customer portal

**Problem area:** Existing customers try to change their mobile subscription online, but a large share drop out during the plan comparison and eligibility step and then contact support or visit a store instead

**Decision to support:** Should the client invest now in improving the self-service subscription change step, and if yes, what should move into delivery first?

**Why this fits Package A:** The problem is bounded to one journey step, the client needs a near-term go or no-go and scope decision, and the team already has some evidence but not enough shared clarity to move cleanly into delivery

## Activity 1.1 using `sponsor-workshop-facilitator`

### Workshop objective

Agree the business question, target users, success measures, and main constraints for the discovery sprint.

### Draft workshop output

**Business question:** How can we reduce drop-off and support load in the self-service subscription change step without taking on avoidable delivery risk?

**Decision to support:** Approve or reject a near-term improvement to the subscription change step and define the scope that should move into delivery first.

**Target users:**

* Existing private mobile customers who want to upgrade or downgrade their subscription
* Secondary user group: front-line support and retail staff who currently help customers complete failed digital attempts

**Success measures:**

* Reduce drop-off in the selected step from `42%` to below `25%`
* Reduce support contacts related to subscription change by `20%`
* Increase digital completion rate for subscription change requests
* Reduce the average time needed to complete a change request

**Main constraints:**

* The billing platform has a fixed release window in 10 weeks
* The legacy eligibility engine cannot be replaced in this release
* Legal disclosures on price and contract implications must remain visible
* Call-center capacity is already under pressure, so the solution should not create a large new assisted-service burden

**Open sprint questions:**

* Is the main failure point clarity, trust, or actual eligibility logic?
* How much of the problem can be solved within the current billing and eligibility setup?
* Which part of the step needs to become clearer before delivery investment is justified?

## Activity 1.2 using `evidence-baseline-reviewer`

### Evidence objective

Review what is already known about the subscription change step before the team debates solutions.

### Sources reviewed

* Portal analytics from the last 90 days
* Top support topics related to plan change
* Retail and sales-team input
* Prior usability research on self-service account changes

### Strongest signals

* Analytics show `42%` drop-off at the plan comparison and eligibility stage, with the highest abandonment on mobile devices
* Support contacts repeatedly mention unclear eligibility messages, unclear fees, and confusion about whether a change takes effect immediately
* Retail staff report that customers often arrive after failing online and need a simple explanation of plan differences and contract implications
* Prior research suggests customers want a plain-language explanation of why a plan is or is not available and a clearer view of price impact before committing

### Known versus assumed

**Well supported:**

* The current plan comparison and eligibility step is the main friction point in the flow
* Customers do not understand why some plans appear unavailable
* Price and contract implications are not clear enough at the point of decision

**Directional but not yet proven:**

* A clearer comparison and explanation layer would improve completion significantly
* Better digital clarity would reduce support demand, not just shift it

**Still assumption:**

* A callback or assisted-service path would outperform a better self-service flow for this step
* Most failed attempts are caused by interface clarity rather than by policy or product complexity

**Conflicts or gaps:**

* Some internal stakeholders believe the issue is mainly content and UI, while retail teams think policy exceptions are the bigger cause
* The current data does not show whether customers who abandon eventually complete in another channel

### Implication for the sprint

The sprint should focus on clarifying the decision moment inside the subscription change step, not on redesigning the entire account area. It should also test whether clearer comparison, clearer eligibility explanation, and clearer price impact can address the main friction within current technical constraints.

## Activity 1.3 using `journey-step-mapper`

### Mapping objective

Map the selected subscription change step to show where users and staff lose time, confidence, or momentum today.

### Current-state view

**Selected step in scope:** Existing customer compares alternative subscriptions and attempts to confirm a change

**Actors involved:**

* Existing mobile customer
* Customer support agent
* Retail-store staff member
* Billing and eligibility systems

**Touchpoints and dependencies:**

* Customer portal
* Eligibility engine
* Billing platform
* Legal disclosure content
* Support and retail channels when the user fails online

### Biggest breakdowns

1. **Eligibility explanation appears too late and with too little context**
   Why it matters: Customers reach the point of decision before understanding why some plans are unavailable, which drives drop-off and low trust.

2. **Price impact is split across screens**
   Why it matters: Customers struggle to understand monthly cost change, one-off fees, and contract implications in one view.

3. **Current versus new plan comparison is weak**
   Why it matters: Users cannot quickly judge whether the change is worth it, which slows the decision and increases uncertainty.

4. **Support handoff loses context**
   Why it matters: When the user abandons and contacts support, the next channel starts from zero and absorbs avoidable effort.

5. **Technical dependency on legacy eligibility logic constrains the experience**
   Why it matters: Some friction comes from real backend rules, so the sprint must separate what can be improved in the interface from what cannot be changed now.

### Implication for the sprint

The next decision should focus on improving clarity and comparison within the current step, while keeping the delivery scope tight enough to fit the release window and system constraints.

## Activity 2.1 using `option-review-facilitator`

### Review objective

Compare two practical directions for the selected subscription change step and narrow to one preferred direction.

### Options compared

**Option A:** Improve the current self-service flow with clearer plan comparison, earlier eligibility explanation, and clearer price-impact visibility

**Option B:** Introduce a hybrid path with simplified self-service plus assisted callback for customers who hit eligibility or comparison uncertainty

### Comparison criteria

* User clarity and confidence
* Business impact on completion and support reduction
* Delivery feasibility inside the current release window
* Risk and dependency exposure

### Tradeoff summary

**Option A strengths:**

* Directly addresses the main friction in the selected step
* Fits the bounded Package A problem more cleanly
* More realistic within current technical and operational constraints

**Option A tradeoffs:**

* Still limited by the legacy eligibility engine
* May not solve edge cases that genuinely need human support

**Option B strengths:**

* Could help customers who need reassurance or exception handling
* Creates a clear assisted path for more complex cases

**Option B tradeoffs:**

* Adds operational complexity immediately
* Risks increasing service load before the self-service step is improved
* Requires tighter channel coordination than the current release window likely allows

### Preferred direction

Recommend **Option A** as the near-term direction.

### Why this direction is stronger

* It responds directly to the strongest evidence and the biggest breakdowns in the mapped step
* It keeps the scope tight enough for a near-term delivery decision
* It reduces avoidable service load without making assisted service the default answer

### Open checks before final recommendation

* Confirm whether clearer eligibility explanation materially improves confidence in quick concept testing
* Confirm which legal and billing constraints affect the final comparison view

## Activity 3.1 using `recommendation-packager`

### Recommendation document

**Decision to support:** Approve a near-term improvement to the self-service subscription change step and move a bounded scope into delivery.

**Recommended direction:** Improve the current self-service comparison and eligibility step rather than adding a broader assisted-service model in this release.

**Why this direction:**

* It addresses the strongest evidence-backed friction points in the current step
* It gives the client a clearer path to reduce drop-off and support load within current constraints
* It avoids expanding scope into a larger service-model change before the bounded self-service problem is tested properly

**Target users and success measures:**

* Existing private mobile customers changing subscription
* Support and retail staff who handle failed digital attempts
* Success will be judged through lower drop-off, fewer support contacts, stronger digital completion, and faster time to complete

**What to build next:**

* A clearer current-versus-new plan comparison view
* Earlier and clearer explanation of plan eligibility
* A single clearer summary of monthly cost change, one-off fees, and contract implications
* Better carry-over context if the user still needs support

**What to defer or not build yet:**

* A callback-led assisted-service path as the default next step
* Broader redesign of the full account-management area
* Replacement of the eligibility engine

### Concept brief

**Purpose of the concept:** Make the chosen direction tangible enough for sponsor review and early delivery planning.

**What the concept needs to show:**

* One screen that compares current and alternative plans clearly
* One decision moment that explains eligibility in plain language
* One confirmation view that makes price and contract implications explicit

**What the concept should help clarify:**

* Whether the clearer explanation reduces hesitation
* Whether users can understand cost change and implications without leaving the flow
* Whether the concept is narrow enough to move into delivery in the next release window

### Build now, defer, validate

**Build now:**

* Comparison view
* Eligibility explanation layer
* Clear price and implication summary

**Defer:**

* Assisted callback path as a standard route
* Larger account-area redesign

**Validate next:**

* Whether edge cases still need assisted handling after the clarity improvements
* Whether support-context carry-over is feasible in the current stack

### Risks, dependencies, and next steps

**Risks and dependencies:**

* The eligibility engine may still create outcomes that are hard to explain elegantly
* Legal wording may weaken clarity if not actively simplified
* Support-context carry-over may depend on CRM and portal integration work

**Immediate next steps:**

* Build a simple concept view or lightweight clickable prototype of the comparison and eligibility step
* Validate comprehension quickly with a small number of representative customers or front-line staff
* Confirm delivery implications with product, billing, and legal stakeholders before implementation starts

## What this dry run shows

This Package A example shows that the current skill set can now support a full discovery sprint flow:

* The sponsor workshop frames the business question and scope
* The evidence baseline prevents the team from debating on instinct
* The journey-step map isolates the real breakdowns in one bounded step
* The option review turns findings into a grounded direction choice
* The recommendation package converts that choice into a practical next-step decision

## Next recommended move

After pressure-testing this dry run, the next build step should be **Package B**, starting with `scoping-workshop-facilitator`.
