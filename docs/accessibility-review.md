# QSO-DIGITALIS Accessibility Review

**Status:** `REVIEW — SOURCE COMPLETE; RENDERED REVIEW REQUIRED`

Accessibility is part of documentation correctness. A charter, retirement, evidence, or authority state is not adequately communicated when a reader must infer it from color, layout, animation, a diagram, or specialist vocabulary alone.

This review surface does not approve GitHub Pages publication. It defines the checks required before a separately authorized publication or release.

## Accessibility principles

- Use a predictable heading hierarchy and descriptive link text.
- State evidence, authority, and lifecycle status in text; status is not conveyed by color alone.
- Give every diagram an equivalent prose explanation that preserves actors, direction, trust boundaries, and failure paths.
- Make tables understandable when read linearly and avoid using spatial position as the only relationship cue.
- Separate current evidence, proposed interpretation, unresolved blockers, historical material, and approved decisions.
- Explain specialized terms at first use and preserve a plain-language decision route.
- Keep security, consent, privacy, correction, withdrawal, retirement, and rollback routes discoverable.
- Use synthetic, non-sensitive examples and avoid exposing personal or confidential information.

## Source-review checklist

### Structure and navigation

- [ ] Each page has one descriptive level-one heading.
- [ ] Heading levels do not skip solely for visual styling.
- [ ] The README and documentation index provide deterministic reader routes.
- [ ] Link text describes its destination without relying on surrounding text.
- [ ] Navigation labels distinguish project overview, architecture, contract boundaries, decision, retirement, onboarding, and developer material.
- [ ] Current location and document status are expressed in text.

### Diagrams and technical relationships

- [ ] Every Mermaid or image-based diagram has an **Equivalent prose:** section.
- [ ] The prose names all components, edge directions, trust boundaries, blocked transitions, and review gates shown visually.
- [ ] No decision depends on shape, line style, position, or color alone.
- [ ] Complex graphs are decomposed into pairwise edges and explicit triple-overlap witnesses.
- [ ] Failure, correction, withdrawal, and rollback paths are described, not merely drawn.

### Tables and code

- [ ] Tables have descriptive headers and remain meaningful when cells are read row by row.
- [ ] Status abbreviations are defined before use.
- [ ] Long tables include an introductory explanation and a plain-language conclusion.
- [ ] Code and commands are optional aids rather than the only way to understand a process.
- [ ] Examples identify whether they are normative, illustrative, synthetic, or historical.

### Language and evidence state

- [ ] `PROPOSED`, `REVIEW`, `BLOCKED`, `VERIFIED`, `WITHDRAWN`, and `HISTORICAL` are used consistently.
- [ ] `VERIFIED` is bound to the exact source and scope.
- [ ] Documentation validation is not described as charter, compatibility, security, publication, release, or operational approval.
- [ ] Literal-consciousness, sentience, personhood, identity-authority, or autonomous-authority claims are not inferred from the repository name.
- [ ] Readers can locate unresolved ownership, privacy, security, licensing, retention, migration, and rollback gaps.

### Forms, decisions, and review records

- [ ] Decision templates use explicit labels and instructions.
- [ ] Required fields are identified in text, not only by formatting.
- [ ] Errors or missing evidence identify the affected field and a correction route.
- [ ] Approval, rejection, withdrawal, and appeal or reconsideration states are distinguishable.
- [ ] No control implies that a reviewer can authorize implementation, publication, release, or deployment through documentation alone.

## Rendered-site review

A rendered review must be performed against the exact publication candidate, not inferred from Markdown source alone.

### Keyboard and focus

- Navigate every page, menu, disclosure, search control, and link using only the keyboard.
- Confirm focus is visible and follows a logical order.
- Confirm there is no keyboard trap.
- Confirm skip or landmark navigation provides an efficient route to primary content where the theme supports it.

### Zoom, reflow, and viewport

- Review at 200% zoom.
- Review at 400% zoom or the closest supported reflow configuration.
- Check narrow mobile-width rendering without requiring two-dimensional scrolling for ordinary prose.
- Confirm tables and code blocks have a usable overflow or alternative presentation.
- Confirm status labels, callouts, and navigation do not overlap or disappear.

### Contrast, motion, and visual presentation

- Check text, link, focus, status, and diagram contrast.
- Confirm meaning is preserved in high-contrast and grayscale viewing.
- Respect reduced-motion preferences; no essential information may depend on animation.
- Avoid flashing, rapid movement, or decorative motion that interferes with reading.
- Confirm diagrams remain understandable without color.

### Assistive-technology comprehension

- Review landmark order, heading outline, link purpose, table headers, code labels, and diagram alternatives with a screen reader or equivalent accessibility inspection.
- Confirm evidence-state and authority-boundary language is announced in a coherent order.
- Confirm page titles and navigation distinguish similarly named QSO repositories.
- Confirm correction, withdrawal, retirement, and contact routes are reachable without visual inference.

## Decision and retirement comprehension test

A reviewer unfamiliar with the portfolio should be able to answer, using only the documentation:

1. What is QSO-DIGITALIS currently?
2. What does it explicitly not implement or authorize?
3. What decision is pending?
4. Why is historical PR #2 not current authority?
5. What evidence would be required for an active charter?
6. How would the repository be retired without losing provenance or stranding consumers?
7. Where are security, privacy, consent, licensing, accessibility, migration, rollback, publication, release, and deployment approvals recorded?

Failure to answer any item is a documentation defect.

## Review record

Record each review with:

- repository and exact source head;
- rendered artifact or preview identity and digest;
- date and reviewer;
- browser, viewport, zoom, operating system, and assistive technology;
- pages and routes reviewed;
- keyboard and focus result;
- 200% and 400% zoom/reflow result;
- contrast, reduced-motion, and grayscale result;
- diagram and table comprehension result;
- decision and retirement comprehension result;
- findings, severity, owner, correction target, and retest evidence;
- disposition: `PASS_FOR_SEPARATE_PUBLICATION_REVIEW`, `FAIL_CLOSED`, or `WITHDRAWN`.

A source-only pass cannot be recorded as a rendered-site pass.

## Publication boundary

Publication remains blocked until the exact rendered candidate passes accessibility, security, privacy, licensing, provenance, link, and authority-boundary review and receives separate explicit approval. Publication does not approve a repository charter, contract, implementation, release, deployment, or operational use.

## FYSA-120 capability mapping

Applied categories:

- **CAT-012:** information architecture, navigation, technical editing, documentation testing, and lifecycle synchronization;
- **CAT-013:** relationship explanation, decision-path modeling, and obstruction communication;
- **CAT-017:** exact-artifact review records, provenance, correction, and retest binding;
- **CAT-019:** accessible writing, keyboard and focus review, zoom and reflow, diagram alternatives, status comprehension, and plain language;
- **CAT-031:** acceptance criteria, hostile accessibility regressions, and fail-closed publication review;
- **CAT-040:** accessible migration, retirement, correction, and rollback routes;
- **CAT-052:** consent, privacy, least privilege, and review-authority boundaries.

Proposed non-authoritative subdivision: **`019-K — evidence-state, authority-boundary, and retirement-route accessibility assurance`**.
