# Intern kortlaegning af aktiviteter, skills og agentmoenstre

Intern note: Dette dokument kortlaegger pakkeaktiviteterne til det interne skill-bibliotek og til den anbefalede agentlogik bag kulissen. Det er ikke kundevendt og maa ikke refereres i tilbud, salgsmateriale eller ledelsesopsummeringer.

## Formaal

Brug denne kortlaegning til at holde pakkeoperativsystemet og `/skills`-biblioteket aligned.

Reglen er:

* `Packages/` definerer pakkelogikken, stage gates og den kundesynlige sekvens
* `Projects/Templates/` definerer projektfilerne og handoffstrukturen
* `/skills` definerer hvordan den interne analyse, faciliteringsstoette, syntese og review skal udfoeres
* Specialiserede agenter er valgfri intern eksekveringsstoette og maa ikke skabe et andet synligt workflow for kunden

## Forklaring af agentmoenstre

* `Kun main thread`: Aktiviteten holdes i hovedflowet. En separat specialistagent er ikke indsatsen vaerd.
* `Main thread + specialist worker`: Main thread ejer stage gate og brugerinteraktion, men en afgraenset worker kan syntetisere eller strukturere outputtet.
* `Main thread + specialist worker + valgfri review-sidecar`: Brug en specialist worker til hovedsyntesen og tilfoej kun et reviewspor, naar outputtet er taet paa klientklart niveau eller er strategisk foelsomt.

## Delte helper-skills

| Helper-skill | Intern rolle |
| --- | --- |
| `artifact-writer` | Skriver rene kundevendte eller interne artefakter ud fra valideret pakkeoutput. |
| `evidence-ingest` | Normaliserer blandet evidens foer syntesetunge aktiviteter. |
| `workshop-design-kit` | Leverer agenda, faciliteringslogik og notefangst til workshopaktiviteter. |
| `map-structure-generator` | Leverer stillads til rejsekort, ecosystem maps og service blueprints. |
| `ux-strategy-reviewer` | Sidste kvalitetstjek af forretningstone, klarhed og pakkekomplethed. |
| `discovery-interview` | Valgfri stoette naar et trin stadig er for vagt og har brug for dybere guidet afklaring. |

## Kortlaegning for Pakke A

| Trin | Primaer skill | Understoettende skills | Agentmoenster | Forventet inputfil | Forventet arbejdsoutput | Forventet review eller endelig gate | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Trin 0 intake` | Ingen dedikeret specialistskill endnu | `discovery-interview`, `artifact-writer` | Kun main thread | `01-inputs/package_a_stage_0_intake_input.md` | `02-working/package_a_stage_0_intake_summary.md` | `03-reviews/package_a_stage_0_intake_check.md` | Kandidat til fremtidig skill: Package A intake og framing. |
| `Aktivitet 1.1` | `sponsor-workshop-facilitator` | `workshop-design-kit`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_1_1_input.md` | `02-working/package_a_activity_1_1_decision_frame.md` | `03-reviews/package_a_activity_1_1_review.md` | Main thread koerer live workshop-handoffet. Worker bruges bedst efter noterne er fanget. |
| `Aktivitet 1.2` | `evidence-baseline-reviewer` | `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_1_2_input.md` | `02-working/package_a_activity_1_2_evidence_synthesis.md` | `03-reviews/package_a_activity_1_2_review.md` | Dette er det tydeligste eksempel paa et afgraenset specialistsyntesetrin. |
| `Aktivitet 1.3` | `journey-step-mapper` | `map-structure-generator`, `workshop-design-kit`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_1_3_input.md` | `02-working/package_a_activity_1_3_breakdown_map.md` | `03-reviews/package_a_activity_1_3_review.md` | Brug workeren efter noterne findes, ikke midt i live fangst. |
| `Aktivitet 2.1` | `option-review-facilitator` | `workshop-design-kit`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_a_activity_2_1_input.md` | `02-working/package_a_activity_2_1_direction_review.md` | `03-reviews/package_a_activity_2_1_review.md` | God worker-kandidat fordi det er et afgraenset sammenligningsproblem med eksplicitte kriterier. |
| `Aktivitet 3.1` | `recommendation-packager` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `01-inputs/package_a_activity_3_1_input.md` | `02-working/package_a_activity_3_1_recommendation_draft.md` | `03-reviews/package_a_activity_3_1_review.md` | Brug kun review-sidecar naar anbefalingen er taet paa kundeklart niveau. |
| `Endelig leverance` | `recommendation-packager` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `04-final/package_a_final_deliverable.md` plus prototypefiler | `04-final/package_a_final_deliverable.md`, `04-final/package_a_prototype_prompt_pack.md`, `04-final/package_a_prototype_record.md` | Endelig kundegodkendelse | Hold hovedanbefaling, prompt pack og prototype record adskilt. |

## Kortlaegning for Pakke B

| Trin | Primaer skill | Understoettende skills | Agentmoenster | Forventet inputfil | Forventet arbejdsoutput | Forventet review eller endelig gate | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Trin 0 intake` | Ingen dedikeret specialistskill endnu | `discovery-interview`, `artifact-writer` | Kun main thread | `01-inputs/package_b_stage_0_intake_input.md` | `02-working/package_b_stage_0_intake_summary.md` | `03-reviews/package_b_stage_0_intake_check.md` | Kandidat til fremtidig skill: Package B intake og opportunity framing. |
| `Aktivitet 1.1` | `scoping-workshop-facilitator` | `workshop-design-kit`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_1_1_input.md` | `02-working/package_b_activity_1_1_scope_summary.md` | `03-reviews/package_b_activity_1_1_review.md` | Main thread haandterer den live scopingworkshop. |
| `Aktivitet 1.2` | `user-research-runner` | `evidence-ingest`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_1_2_input.md` | `02-working/package_b_activity_1_2_insight_summary.md` | `03-reviews/package_b_activity_1_2_review.md` | Specialist worker er nyttig naar interviewnoter og evidens er samlet. |
| `Aktivitet 2.1` | `current-journey-synthesizer` | `map-structure-generator`, `artifact-writer`, `evidence-ingest`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_2_1_input.md` | `02-working/package_b_activity_2_1_current_state_journey_summary.md` | `03-reviews/package_b_activity_2_1_review.md` | Staerk kandidat til specialistsyntese fordi outputtet baade har map-logik og opportunity framing. |
| `Aktivitet 3.1` | `future-state-concept-facilitator` | `workshop-design-kit`, `map-structure-generator`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_b_activity_3_1_input.md` | `02-working/package_b_activity_3_1_future_state_concept_summary.md` | `03-reviews/package_b_activity_3_1_review.md` | Main thread ejer workshoppen. Workeren hjaelper med at pakke konceptet og serviceaendringerne. |
| `Aktivitet 4.1` | `prototype-and-prioritization-facilitator` | `workshop-design-kit`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `01-inputs/package_b_activity_4_1_input.md` | `02-working/package_b_activity_4_1_prioritization_and_prototype_summary.md` | `03-reviews/package_b_activity_4_1_review.md` | Brug review-sidecar naar den endelige anbefaling er paa vej mod klientklart niveau. |
| `Endelig leverance` | `prototype-and-prioritization-facilitator` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `04-final/package_b_final_deliverable.md` plus prototypefiler | `04-final/package_b_final_deliverable.md`, `04-final/package_b_prototype_prompt_pack.md`, `04-final/package_b_prototype_record.md` | Endelig kundegodkendelse | Den endelige paketering skal holde prototypeartefakterne adskilt fra hovedanbefalingen. |

## Kortlaegning for Pakke C

| Trin | Primaer skill | Understoettende skills | Agentmoenster | Forventet inputfil | Forventet arbejdsoutput | Forventet review eller endelig gate | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Trin 0 intake` | Ingen dedikeret specialistskill endnu | `discovery-interview`, `artifact-writer` | Kun main thread | `01-inputs/package_c_stage_0_intake_input.md` | `02-working/package_c_stage_0_intake_summary.md` | `03-reviews/package_c_stage_0_intake_check.md` | Kandidat til fremtidig skill: Package C strategisk intake og boundary framing. |
| `Aktivitet 1.1` | `executive-and-service-owner-interviewer` | `evidence-ingest`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_1_1_input.md` | `02-working/package_c_activity_1_1_strategic_framing_summary.md` | `03-reviews/package_c_activity_1_1_review.md` | Main thread ejer interviewstroemmen og stage gaten. |
| `Aktivitet 1.2` | `ecosystem-workshop-facilitator` | `workshop-design-kit`, `map-structure-generator`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_1_2_input.md` | `02-working/package_c_activity_1_2_service_scope_summary.md` | `03-reviews/package_c_activity_1_2_review.md` | God placering for struktureret syntese efter en taet tvaerfaglig workshop. |
| `Aktivitet 2.1` | `contextual-fieldwork-runner` | `evidence-ingest`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_2_1_input.md` | `02-working/package_c_activity_2_1_operational_observation_summary.md` | `03-reviews/package_c_activity_2_1_review.md` | Staerk worker-kandidat fordi feltarbejdssyntesen er evidenstung og afgraenset. |
| `Aktivitet 2.2` | `service-blueprint-builder` | `map-structure-generator`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker | `01-inputs/package_c_activity_2_2_input.md` | `02-working/package_c_activity_2_2_blueprint_summary.md` | `03-reviews/package_c_activity_2_2_review.md` | Blueprint-konstruktion er en klar specialistaktivitet og boer ikke improviseres i main thread. |
| `Aktivitet 3.1` | `future-state-service-model-and-validation` | `workshop-design-kit`, `map-structure-generator`, `discovery-interview`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `01-inputs/package_c_activity_3_1_input.md` | `02-working/package_c_activity_3_1_future_state_service_model_summary.md` | `03-reviews/package_c_activity_3_1_review.md` | Tilfoej kun review-sidecar naar target-state-modellen er taet paa ekstern playback. |
| `Aktivitet 4.1` | `roadmap-and-business-case-framer` | `workshop-design-kit`, `evidence-ingest`, `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `01-inputs/package_c_activity_4_1_input.md` | `02-working/package_c_activity_4_1_roadmap_and_business_case_summary.md` | `03-reviews/package_c_activity_4_1_review.md` | Review-sidecar er saerligt nyttig naar ROI-logikken skal bruges i ledelsesdialog. |
| `Endelig leverance` | `roadmap-and-business-case-framer` | `artifact-writer`, `ux-strategy-reviewer` | Main thread + specialist worker + valgfri review-sidecar | `04-final/package_c_final_deliverable.md` plus valgfrie prototypefiler | `04-final/package_c_final_deliverable.md`, valgfri `04-final/package_c_prototype_prompt_pack.md`, valgfri `04-final/package_c_prototype_record.md` | Endelig kundegodkendelse | Prototypestoette er stadig valgfri og maa kun daekke ét udvalgt hoejrisiko-udsnit af rejsen. |

## Driftsregler til senere integration

Naar denne kortlaegning bruges operationelt:

* Main package flow skal stadig eje brugerinteraktion, validation gate og projektstatus-sync.
* Skills skal drive det interne arbejde bag hver aktivitet og ikke erstatte pakkesekvensen.
* Specialiserede agenter skal kun bruges, naar de reelt forbedrer kvaliteten af en afgraenset syntese.
* Review-sidecars skal bruges selektivt taet paa klientklare outputs og ikke som standard paa alle aktiviteter.
* Hvis en skill og pakkedokumenterne paa noget tidspunkt siger noget forskelligt, skal skillen eller pakken opdateres, saa kortlaegningen igen er konsistent.
