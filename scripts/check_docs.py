"""Check local Markdown links, README anchors, and bilingual source parity."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(([^\s)]+)\)")


def anchors(text):
    return {
        re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        for title in re.findall(r"^#{1,6} (.+)$", text, re.M)
    }


errors = []
for path in ROOT.rglob("*.md"):
    if any(part in {".git", "node_modules"} for part in path.parts):
        continue
    text = path.read_text()
    for target in LINK.findall(re.sub(r"`[^`]+`", "", text)):
        if target.startswith(("https://", "http://", "mailto:")):
            continue
        file, _, fragment = target.partition("#")
        destination = path.parent / file if file else path
        if not destination.is_file():
            errors.append(f"{path.relative_to(ROOT)}: missing {target}")
        elif fragment and fragment not in anchors(destination.read_text()):
            errors.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    if not text.endswith("\n") or any(line != line.rstrip() for line in text.splitlines()):
        errors.append(f"{path.relative_to(ROOT)}: whitespace or final newline")

english, chinese = [(ROOT / name).read_text() for name in ("README.md", "README.zh-CN.md")]
urls = lambda text: {url for url in LINK.findall(text) if url.startswith("https://")}
if urls(english) != urls(chinese):
    errors.append("README source URLs differ between languages")
counts = lambda text: re.findall(r"\|\s+([\d,]+)\s+\|", text)
if counts(english) != counts(chinese):
    errors.append("README star counts differ between languages")
if errors:
    raise SystemExit("\n".join(errors))
print("PASS: local links, anchors, whitespace, bilingual URLs and star counts")
