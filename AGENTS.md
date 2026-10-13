# Repository rules

- Scope: EmbeddingGemma2 resources; keep English and Chinese editions in sync.
- Keep descriptions short, sourced, and useful. Do not infer v2 support from v1.
- For requested list maintenance, use `.agents/skills/maintain-awesome-list/SKILL.md`.
- Validate with `python3 scripts/check_docs.py` and `npx --yes awesome-lint@2.3.0 README.md`.
- Standing maintainer authorization: for list maintenance and its documentation rules, follow the AGY review-and-publish workflow in `.agents/skills/maintain-awesome-list/SKILL.md`. After checks and explicit AGY approval of the final diff, create a new commit and push to `origin/main` without asking again.
- If review fails, is unavailable, or leaves blocking findings, do not commit or push; preserve the changes and report the blocker. Repository settings, releases, and external submissions still require separate authorization.
