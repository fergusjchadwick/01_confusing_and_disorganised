"""Stage 3: rank guests and render a small Markdown report."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "out3.csv"
DEST = ROOT / "answer_real.md"

with SOURCE.open(newline="", encoding="utf-8") as handle:
    scores = list(csv.DictReader(handle))

if not scores:
    raise ValueError("There are no scores to rank")
scores.sort(key=lambda item: (-float(item["sleepiness_score"]), item["name"]))

lines = [
    "# Christmas sleep prediction",
    "",
    f"**Predicted first to fall asleep: {scores[0]['name']}**",
    "",
    "| Rank | Guest | Sleepiness score |",
    "| ---: | --- | ---: |",
]
for rank, item in enumerate(scores, start=1):
    lines.append(f"| {rank} | {item['name']} | {float(item['sleepiness_score']):.2f} |")
lines += ["", "*Higher scores correspond to earlier predicted sleep, solely under this toy rule.*", ""]
DEST.write_text("\n".join(lines), encoding="utf-8")
print(f"Predicted {scores[0]['name']} -> {DEST.relative_to(ROOT)}")
