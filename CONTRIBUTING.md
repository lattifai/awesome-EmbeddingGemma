# Contributing

## Inclusion criteria

- Explicitly support EmbeddingGemma 2 (do not infer support from EmbeddingGemma 300M).
- Prefer original documentation, repositories, and reproducible demonstrations.
- Disclose modality, backend, or version constraints.
- Avoid generic directories, affiliate links, duplicates, and unverified performance claims.
- Disclose project affiliations upon submission.

## Submission checklist

1. Add the entry to both `README.md` and `README.zh-CN.md`.
2. Include direct evidence of second-generation support and the date checked.
3. State whether verification is documentation-only or includes runtime environment, version, commands, and results.
4. Ensure consistent formatting and relative links across language editions.
5. For corrections or removals, provide replacement sources or context (broken links alone do not prove abandonment).

## Benchmark submissions

Community benchmark submissions must include:

- Checkpoint, revision, runtime version, precision, and active encoders.
- Vector dimensions, prompts, dataset, evaluation metric, and hardware specifications.
- Exact reproduction instructions.
- Separate metrics for retrieval quality, latency, memory usage, and index size (download size is not peak memory).
- Clear labeling of publisher-reported vs. independent results, keeping first-generation metrics distinct.

## License

Contributions are dedicated under [CC0-1.0](LICENSE). Referenced resources retain their original licenses.

## Maintenance

- Use `- [Name](URL) - One-sentence description.` for list entries.
- Popular projects need 1,000+ stars and documented v2 support; smaller projects belong in community tools. Date star snapshots. This is our editorial threshold.
- Run `python3 scripts/check_docs.py` and `npx --yes awesome-lint@2.3.0 README.md`. CI checks external links with Lychee; investigate transient failures before removing entries.
- Invoke the repository-local `maintain-awesome-list` skill for repeatable updates. It follows the [Awesome guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md); it is not an official Awesome skill.
