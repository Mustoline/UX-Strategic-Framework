# UX Strategic Framework

This repository packages a strategic UX and service design offer that can be sold and run upstream of delivery.

The goal is not to produce UX activity for its own sake. The goal is to help a client define the right problem, reduce delivery risk, improve prioritization, and expose the service and operational changes required behind the interface before major build work starts.

## What This Repository Contains

The framework is organized first by document purpose and then by language.

```text
UX-Strategic-Framework/
  Packages/
    English/
    Danish/
  Sales materials/
    English/
    Danish/
  Projects/
    Templates/
    bootstrap_project.py
    generate_next_activity_prep.py
    sync_project_status.py
  skills/
```

## Start Here

If you are new to the repository, these are the best entry points:

* [Packages/English/strategic_ux_packages.md](Packages/English/strategic_ux_packages.md): package portfolio, positioning logic, and package-selection rules
* [Sales materials/English/upstream_discovery_positioning.md](Sales%20materials/English/upstream_discovery_positioning.md): why the offer belongs upstream
* [Sales materials/English/discovery_sales_playbook.md](Sales%20materials/English/discovery_sales_playbook.md): qualification, objections, proposal language, and handoff logic
* [Sales materials/English/executive_offer_one_pager.md](Sales%20materials/English/executive_offer_one_pager.md): compressed executive-facing summary
* [Projects/README.md](Projects/README.md): how live engagements should be created and managed inside the repository

## Repository Structure

### `Packages/`

The reusable package definitions for the offer.

This is where the portfolio logic lives, including:

* package positioning
* core activities
* facilitator guides
* AI process guides
* internal operating references
* prototype prompt-pack templates

### `Sales materials/`

The commercial layer around the package offer.

This includes:

* positioning documents
* the discovery sales playbook
* executive-facing one-pagers
* proposal templates

### `Projects/`

The live-project operating system.

Use this area when a real engagement starts. It contains:

* project setup guidance
* reusable templates
* scripts for bootstrapping new projects
* scripts for syncing project status and generating next-activity prep

### `skills/`

The internal skill library used to support package activities, synthesis steps, and strategy artifact production.

See [skills/README.md](skills/README.md) for the full skill catalog and a short summary of each skill's purpose.

## How The Offer Is Structured

The client-facing offer is built as three upstream discovery packages:

* **Package A: Discovery sprint** for one bounded problem that needs a fast go or no-go and scope decision
* **Package B: Service concept definition** for defining the right concept, journey, and service changes before delivery scope is locked
* **Package C: Strategic service redesign** for broader cross-team or cross-system redesign work that needs an investment and sequencing basis

Each package is meant to run as a staged decision process with:

* focused activities
* structured synthesis between activities
* review checkpoints before the next step moves forward

## Language Model

English and Danish source materials are maintained in parallel:

* `Packages/English/` and `Packages/Danish/`
* `Sales materials/English/` and `Sales materials/Danish/`

The detailed files should stay aligned in logic, naming, and commercial framing across both languages.

## Running A Live Project

When a real client project starts, create it inside `Projects/` rather than writing project artifacts into the shared source folders.

Preferred setup path:

```bash
python3 Projects/bootstrap_project.py --project-name "Client Name" --package A --language english
```

That creates the standard project folder structure, seeds the relevant files, and prepares the project for later workflow sync.

## Working Principle

This is a strategy repository, not a software product repository.

The standard for new material is:

* direct, commercially grounded language
* business value and risk-reduction logic
* concrete activities, outputs, and next decisions
* a service-design lens, not only an interface-design lens

## Status

The repository is now structured as a reusable operating system for upstream discovery work:

* reusable package definitions
* reusable sales materials
* reusable project templates and automation scripts
* no sample dry-run deliverables in the final product surface
