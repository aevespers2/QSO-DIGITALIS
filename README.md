# QSO-DIGITALIS

QSO-DIGITALIS is currently a **charter decision repository**, not an implemented product or service. Its active purpose is to determine whether the QSO portfolio needs a separate, bounded, content-addressed evidence-exchange contract—or whether this repository should be retired.

The leading proposal is the **Digital Consciousness Field (DCF)** in draft PR #2. That name is architectural shorthand only; it does not assert literal consciousness, awareness, sentience, identity, agency, or independent authority.

## Status

- **Charter:** under review
- **Accepted schemas:** none
- **Reference implementation:** none
- **Network/storage service:** not authorized
- **Release:** blocked
- **Deployment:** not authorized

Documentation and scaffold files are proposal artifacts. Their presence must not be presented as implementation evidence.

## Proposed bounded role

If explicitly approved, QSO-DIGITALIS would own only the versioned exchange contracts for immutable evidence references, operation-specific capabilities, topics, scoped queries and responses, acknowledgments, retention, expiry, revocation, and provenance links.

Neighboring repositories retain their existing authority:

- **QSO-SEEKER** — isolated retrieval, sanitization, canonicalization, and source evidence records.
- **QuantumStateObjects** — local QSO state and execution.
- **QSO-FABRIC** — experiment evidence assembly and recording of evidence use.
- **QSO-DIGITALIS** — proposed exchange-envelope and access-policy contract only.

## Explicit non-goals

QSO-DIGITALIS does not authorize:

- network retrieval or raw response transport;
- credentials, packages, binaries, archives, Git objects, or executable payloads;
- unrestricted shared memory or implicit trust between QSOs;
- conclusion or action approval;
- repository mutation, payments, signing authority, scheduling, release publication, or production deployment;
- literal-consciousness claims.

## Documentation

A Pages-ready MkDocs site is available under `docs/`:

- [Project overview](docs/project-overview.md)
- [Architecture outline](docs/architecture.md)
- [Architecture diagrams](docs/diagrams.md)
- [Design contracts](docs/design-contracts.md)
- [Charter decision](docs/charter-decision.md)
- [Security and privacy](docs/security-privacy.md)
- [Limitations](docs/limitations.md)
- [Developer onboarding](docs/onboarding.md)
- [Operations and recovery](docs/operations.md)
- [ADR-0001](docs/adr/0001-bounded-field-charter-candidate.md)

Build locally with:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install mkdocs
mkdocs build --strict
```

A successful documentation build proves rendering and navigation only. It does not approve the charter, establish runtime capability, or authorize Pages publication.

## Decision path

The current P0 decision is to:

1. approve a unique bounded field-contract charter;
2. request bounded revision; or
3. retire the repository and preserve a clear migration/provenance record.

See [`taskchain.md`](taskchain.md), [`release.md`](release.md), and [`changelog.md`](changelog.md) for the authoritative work state and release gates.

## Contribution boundary

Documentation, diagrams, decision records, threat models, fixture plans, and review checklists may be improved while the charter is unresolved. Implementation, scaffold materialization, integration, release, and deployment remain blocked until explicit approval and immutable evidence satisfy the recorded gates.
