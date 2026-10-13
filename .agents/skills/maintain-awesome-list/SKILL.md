---
name: maintain-awesome-list
description: Curate and maintain this bilingual EmbeddingGemma awesome list. Use when explicitly asked to add projects, refresh popularity, audit entries, or revise list copy.
---

# Maintain Awesome EmbeddingGemma

Repository-local workflow, based on primary Awesome guidance. This is a custom skill, not an upstream-certified one.

## Workflow

1. Read `git status --short`, both READMEs, and `CONTRIBUTING.md`. Preserve unrelated edits.
2. Search official documentation, release notes, and project repositories. Confirm EmbeddingGemma **2** support; first-generation support is insufficient.
3. For GitHub projects, check archived status, documentation, recent activity, license, and stars with `gh api repos/OWNER/REPO`. Stars measure attention, not quality. Review release notes or implementation evidence before claiming support.
4. Keep popular applications separate from early-stage applications. Place inference frameworks, libraries, and servers in a separate section after model resources; their star counts do not qualify them as applications. For this list, the popular section requires at least 1,000 stars plus documented second-generation support. This threshold is a local editorial choice, not an Awesome rule. Use dynamic Shields.io star badges. Order projects by use or name, not live star counts.
5. Write one useful sentence per entry: what it does, where it runs, and any material support restriction. Keep runtime measurements distinct from documented claims. Do not pad the list with generic tools.
6. Update both language editions together. Retain equivalent URLs, restrictions, versions, and badge targets. Put contributor instructions in `CONTRIBUTING.md`.
7. Run `python3 scripts/check_docs.py` and `npx --yes awesome-lint@2.3.0 README.md`. Check changed external destinations; a timeout or 403 is inconclusive, not proof of abandonment. CI also runs Lychee.
8. Follow the AGY review-and-publish workflow below, then report the verified result briefly.

## AGY review and publishing

The maintainer has authorized automatic commits and pushes for curated list updates and these maintenance rules. This applies to manual and scheduled maintenance; no per-update confirmation is needed. It does not authorize repository settings changes, releases, external submissions, or contacting authors.

1. Prepare only the intended changes and complete the checks above. Read `~/.codex/instructions/review-workflows.md` for the local AGY review procedure. If that procedure or tooling is unavailable, preserve the changes and report the blocker.
2. Run `agy models </dev/null` and select an available Gemini 3.8 high model. Use `agr` with an explicit snapshot scope, `--timeout 900`, and closed stdin. For a cleanly isolated worktree diff, use `agr --worktree --model <model> --timeout 900 '<review prompt>' </dev/null`; if unrelated changes exist, isolate only the intended files/hunks in a staged snapshot and use `--staged`, preserving any pre-existing staging.
3. Bind the review to this repository and the intended diff. Supply the change goal, source evidence, constraints, and actual validation results. Require a read-only three-step review: define the problem, propose an independent solution before inspecting the diff, then compare and give findings plus an explicit ship recommendation.
4. Require a successful, nonempty review with explicit approval. Verify findings against sources and local files. Resolve blocking findings, rerun affected checks, and obtain approval for the final changed diff. A failed, empty, unavailable, or inconclusive review never counts as approval; stop before committing or pushing and report the blocker.
5. Inspect the final diff and status, ensuring AGY made no edits and no unrelated changes are included. Use `LattifAI <tech@lattifai.com>` and explicit pathspecs for the intended files/hunks to create a new commit; do not amend prior commits. Fetch and check the remote before committing and pushing to `origin/main`. If the branch, upstream, or remote history differs from the expected repository/main, stop and report rather than automatically merging, rebasing, or switching branches.
6. Use a normal push, never a force push. Do not stash, reset, restore, or clean unrelated work. Verify the remote branch contains the new commit, then report its link, what changed, and the checks and AGY conclusion. A rejected or uncertain push must be reported accurately, not treated as published.

## Editorial basis

- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): select resources maintainers can recommend; avoid exhaustive link collection.
- [List guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md): concise descriptions, contents, badge, contribution guide, and a Creative Commons license.
- [awesome-lint](https://github.com/sindresorhus/awesome-lint): Markdown and list checks.
- [Agent Skills specification](https://agentskills.io/specification): portable `SKILL.md` format.

## Scope and exceptions

- The English README is linted against Awesome conventions; Chinese headings remain translated.
- Repeated source links are intentional citations across sections, so `double-link` is disabled in the READMEs. Keep other lint rules active.
- This is an AI-assisted draft. The Awesome index rejects AI-generated lists and requires at least 30 days of public history. Passing lint does not establish eligibility or endorsement. The current mixed-case repository name also differs from its lowercase naming convention; do not rename it without a request.
- This skill runs only when invoked. It does not create a scheduled monitor.

See [source review](references/source-review.md) for the inspected third-party candidates and tooling choices.
