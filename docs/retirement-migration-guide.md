# QSO-DIGITALIS Retirement and Migration Guide

**Status:** `REVIEW — REVERSIBLE RETIREMENT PLAN`

This guide defines how QSO-DIGITALIS can be revised, consolidated, or retired without losing provenance, misleading readers, stranding consumers, or restoring stale implementation claims. It is documentation only and authorizes no repository setting change, redirect, archive, deletion, release, publication, deployment, or consumer migration.

## Retirement triggers

Begin a retirement review when any of the following is true:

- no unique repository role can be demonstrated;
- another repository already owns the relevant semantics with lower coupling;
- critical schema, security, privacy, licensing, support, migration, or rollback ownership remains vacant;
- runtime-local and Fabric-level record roles cannot be separated coherently;
- no independently reviewed producer and consumer need the proposed profile;
- the repository would preserve only a name or speculative capability rather than a maintainable contract;
- the accepted charter is withdrawn, superseded, or found unsafe.

A trigger opens review. It does not itself authorize retirement.

## Consumer and dependency inventory

Before any disposition, record:

| Inventory class | Required fields |
|---|---|
| Repository identity | Full repository name, default branch, exact head, visibility, description, topics, Pages state, and archive state |
| Historical candidates | PR or issue identity, source and target heads, merge state, evidence state, useful material, rejected authority, and superseding route |
| Contract references | Contract/profile identifier, namespace, version, digest, owner, status, and replacement if any |
| Producers | Repository, exact generation, records produced, authority claimed, and migration contact |
| Consumers | Repository, exact generation, records consumed, parser/semantic status, cache or copy state, and acknowledgment route |
| Documentation links | Incoming and outgoing repository links, Pages routes, READMEs, diagrams, catalogs, and portfolio indexes |
| Automation | Workflows, scheduled checks, bots, release jobs, deployment jobs, secrets or environments referenced, and disablement owner |
| Artifacts and releases | Artifact/release identity, retention, checksum, provenance, withdrawal state, and preservation requirement |
| Security and privacy | Data classes, incidents, reports, retention/deletion duties, consent dependencies, and unresolved risk |
| Ownership | Maintainer, documentation, schema, security, privacy, licensing, migration, rollback, support, and incident roles or vacancies |

An empty inventory must be demonstrated, not assumed.

## Retirement sequence

1. **Freeze scope.** Keep implementation, schema acceptance, consumer registration, publication, release, deployment, and repository-setting changes blocked.
2. **Record exact state.** Capture the default head, open pull requests, issues, workflows, releases, artifacts, Pages state, dependency references, and current documentation hashes.
3. **Classify historical work.** Preserve historical PR #2 and every later candidate as provenance; label each as current, stale, superseded, withdrawn, rejected, or migrated.
4. **Select a disposition.** Choose revise in place, split and migrate, consolidate into another repository, or retire without replacement.
5. **Define replacement ownership.** Name the destination repository and exact contract/document owners, or explicitly state that no replacement is accepted.
6. **Prepare migration mappings.** Map every retained identifier, term, status, lifecycle event, link, and consumer expectation to the replacement or to a terminal withdrawn state.
7. **Validate consumers independently.** Require each reachable consumer to acknowledge the exact retirement or migration generation; uncontrolled copies remain residual risk, not silent success.
8. **Prepare public wording.** State plainly that QSO-DIGITALIS never had an approved operational runtime unless separately evidenced.
9. **Review accessibility, security, privacy, and licensing.** Confirm the retirement notice and retained archive do not expose sensitive data, remove required attribution, or hide decision state.
10. **Obtain explicit approval.** Repository archive, redirects, Pages changes, release withdrawal, workflow disablement, and consumer migration require named human authorization.
11. **Apply one reversible change at a time.** Verify the resulting state after each approved transition and retain exact-head evidence.
12. **Close only after reachability review.** Record acknowledged consumers, unreachable consumers, uncontrolled copies, residual risk, and the restoration window.

Consumer acknowledgments must bind the exact retirement or migration generation, the receiving repository and head, the semantic mapping, and any residual copy or cache risk.

## Migration states

Use distinct states rather than a single “done” flag:

- `PLANNED` — disposition described, no change authorized;
- `APPROVED` — named reviewer approved the exact plan;
- `FROZEN` — new scope and consumer additions blocked;
- `MAPPING_READY` — identifier and semantic mappings reviewed;
- `CONSUMER_PENDING` — at least one controlled consumer has not acknowledged;
- `PARTIALLY_MIGRATED` — some controlled consumers acknowledge the new generation;
- `MIGRATED` — all known controlled consumers acknowledge the exact target generation;
- `RETIRED` — repository state and public documentation reflect the approved terminal disposition;
- `RESTORED` — an approved rollback returned to the prior supported state;
- `WITHDRAWN` — the migration or retirement claim is no longer current.

Never report `MIGRATED` or `RETIRED` solely because a repository was archived or a link was changed.

## Contract and identifier handling

- Preserve original identifiers and exact-source provenance in historical records.
- Do not reuse a retired namespace or profile identifier for different semantics.
- Mark replacement mappings as exact, lossless, lossy, unsupported, or unknown.
- Fail closed when a consumer cannot distinguish a retired generation from a current one.
- Preserve correction, revocation, withdrawal, and supersession links after migration.
- Do not copy authority claims, credentials, capabilities, consent, or canonical state through a documentation migration.
- Treat parser compatibility as insufficient without semantic and lifecycle agreement.

## Documentation and redirect plan

A retirement front door should include:

- the final disposition and approval record;
- the exact last supported documentation head;
- a concise statement of what the repository did and did not implement;
- replacement routes, when accepted;
- historical PR and decision links;
- security/contact guidance that remains valid;
- the date, scope, and evidence state of retirement;
- known residual consumers or uncontrolled copies;
- rollback or correction route.

Redirects must not erase historical context or imply that a replacement repository accepted every QSO-DIGITALIS proposal.

## Rollback and restoration

Rollback is required when:

- a replacement loses required semantics or provenance;
- a controlled consumer cannot process correction, withdrawal, or supersession;
- a redirect creates a broken or misleading dependency path;
- archive or publication changes hide required security, privacy, license, or support information;
- the resulting state differs from the approved plan;
- accessibility or public-review checks fail.

The restoration record must identify the prior exact head and settings, the failed transition, affected consumers, retained evidence, and the reviewer authorizing restoration. Restoring documentation does not restore stale implementation authority, revoked access, withdrawn claims, or expired evidence.

## Approval checklist

- [ ] Charter disposition is explicit.
- [ ] Historical PR #2 and all later candidates are classified.
- [ ] Producer, consumer, dependency, automation, release, artifact, and link inventories are complete.
- [ ] Replacement ownership and identifier mappings are reviewed.
- [ ] Controlled consumers have an acknowledgment and correction route.
- [ ] Security, privacy, consent, licensing, retention, accessibility, and support reviews are recorded.
- [ ] Repository settings, Pages, releases, workflows, and archives remain unchanged until separately approved.
- [ ] Rollback target and restoration evidence are defined.
- [ ] Resulting-state verification and residual-risk reporting are required.

## FYSA-120 capability mapping

Applied categories:

- **CAT-012:** lifecycle documentation, cross-file consistency, deprecation notices, and technical editing;
- **CAT-013:** dependency and consumer graph inventory, ownership analysis, and obstruction detection;
- **CAT-017:** provenance preservation, exact-state capture, correction and withdrawal propagation;
- **CAT-019:** accessible retirement notices, plain-language state distinctions, and equivalent routes;
- **CAT-031:** acceptance criteria, hostile transition cases, and resulting-state validation;
- **CAT-040:** migration sequencing, deprecation, retirement, restoration, and rollback readiness;
- **CAT-052:** approval boundaries, least privilege, consent, and audit evidence.

Proposed non-authoritative subdivision: **`040-J — repository retirement, consumer-reachability, and restoration engineering`**.
