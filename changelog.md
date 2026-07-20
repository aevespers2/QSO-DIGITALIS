# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Made approval of a unique, non-overlapping repository charter or explicit retirement the only active QSO-DIGITALIS product decision.
- 2026-07-16 — Confirmed that retirement is preferable to inferring identity, twin, wallet, runtime, or agent scope from the repository name.
- 2026-07-19 — Added a Pages-ready project overview that presents QSO-DIGITALIS as a charter decision repository and identifies draft PR #2 as a proposal rather than an implemented product.

### Architecture
- No schema, integration contract, or implementation may begin until ownership relative to the other QSO repositories is approved.
- 2026-07-19 — Added proposed responsibility, trust-boundary, validation, lifecycle, authority, and release-decision diagrams.
- 2026-07-19 — Added a design-contract framework for envelopes, topics, capabilities, queries, responses, acknowledgments, revocations, provenance links, retention, canonicalization, fixtures, compatibility, and rollback.
- 2026-07-19 — Added ADR-0001 as a proposed bounded field-contract charter candidate; no decision was accepted by implication.

### Documentation
- 2026-07-19 — Added strict MkDocs navigation, Pages landing content, project overview, architecture outline, diagrams, design contracts, charter decision framework, security/privacy requirements, limitations, developer onboarding, and operations/recovery guidance.
- 2026-07-19 — Expanded the root README and aligned `taskchain.md` and `release.md` with explicit documentation build, quality, publication, provenance, and rollback gates.

### Security
- 2026-07-19 — Documented strict parsing, deterministic canonicalization, fail-closed version resolution, capability separation, policy filtering, retention/revocation evaluation, bounded limits, non-executable records, provenance, and incident triggers as requirements rather than implemented controls.
- 2026-07-19 — Reaffirmed repository-wide `QSO-CONSENT-CAPACITY-LOCK-v1` binding without weakening or reinterpreting it.

### Implementation
- No implemented field capability is claimed; coordination, roadmap, scaffold, and documentation files remain proposal or administrative evidence only.

### Release
- Only a documentation charter candidate is possible before P0 approval; no runtime release is eligible.
- 2026-07-19 — Added exact-head documentation artifact, checksum, accessibility, privacy, license, claim-review, publication, and rollback requirements.

### Deployment
- No deployment surface is authorized.
- A successful documentation build does not authorize GitHub Pages publication.

## Entry Format
- Date
- Category: Product / Architecture / Documentation / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
