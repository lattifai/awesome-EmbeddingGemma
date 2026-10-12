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
4. Keep popular projects separate from early-stage examples. For this list, the popular section requires at least 1,000 stars plus documented second-generation support. This threshold is a local editorial choice, not an Awesome rule. Refresh counts together, date the snapshot, and sort descending.
5. Write one useful sentence per entry: what it does, where it runs, and any material support restriction. Keep runtime measurements distinct from documented claims. Do not pad the list with generic tools.
6. Update both language editions together. Retain equivalent URLs, restrictions, versions, and counts. Put contributor instructions in `CONTRIBUTING.md`.
7. Run `python3 scripts/check_docs.py` and `npx --yes awesome-lint@2.3.0 README.md`. Check changed external destinations; a timeout or 403 is inconclusive, not proof of abandonment. CI also runs Lychee.
8. Report changes and actual verification briefly. Do not commit, push, or submit to another list unless requested.

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
