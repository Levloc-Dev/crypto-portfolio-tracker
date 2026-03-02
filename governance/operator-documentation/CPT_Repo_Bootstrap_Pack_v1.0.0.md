# Crypto Portfolio Tracker (CPT)

## Repo Bootstrap Pack

**Version:** v1.0.0 **Status:** Implementation Bootstrap Pack **Date:**
2026-03-02

------------------------------------------------------------------------

# 1️⃣ Purpose

This document bootstraps a governance-first Python repository for the
Crypto Portfolio Tracker (CPT).

It aligns with:

-   CPT Constitutional Charter v1.0.0
-   Master Prompt Library discipline
-   Operator Documentation separation model
-   Drift Detection enforcement model

This pack defines:

-   Folder structure
-   Deterministic pipeline layout
-   Schema discipline
-   CI enforcement hooks
-   Governance protection rules

------------------------------------------------------------------------

# 2️⃣ Recommended Repository Structure

crypto-portfolio-tracker/ ├── README.md ├── LICENSE ├── .gitignore ├──
.editorconfig ├── .gitattributes │ ├── governance/ │ ├── constitutional/
│ ├── master-prompt-library/ │ ├── operator-documentation/ │ └──
drift-workspace/ │ ├── schemas/ │ ├── tx_raw.schema.json │ ├──
tx_normalized.schema.json │ ├── prices.schema.json │ ├──
snapshot.schema.json │ └── report.schema.json │ ├── data/ │ ├── raw/ │
├── normalized/ │ ├── pricing/ │ └── manual-overrides/ │ ├── snapshots/
│ ├── daily/ │ ├── events/ │ └── tax-year/ │ ├── reports/ │ ├──
portfolio/ │ ├── tax/ │ └── exports/ │ ├── src/ │ ├── cpt/ │ │ ├──
**init**.py │ │ ├── ingestion/ │ │ ├── normalization/ │ │ ├── pricing/ │
│ ├── valuation/ │ │ ├── lp/ │ │ ├── tax/ │ │ ├── reporting/ │ │ └──
utils/ │ └── tests/ │ ├── cli/ │ └── cpt_run.py │ ├── tools/ │ ├──
validate_schemas.py │ ├── validate_snapshot.py │ ├── drift_compare.py │
└── hash_inputs.py │ ├── runs/ │ └── README.md │ ├── configs/ │ ├──
chains.yaml │ ├── pricing_sources.yaml │ └── tax_profiles.yaml │ └──
.github/ └── workflows/ ├── ci.yml └── governance-checks.yml

------------------------------------------------------------------------

# 3️⃣ Deterministic Pipeline Model

Raw → Normalize → Price → Calculate → Tax → Snapshot → Report

Each stage must:

-   Accept explicit inputs
-   Produce explicit outputs
-   Log version metadata
-   Preserve reproducibility

------------------------------------------------------------------------

# 4️⃣ CLI Pattern (Python)

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

All commands must log:

-   Engine version
-   Pricing source
-   Tax profile
-   Timestamp
-   Input hash

------------------------------------------------------------------------

# 5️⃣ Run Manifest Structure

runs/ └── YYYY-MM-DD/ └── run-`<hash>`{=html}/ ├── run.json ├── inputs/
└── outputs/

run.json must include:

-   Engine versions
-   Schema versions
-   Pricing source
-   Tax method
-   Input hash
-   Output hash

------------------------------------------------------------------------

# 6️⃣ CI Workflow (ci.yml)

Must:

-   Install Python
-   Install dependencies
-   Run tests
-   Validate schemas
-   Validate snapshot fixtures (if present)

------------------------------------------------------------------------

# 7️⃣ Governance Checks Workflow (governance-checks.yml)

Must fail if:

-   Governance files modified without version increment
-   Schema files modified without versioning discipline
-   Constitutional files overwritten
-   Required metadata (Version, Status, Date) missing

------------------------------------------------------------------------

# 8️⃣ CODEOWNERS Recommendation

/governance/\*\* @repo-owner /schemas/\*\* @repo-owner

------------------------------------------------------------------------

# 9️⃣ Branch Protection Rules

Protect main branch:

-   Require PR review
-   Require CI pass
-   Require governance-checks pass

------------------------------------------------------------------------

# 🔟 Initial Bootstrap Steps

1.  Create empty repo
2.  Commit governance files first
3.  Commit schema stubs
4.  Add CI workflows
5.  Enable branch protection
6.  Begin ingestion module

Governance precedes implementation.

------------------------------------------------------------------------

# 1️⃣1️⃣ Where This File Belongs

This file belongs in:

/governance/operator-documentation/

It should also be pasted into:

CPT --- Operator Documentation chat

This chat is the correct operational layer for this artifact.

------------------------------------------------------------------------

End of CPT Repo Bootstrap Pack v1.0.0
