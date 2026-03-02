# Crypto Portfolio Tracker (CPT)

## Operator Documentation

**Version:** v1.0.0\
**Status:** Non-Authoritative Documentation Seed\
**Date:** 2026-03-02

------------------------------------------------------------------------

# Purpose

This chat documents the practical operation of the Crypto Portfolio
Tracker (CPT).

It explains:

-   Tooling
-   CLI usage
-   Folder structure
-   Workflow execution
-   Snapshot generation
-   Validation procedures
-   Reporting exports

This documentation describes how CPT is used.

It does not define governance.

------------------------------------------------------------------------

# Scope

Operator Documentation may include:

-   Local development setup
-   CLI command patterns
-   Environment variable configuration
-   Example workflows
-   Snapshot generation examples
-   Reporting export instructions
-   Validation tooling usage
-   Schema validation examples
-   Git workflow guidance
-   Deterministic rebuild instructions

------------------------------------------------------------------------

# Non-Scope

This documentation does NOT:

-   Define constitutional standards
-   Modify governance rules
-   Store operational prompts
-   Override the Constitutional Charter
-   Store binary artifacts
-   Act as a registry
-   Interpret tax law
-   Modify snapshot history

If documentation conflicts with the Constitution:

The Constitution prevails.

------------------------------------------------------------------------

# Separation of Concerns

  Layer                       Authority
  --------------------------- ---------------------------
  Constitutional Archive      Governance
  Master Prompt Library       Operational Prompts
  Operator Documentation      Usage & Tooling Reference
  Local Git Repo              Implementation
  Drift Detection Workspace   Architectural Comparison

------------------------------------------------------------------------

# Recommended Local Folder Structure

crypto-portfolio-tracker/ │ ├── governance/ │ ├── constitutional/ │ ├──
master-prompt-library/ │ ├── operator-documentation/ │ └──
drift-workspace/ │ ├── data/ │ ├── raw/ │ ├── normalized/ │ └── pricing/
│ ├── snapshots/ │ ├── reports/ │ ├── src/ │ ├── ingestion/ │ ├──
normalization/ │ ├── pricing/ │ ├── valuation/ │ ├── tax/ │ └──
reporting/ │ └── cli/

------------------------------------------------------------------------

# CLI Execution Model (Example Pattern)

cpt_run.py ingest --wallet
```{=html}
<address>
```
--chain `<chain>`{=html}

cpt_run.py normalize --date `<YYYY-MM-DD>`{=html}

cpt_run.py price --date `<YYYY-MM-DD>`{=html}

cpt_run.py calculate --date `<YYYY-MM-DD>`{=html}

cpt_run.py snapshot --date `<YYYY-MM-DD>`{=html}

cpt_run.py report --tax-year `<YYYY>`{=html}

Each command must:

-   Declare explicit input parameters
-   Produce deterministic outputs
-   Log version metadata
-   Preserve raw inputs

------------------------------------------------------------------------

# Snapshot Workflow Example

1️⃣ Ingest raw transactions\
2️⃣ Normalize transactions\
3️⃣ Apply pricing data\
4️⃣ Calculate portfolio state\
5️⃣ Run tax computation\
6️⃣ Generate immutable snapshot\
7️⃣ Register snapshot hash

Snapshots must include:

-   Engine versions\
-   Pricing source\
-   Tax method\
-   Timestamp\
-   Input hash

------------------------------------------------------------------------

# Validation Model

CPT validation may include:

-   Schema validation
-   Snapshot integrity verification
-   Hash verification
-   Version compatibility checks
-   Drift comparison before upgrade

All validation logic must be versioned.

------------------------------------------------------------------------

# Reporting Guidance

Reports may include:

-   Portfolio valuation summary
-   Asset allocation breakdown
-   LP exposure summary
-   Realized gains report
-   Unrealized gains report
-   Tax-year summary

Reports must reference:

-   Snapshot ID
-   Engine versions
-   Pricing source
-   Tax method

Reports are outputs --- not governance artifacts.

------------------------------------------------------------------------

# Documentation Evolution Rules

-   Documentation may evolve over time.
-   Changes here do not require constitutional version bump.
-   If documentation introduces architectural change, it must be
    rejected.
-   Major operational workflow changes should reference relevant prompt
    version.

------------------------------------------------------------------------

# Documentation Mode Activation

After this seed document is registered, this chat transitions into:

📘 Documentation Mode

In Documentation Mode:

-   Practical guidance may be added.
-   Examples may be provided.
-   Tooling explanations may be expanded.
-   No governance rules may be altered.
-   No registry behavior occurs.

------------------------------------------------------------------------

**End of CPT Operator Documentation Seed v1.0.0**
