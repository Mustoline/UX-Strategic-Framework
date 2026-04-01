# Package C dry run: Move-home service redesign

Internal note: This is an internal dry run showing how the current Package C skill set can work together on one realistic scenario. The example is illustrative, not client-specific. It is written to test whether the workflow produces a clear strategic framing, an evidence-backed target-state service model, and a practical roadmap with investment logic.

## Scenario

**Client type:** Regional utility provider serving residential electricity and heat customers

**Problem area:** Customers moving into or out of a home face a fragmented move-home service spread across website forms, the contact center, billing, CRM, meter-data systems, and operational teams. The result is duplicate effort, missed handoffs, delayed confirmations, billing errors, and avoidable complaints at a moment when churn risk is high.

**Decision to support:** Should the utility invest in a broader move-home service redesign, and if yes, how should the work be sequenced across digital channels, operations, billing, and ownership?

**Why this fits Package C:** The problem crosses departments, channels, and systems, requires a basis for investment and sequencing, and depends on service-model and organizational change rather than interface improvements alone.

## Activity 1.1 using `executive-and-service-owner-interviewer`

### Interview objective

Clarify the business case, strategic priorities, service pressures, and investment questions surrounding the move-home service.

### Strategic interview synthesis

**Main service pressures raised:**

* Customers often start online but still call because they do not trust that the move request is complete
* Billing corrections and move-date disputes create costly rework after the fact
* Ownership of the end-to-end move-home service is fragmented across digital, contact center, billing, and operations
* Complaints rise when confirmation is late or the first bill is wrong

**Value at stake:**

* Fewer avoidable contacts during move-home periods
* Lower correction work in billing and operations
* Better customer retention at a high-risk moment in the relationship
* Less reputational damage from move-in and final-bill complaints

**Investment questions:**

* Does the utility need one cross-channel move-home case rather than separate handoffs between teams?
* Which system and ownership changes matter most before a broader transformation is approved?
* What should be sequenced first to reduce service failure without waiting for a full platform replacement?

### Implication for the next step

The ecosystem workshop should focus on the real cross-functional service boundary, not just the website flow.

## Activity 1.2 using `ecosystem-workshop-facilitator`

### Workshop objective

Agree the service scope, map the ecosystem around the move-home journey, and define the critical service moments for later fieldwork.

### Draft workshop output

**Departments, systems, and actors in scope:**

* Digital product and website team
* Contact center
* Billing operations
* CRM team
* Meter-data and settlement systems
* Operational back-office handling exceptions
* Customers and, in some cases, landlords or property administrators

**Agreed service scope:**

* Residential move-in and move-out journeys
* Address verification, move date capture, meter-read handling, confirmation, first bill, and final bill

**Context to keep visible but not study in depth:**

* Commercial-property move cases
* Debt-collection edge cases
* Long-term tariff redesign

**Critical service moments to study:**

1. Customer submits or starts a move request
2. Address and meter details are verified
3. Exceptions or missing information are handled
4. Start or stop confirmation is issued
5. First or final bill is produced

### Implication for later work

The fieldwork should follow both the customer-facing and operational sides of those moments, not only the digital form flow.

## Activity 2.1 using `contextual-fieldwork-runner`

### Fieldwork objective

Study how the move-home service works in practice across customers, contact-center staff, billing teams, and operational support functions.

### Sessions represented

* Customers who recently moved home
* Contact-center agents handling move-home calls
* Billing specialists resolving move-date and bill disputes
* Operational staff handling meter or account exceptions
* Digital-service owners reviewing service data and failure cases

### Repeated patterns observed

* Agents re-enter information already submitted online because the first channel does not create a usable shared case
* Customers are unsure whether the request is complete and call to seek confirmation
* Billing teams manually correct move dates, meter reads, or account links after incomplete handoffs
* Exception handling relies on informal spreadsheet tracking and manual follow-up
* Ownership for unresolved cases drifts between contact center, billing, and operations

### Hidden effort and ownership gaps

* Contact-center agents manually reconstruct context from multiple systems
* Billing specialists perform exception triage not visible in the formal process
* Customers compensate for system uncertainty by collecting extra documents or phoning repeatedly
* No single team is clearly responsible for the full move-home experience once an exception appears

### Implication for blueprinting

The current-state service blueprint needs to show the invisible support work, duplicate entry, and exception handling that keep the service functioning today.

## Activity 2.2 using `service-blueprint-builder`

### Blueprint objective

Build a current-state service blueprint that exposes how the move-home service actually works across front-stage and back-stage layers.

### Current-state blueprint summary

**Front-stage interactions:**

* Customer starts a move request online or through the contact center
* Customer provides address, dates, and meter information
* Customer waits for confirmation or follow-up
* Customer receives first or final bill and may dispute it

**Back-stage and support layers:**

* CRM records and contact-center notes
* Billing setup and correction steps
* Meter-data verification
* Operational exception handling and manual follow-up
* Email or SMS confirmation processes

### Main hotspots

1. **Duplicate entry across channels**
   Why it matters: The same move details are captured multiple times, adding effort and introducing error risk.

2. **Weak exception visibility**
   Why it matters: Once something breaks, ownership becomes unclear and the customer loses confidence quickly.

3. **Confirmation timing is unreliable**
   Why it matters: Customers call to check whether the request is complete, which raises service load and uncertainty.

4. **Billing correction work is hidden and expensive**
   Why it matters: Operational teams absorb significant manual effort that is invisible in the customer-facing flow.

5. **The service model leaks value at a churn-sensitive moment**
   Why it matters: Poor move-home experiences damage trust when the customer relationship is most vulnerable.

### Implication for target-state work

The future-state model should not only improve digital intake. It needs a clearer cross-channel case flow, better exception ownership, and a stronger confirmation and billing handoff model.

## Activity 3.1 using `future-state-service-model-and-validation`

### Target-state objective

Define a future-state move-home service model and test whether it is understandable, workable, and credible for customers and internal teams.

### Target-state service model summary

* Create one move-home case that persists across digital and assisted channels
* Give customers a clearer progress view showing what is complete, what is missing, and what happens next
* Introduce clearer exception routing so incomplete or unusual cases do not disappear between teams
* Provide agents and billing teams with a shared service timeline rather than fragmented system notes
* Trigger clearer confirmation messages and milestone updates during the journey

### Validation participants

* Customers who recently moved
* Contact-center staff
* Billing specialists
* Operational support staff

### Signals that the model held up

* Customers strongly valued a visible progress and confirmation view
* Contact-center staff saw clear value in a shared move-home case and timeline
* Billing specialists believed earlier exception visibility would reduce correction work

### Remaining friction and feasibility signals

* Internal teams questioned how quickly a shared case view could be created across legacy systems
* Some exception types still require manual operational judgment
* Customers wanted more explicit reassurance about what happens if the meter reading is missing or disputed

### Refinements made

* Added a clearer exception path rather than assuming all cases can stay in a linear self-service flow
* Strengthened the role of milestone confirmations and fallback guidance
* Clarified that the first release should improve cross-channel visibility before deeper automation

## Activity 4.1 using `roadmap-and-business-case-framer`

### Roadmap objective

Turn the validated move-home service model into a phased roadmap, change summary, and credible ROI hypothesis.

### Phased roadmap

**Now:**

* Create one clearer move-home intake and confirmation flow
* Introduce a shared move-home case identifier across channels
* Improve confirmation content and progress visibility

**Next:**

* Build a shared internal view of move-home case status for contact center and billing teams
* Improve exception routing and ownership rules
* Tighten handoff logic between billing, CRM, and operational support

**Later:**

* Expand automation for meter-read and exception handling where viable
* Improve landlord or partner integration for relevant cases
* Broaden the service redesign into adjacent onboarding and retention touchpoints

### Dependencies and change implications

**Dependencies:**

* CRM and billing integration
* Agreement on cross-functional service ownership
* Governance for exception handling and escalation

**Operating-model implications:**

* A named end-to-end move-home service owner is needed
* Contact-center, billing, and operations need clearer rules for who owns exceptions at each stage
* Performance measures should shift from team-local tasks to end-to-end move completion and correction reduction

### ROI hypothesis summary

**Most credible value areas:**

* Fewer avoidable move-home contact-center calls
* Reduced billing correction effort and dispute handling
* Faster completion and confirmation for customers
* Lower complaint volume and lower churn risk during move-home periods

**Strongest supporting signals:**

* Fieldwork shows repeated duplicate entry, manual correction, and contact-center clarification work
* Validation shows customers and staff both value clearer confirmation and shared case visibility
* The current-state blueprint shows multiple hotspots where time, effort, and ownership confusion accumulate

**What remains directional:**

* Exact savings from reduced correction work
* Longer-term retention impact
* The speed at which system integration can be delivered

### Final recommendation

Approve a phased redesign focused first on shared case visibility, clearer confirmation, and better exception ownership, rather than attempting a one-step end-state transformation. The move-home service now has a credible investment case, but the roadmap should sequence service-model improvements before broader automation ambitions.

## What this dry run shows

This Package C example shows that the current skill set can now support a full strategic service redesign flow:

* The executive and service-owner interviews create the investment and risk framing
* The ecosystem workshop defines the real service boundary and study focus
* The fieldwork exposes how the service works in practice across teams and systems
* The current-state blueprint makes hidden effort, delay, duplication, and ownership gaps visible
* The future-state model and validation step pressure-test the proposed direction before investment is sequenced
* The roadmap and business-case step converts that direction into a phased change path and credible ROI hypothesis
