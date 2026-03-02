# Crypto Portfolio Tracker (CPT)

## Constitutional Charter

**Version:** v1.0.0\
**Status:** Locked Baseline\
**Date:** 2026-03-02

------------------------------------------------------------------------

# 1️⃣ Purpose

The Crypto Portfolio Tracker (CPT) is a deterministic, audit-ready
digital asset tracking system designed to:

-   Track multi-chain crypto holdings\
-   Track liquidity pool (LP) positions\
-   Track staking and yield activities\
-   Record realized and unrealized gains\
-   Produce tax-aligned reporting\
-   Preserve historical state snapshots\
-   Maintain reproducible calculations

CPT prioritizes:

-   Determinism\
-   Auditability\
-   Version discipline\
-   Architectural clarity\
-   Separation of concerns

CPT is a financial record system --- not a speculative trading engine.

------------------------------------------------------------------------

# 2️⃣ Core Principles

## 2.1 Determinism First

All portfolio calculations must be reproducible from:

-   Raw transaction data\
-   Defined pricing source\
-   Versioned calculation logic

If identical inputs are provided, identical outputs must be produced.

No hidden state.\
No opaque recalculations.

------------------------------------------------------------------------

## 2.2 Audit Trail Preservation

Every derived output must be traceable to:

-   Source transaction\
-   Normalization logic version\
-   Pricing source\
-   Calculation engine version

Historical results must remain reconstructable.

------------------------------------------------------------------------

## 2.3 Immutable Snapshots

CPT supports:

-   Daily portfolio snapshots\
-   Tax-year snapshots\
-   Event-based snapshots

Snapshots are immutable once registered.

Amendments require version increment.

------------------------------------------------------------------------

## 2.4 Governance Separation

CPT governance is divided into:

  Layer                       Authority
  --------------------------- --------------------------
  Constitutional Archive      Governance standards
  Master Prompt Library       Operational prompts
  Operator Documentation      Usage & tooling
  Local Git Repo              Implementation
  Drift Detection Workspace   Architectural comparison

No single layer overrides the Constitution.

------------------------------------------------------------------------

# 3️⃣ Architectural Boundaries

CPT consists of modular domains:

-   Transaction Ingestion
-   Normalization Engine
-   Pricing Engine
-   Position Calculator
-   LP Valuation Module
-   Tax Computation Engine
-   Reporting Layer
-   Snapshot Registry

Modules must not:

-   Share hidden state
-   Modify upstream raw data
-   Mutate registered snapshots

Each module must declare:

-   Version
-   Input contract
-   Output schema

------------------------------------------------------------------------

# 4️⃣ Data Model Discipline

All CPT data must follow:

-   Explicit schemas
-   Version-controlled structure
-   Backwards compatibility rules

Breaking schema changes require:

-   Version increment
-   Migration documentation
-   Drift review
-   Snapshot compatibility declaration

Silent schema mutation is prohibited.

------------------------------------------------------------------------

# 5️⃣ Pricing Source Rules

CPT may consume:

-   WebSocket feeds
-   API pricing sources
-   Onchain pricing
-   Manual override inputs (if explicitly versioned)

Pricing inputs must be:

-   Timestamped
-   Source-identified
-   Versioned

Changing pricing source logic without versioning is an automatic
governance violation.

------------------------------------------------------------------------

# 6️⃣ Tax Integrity Model

CPT tax computation must:

-   Declare jurisdiction assumptions
-   Declare cost basis method (e.g., FIFO, LIFO, Share Pooling)
-   Version tax engine logic
-   Produce exportable audit logs

Tax assumptions must not be implicit.

------------------------------------------------------------------------

# 7️⃣ Deterministic Snapshot Model

Each snapshot must contain:

-   Portfolio state
-   Asset balances
-   LP positions
-   Pricing source
-   Calculation engine version
-   Tax engine version
-   Timestamp
-   Hash of input state

Snapshots must be reproducible from stored raw inputs.

------------------------------------------------------------------------

# 8️⃣ Drift Detection Policy

Any modification to:

-   Schema
-   Calculation logic
-   Event types
-   Snapshot structure
-   Pricing method
-   Tax method

Requires:

1.  Candidate Snapshot
2.  Drift Detection comparison
3.  Explicit PASS before registration

Silent architectural drift = FAIL.

------------------------------------------------------------------------

# 9️⃣ Versioning Discipline

CPT follows semantic governance versioning:

-   MAJOR --- breaking architectural change
-   MINOR --- additive non-breaking extension
-   PATCH --- documentation clarification only

No version may overwrite a prior registered version.

------------------------------------------------------------------------

# 🔟 Amendment Procedure

To amend CPT Constitution:

1.  Draft new version (.md file)
2.  Increment version appropriately
3.  Clearly declare:
    -   Changes introduced
    -   Migration implications
4.  Submit to Constitutional Archive
5.  Register new version

Previous versions remain preserved unless explicitly archived.

------------------------------------------------------------------------

# 1️⃣1️⃣ Non-Scope

CPT does NOT:

-   Execute trades
-   Provide financial advice
-   Forecast markets
-   Optimize yield strategies
-   Store private keys
-   Custody assets

CPT is a record and reporting system.

------------------------------------------------------------------------

# 1️⃣2️⃣ Authority Declaration

This document defines the immutable governance baseline for CPT.

All:

-   Prompts
-   Documentation
-   Tooling
-   Modules
-   Snapshots
-   Registry submissions

Must comply with this Constitution.

If conflict occurs, this document prevails.

------------------------------------------------------------------------

**End of CPT Constitutional Charter v1.0.0**
