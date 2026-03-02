# Crypto Portfolio Tracker (CPT)

## GitHub Enforcement Checklist

**Version:** v1.0.0 **Status:** Enforcement Compliance Checklist
**Date:** 2026-03-02

------------------------------------------------------------------------

# 1️⃣ Purpose

This checklist operationalizes the CPT GitHub Dual-Layer Interaction
Protocol.

It defines mandatory enforcement controls that must be satisfied before
any GitHub configuration change, workflow modification, or structural
repository update is implemented.

This checklist applies exclusively to:

-   CPT --- GitHub Enforcement Mode

------------------------------------------------------------------------

# 2️⃣ Locked Baseline Protection

☐ Confirm governance/constitutional/CPT_Constitutional_Charter_v1.0.0.md
has not been modified\
☐ Confirm no force-push occurred to main\
☐ Confirm no historical commit rewrite (no rebase on main)\
☐ Confirm new constitutional changes (if any) use new versioned file

Failure → REJECTED

------------------------------------------------------------------------

# 3️⃣ Governance Metadata Integrity

If governance/\*.md files changed:

☐ Contains Version field\
☐ Contains Status field\
☐ Contains Date field\
☐ Version increment appropriate\
☐ No silent overwrite of prior versions

Failure → REJECTED

------------------------------------------------------------------------

# 4️⃣ Schema Discipline Controls

If schemas/ changed:

☐ Files remain \*.schema.json\
☐ \$id reflects correct semantic version\
☐ Breaking changes accompanied by version bump\
☐ No schema file renamed without migration documentation\
☐ CI validates schema integrity

Failure → REJECTED

------------------------------------------------------------------------

# 5️⃣ CI Enforcement Controls

☐ ci.yml exists and runs on pull_request + main\
☐ governance-checks.yml exists and runs on pull_request + main\
☐ CI cannot be bypassed\
☐ No workflow disabling in PR\
☐ Required status checks enabled in branch protection

Failure → REJECTED

------------------------------------------------------------------------

# 6️⃣ Branch Protection Requirements

Main branch must enforce:

☐ Pull Request required\
☐ Status checks required\
☐ No direct pushes\
☐ No force pushes\
☐ No deletion allowed\
☐ Linear history enforced (recommended)

Failure → CONDITIONAL APPROVAL until configured

------------------------------------------------------------------------

# 7️⃣ Commit Discipline Validation

☐ Commit messages structured\
☐ No mixed-purpose commits\
☐ Governance changes isolated from feature commits\
☐ No vague commit messages ("update", "fix stuff", etc.)

Failure → CONDITIONAL APPROVAL

------------------------------------------------------------------------

# 8️⃣ SSH & Remote Integrity

☐ Remote uses approved alias (github-levloc-dev)\
☐ IdentityFile matches authorized key\
☐ No alternate unauthorized remote configured\
☐ git remote -v matches expected origin

Failure → REJECTED

------------------------------------------------------------------------

# 9️⃣ Deterministic Artifact Integrity

If CLI or pipeline logic changed:

☐ Run manifest format unchanged or versioned\
☐ input_hash logic unchanged or versioned\
☐ output_hash logic unchanged or versioned\
☐ Snapshot schema unchanged or versioned\
☐ Deterministic guarantees preserved

Failure → REJECTED

------------------------------------------------------------------------

# 🔟 Release & Tagging Discipline (When Applicable)

If release/tag introduced:

☐ Semantic version format (vX.Y.Z)\
☐ Tag matches repo state\
☐ No retagging existing version\
☐ Release notes reference schema + engine versions\
☐ Tag created from protected branch

Failure → REJECTED

------------------------------------------------------------------------

# 1️⃣1️⃣ Enforcement Decision Output

After checklist review, Enforcement Mode must output one of:

APPROVED --- All enforcement criteria satisfied

REJECTED --- Non-compliant (list failed sections)

CONDITIONAL APPROVAL --- Must satisfy:\
- Item 1\
- Item 2

No additional commentary.

------------------------------------------------------------------------

# 1️⃣2️⃣ Escalation Rule

If any item in Sections 2, 4, 5, 8, or 9 fails:

Automatic REJECTED

These sections protect deterministic and constitutional guarantees.

------------------------------------------------------------------------

End of CPT GitHub Enforcement Checklist v1.0.0
