# Developer onboarding

## Before contributing

Read the repository in this order:

1. `README.md` for the current claim boundary.
2. `taskchain.md` for the active priority and dependencies.
3. `release.md` for evidence gates and blocked authority.
4. `changelog.md` for accepted history.
5. `punchlist.md` for Builder constraints.
6. `.consent/consent-capacity-lock-v1.json` for the immutable consent-capacity control.
7. This documentation site for the architecture candidate and open decisions.

Do not treat draft PR #2, its scaffold plan, or generated placeholders as accepted implementation.

## Documentation environment

Requirements:

- Python 3.11 or newer;
- a clean virtual environment;
- no repository credentials beyond ordinary read access for a documentation build.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-docs.txt
mkdocs build --strict
mkdocs serve
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

The generated `site/` directory is disposable build output and should not be committed unless a separately approved Pages publication design explicitly requires it.

## Safe contribution types before P0

Before the charter is approved, acceptable contributions are limited to:

- correcting inaccurate or ambiguous documentation;
- improving responsibility and non-overlap analysis;
- defining review questions, acceptance evidence, retirement criteria, and migration constraints;
- adding synthetic diagrams or examples that remain clearly labeled as proposals;
- strengthening documentation validation without changing runtime authority;
- recording newly accepted decisions in `taskchain.md`, `release.md`, and `changelog.md`.

Do not add schemas, generated scaffolds, runtime modules, storage, transport, signing, schedules, external integrations, or deployment configuration as though P0 were complete.

## Future contract workflow

After explicit P0 approval, use the following sequence:

1. **Decision record:** link the approved charter, exact scope, owners, and non-goals.
2. **Schema draft:** add the minimum record family and canonicalization rules.
3. **Fixtures first:** create positive, negative, malformed, boundary, expiry, revocation, replay, tamper, and isolation cases.
4. **Validator:** implement deterministic validation only for the accepted contract.
5. **Exact-head CI:** verify source identity before testing and retain evidence artifacts.
6. **Security and privacy review:** test data classes, purpose, sensitivity, retention, redaction, logging, and prohibited media.
7. **Migration and rollback:** prove compatible and incompatible transitions before changing consumers.
8. **Bounded local path:** only then consider an in-memory/filesystem reference implementation with no network or credentials.
9. **Consumer acceptance:** require SEEKER, QuantumStateObjects, and FABRIC fixtures to bind to exact versions and hashes.
10. **Separate release decision:** implementation evidence does not itself authorize release or deployment.

## Pull-request expectations

Every pull request should state:

- objective and user outcome;
- exact files and authority boundaries affected;
- relationship to the active `taskchain.md` item;
- implementation claims, if any, limited to observable evidence;
- commands run and exact source identity;
- security, privacy, license, retention, migration, and rollback impact;
- downstream compatibility impact;
- unresolved questions and stop conditions.

Documentation-only pull requests should say explicitly that they do not authorize materialization, runtime, integration, release, or deployment.

## Review checklist

- [ ] The contribution advances the active task rather than inferring scope from the repository name.
- [ ] Current and proposed capabilities are clearly separated.
- [ ] Ownership does not overlap silently with another portfolio repository.
- [ ] Inputs, outputs, trust boundaries, non-goals, and failure behavior are explicit.
- [ ] Examples are synthetic and contain no secrets or restricted data.
- [ ] Contract names, versions, and hashes are not presented as accepted unless linked to evidence.
- [ ] `taskchain.md`, `release.md`, and `changelog.md` remain consistent.
- [ ] `mkdocs build --strict` passes from a clean environment.
- [ ] The consent-capacity lock passes against the submitted head.
- [ ] No generated site output or local environment files are committed accidentally.

## Branch and commit discipline

Use a dedicated branch, keep changes narrowly related, and prefer commits that separate documentation structure, content, and governance alignment. Never rewrite accepted history to make a candidate appear previously approved. Preserve draft PR and workflow identities in decision records.
