# Crypto Portfolio Tracker (CPT)

## GitHub Governance Lifecycle

**Version:** v1.0.0 **Status:** Operational Governance Framework
**Date:** 2026-03-02

------------------------------------------------------------------------

# 1️⃣ Purpose

This document defines the lifecycle model governing GitHub operations
within the Crypto Portfolio Tracker (CPT) project.

It formalizes:

-   How GitHub decisions are proposed
-   How they are validated
-   How they are enforced
-   How they evolve over time
-   When enforcement dominance transitions occur

This lifecycle aligns with CPT Constitutional Charter v1.0.0.

------------------------------------------------------------------------

# 2️⃣ Lifecycle Phases

CPT GitHub governance operates in structured phases:

## Phase 0 --- Bootstrap

Characteristics: - Governance stack committed - CI initialized - Basic
branch protection enabled - SSH architecture verified - Deterministic
run manifests implemented

Primary Chat: CPT --- GitHub & Repository Operations

Enforcement Mode Role: Advisory validation only

------------------------------------------------------------------------

## Phase 1 --- Structured Development

Characteristics: - Active feature development - Schema evolution - CLI
surface expansion - CI refinement - Governance-check hardening

Primary Chat: CPT --- GitHub & Repository Operations

Enforcement Mode Role: Validates major structural changes before
implementation

Transition Trigger to Phase 2: - Schema stabilization - Snapshot
structure stability - First pre-release tag

------------------------------------------------------------------------

## Phase 2 --- Stabilization

Characteristics: - Release tagging begins (v0.x → v1.0.0 trajectory) -
Snapshot logic stable - Deterministic guarantees audited - CI fully
hardened - Branch protection strictly enforced

Primary Chat: CPT --- GitHub Enforcement Mode

Operations Role: Design proposals only

Transition Trigger to Phase 3: - v1.0.0 release - Financial reporting
reliance - External contributor involvement

------------------------------------------------------------------------

## Phase 3 --- Production Governance

Characteristics: - Semantic version enforcement - Signed tags required -
Strict PR-only workflow - Mandatory status checks - Immutable release
history

Primary Chat: CPT --- GitHub Enforcement Mode

Operations Role: Experimental design workspace only

------------------------------------------------------------------------

# 3️⃣ Change Flow Model

All GitHub structural changes follow this lifecycle:

Idea → Operations Proposal\
↓\
Formalized Proposal Template\
↓\
Enforcement Review\
↓\
APPROVED → Implement → Commit → Push\
REJECTED → Revise in Operations

No direct enforcement decisions occur inside Operations chat.

------------------------------------------------------------------------

# 4️⃣ Enforcement Dominance Rules

Enforcement Mode becomes dominant when:

☐ Schema reaches stable version\
☐ Snapshot format stable\
☐ First stable semantic release tagged\
☐ Branch protection fully enabled\
☐ CI blocking required for all merges

Until then, Operations remains primary.

------------------------------------------------------------------------

# 5️⃣ Prohibited Actions (All Phases)

-   Force push to main\
-   Modify locked constitutional baseline\
-   Disable CI without enforcement approval\
-   Retag existing release versions\
-   Merge without passing governance-checks\
-   Rewrite public history

Violation → Immediate REJECTED status in Enforcement Mode

------------------------------------------------------------------------

# 6️⃣ Versioning Governance

GitHub lifecycle versioning follows:

MAJOR → Structural Git governance change\
MINOR → Enforcement rule expansion\
PATCH → Documentation clarification

Lifecycle version does NOT modify constitutional version.

------------------------------------------------------------------------

# 7️⃣ Audit Requirements (Phase 2+)

Before each major release:

☐ Confirm branch protection rules\
☐ Confirm CI required checks\
☐ Confirm governance-check integrity\
☐ Confirm schema version discipline\
☐ Confirm tag immutability

------------------------------------------------------------------------

# 8️⃣ Maturity Indicators

CPT GitHub governance maturity is achieved when:

-   No direct pushes to main\
-   All merges via PR\
-   CI cannot be bypassed\
-   Constitutional baseline untouched\
-   Release tags immutable\
-   Deterministic run manifests validated

------------------------------------------------------------------------

End of CPT GitHub Governance Lifecycle v1.0.0
