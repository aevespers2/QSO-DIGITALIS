# Developer Guide

## Repository mode

QSO-DIGITALIS is currently a documentation and architectural-review repository. Code changes are acceptable only when they support deterministic documentation validation or an explicitly approved future schema/fixture task.

## Source layout

```text
README.md                  project front door
docs/                      Pages-ready documentation source
taskchain.md               ordered product and architecture decisions
punchlist.md               bounded preparation and quality gates
release.md                 release, evidence, and approval gates
changelog.md               notable changes and evidence references
.consent/                   immutable consent-capacity policy
scripts/                    documentation validators only at this stage
tests/                      hostile and positive documentation regressions
.github/workflows/          exact-head, least-privilege validation
```

Roadmap or scaffold files are proposal artifacts. Their presence does not make generated paths implemented or approved.

## Documentation design rules

1. **One claim, one state.** Mark claims `PROPOSED`, `REVIEW`, `BLOCKED`, `VERIFIED`, `WITHDRAWN`, or `HISTORICAL`.
2. **Bind evidence exactly.** Use exact repository, commit, path, blob or digest, workflow run, and artifact identity where evidence exists.
3. **Separate syntax and semantics.** Parsing or schema validity is not semantic compatibility.
4. **Preserve source precedence.** Repository-local accepted records outrank portfolio summaries and copied descriptions.
5. **Keep authority explicit.** Documentation, CI, review, mergeability, or taxonomy mapping cannot create ownership or operational authority.
6. **Close lifecycle routes.** Corrections, withdrawals, migrations, retirement, and rollback must identify every controlled consumer.
7. **Make diagrams accessible.** Supply equivalent prose and avoid color-only meaning.

## Proposed schema-development sequence

Schema work remains blocked until the charter is approved. After approval, use this sequence:

```text
approved responsibility
→ semantic profile
→ namespace and record role
→ canonical byte profile
→ JSON Schema or equivalent
→ positive and hostile fixtures
→ independent validator
→ consumer compatibility tuple
→ correction/withdrawal propagation
→ migration and rollback witness
→ exact-head retained evidence
```

Do not begin with a runtime or scaffold materialization.

## Interface documentation checklist

For every future record family document:

- purpose and non-goals;
- producer and consumer responsibilities;
- exact version and namespace;
- required and optional fields;
- canonicalization and digest rules;
- ordering, retry, replay, duplicate, and conflict behavior;
- sensitivity, purpose, access, and retention;
- correction, revocation, withdrawal, and supersession;
- migration, deprecation, retirement, and rollback;
- hostile cases and failure dispositions;
- privacy, security, licensing, and accessibility considerations;
- owner or explicit vacancy.

## Validation architecture

The documentation validator should remain:

- standard-library only;
- deterministic and network-free;
- strict UTF-8;
- fail-closed on missing routes or required statements;
- tested against hostile mutations;
- isolated from generated evidence;
- executed at the submitted exact head;
- paired with read-only workflow permissions and immutable Action references.

## Pull request review

A documentation PR is review-ready when:

- required routes exist and resolve;
- planning files agree on status and scope;
- diagrams have prose alternatives;
- the consent-capacity marker is preserved where applicable;
- no unsupported implementation or publication claim appears;
- exact-head validation passes;
- unresolved decisions and vacancies remain explicit;
- rollback or withdrawal implications are described.

## Release boundary

No documentation contribution can independently authorize:

- acceptance of the Digital Consciousness Field charter;
- a namespace, schema, adapter, or consumer registration;
- materializer write mode;
- network, storage, credential, signing, payment, or repository-write capability;
- package release, Pages publication, deployment, or operational use.
