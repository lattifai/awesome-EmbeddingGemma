# Maintenance references

Reviewed: 2026-10-12.

## Primary standards and tools

- [Awesome creation guide](https://github.com/sindresorhus/awesome/blob/main/create-list.md): check for an existing list before starting another.
- [Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md): curation and badge usage; the badge does not imply index inclusion.
- [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md): editorial format and separate index-admission requirements.
- [awesome-lint](https://github.com/sindresorhus/awesome-lint): automated Markdown/list validation. This repository pins CLI version 2.3.0.
- [Lychee action](https://github.com/lycheeverse/lychee-action): broken-link checks in pull requests and pushes. No scheduled workflow is configured.
- [Agent Skills specification](https://agentskills.io/specification): skill packaging and metadata.

For this small list, manually maintained Markdown plus PR checks is sufficient. A website, database, and generated README would add maintenance without improving resource selection.

## Skill candidates inspected

| Candidate | Useful aspect | Why not installed |
| --- | --- | --- |
| [awesome-playwright audit-entries](https://github.com/mxschmitt/awesome-playwright/blob/main/.claude/skills/audit-entries/SKILL.md) | Existing-entry audits using repository metadata. | Playwright-specific categories and removal workflow; assumes parallel agents. |
| [awesome-list-site awesome-list](https://github.com/krzemienski/awesome-list-site/blob/main/.agents/skills/awesome-list/SKILL.md) | Import/export and validation workflow. | Depends on its own PostgreSQL application and API; its README license-section convention conflicts with current upstream guidance. |
| [hermes-skills bilingual-awesome-list-readme](https://github.com/itgoyo/hermes-skills/blob/main/documentation/bilingual-awesome-list-readme/SKILL.md) | Bilingual README synchronization. | Depends on Hermes tools and leaves repository-row descriptions untranslated. |

These are related examples, not verified drop-in skills for this repository. The local skill is an original, narrow workflow grounded in the primary standards above; it is not presented as an official or independently certified skill.
