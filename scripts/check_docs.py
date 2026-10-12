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
def star_badges(text):
    pairs = []
    for line in text.splitlines():
        if not line.startswith("| [") or "img.shields.io/github/stars/" not in line:
            continue
        repo = re.search(r"\]\(https://github.com/([^/)]+/[^/)]+)\)", line)
        badge = re.search(r"img\.shields\.io/github/stars/([^?/)]+/[^?/)]+)\?style=flat", line)
        if not repo or not badge or repo[1] != badge[1]:
            errors.append("Star badge does not match its project: " + line)
        else:
            pairs.append((repo[1], badge[1]))
    return pairs


if star_badges(english) != star_badges(chinese):
    errors.append("README star badges differ between languages")
if errors:
    raise SystemExit("\n".join(errors))
print("PASS: local links, anchors, whitespace, bilingual URLs and star badge targets")
