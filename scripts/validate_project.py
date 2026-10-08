from pathlib import Path
root=Path(__file__).resolve().parents[1]
for p in ["README.md","app/index.html","app/styles.css","app/app.js"]: assert (root/p).is_file(), p
html=(root/"app/index.html").read_text(encoding="utf-8")
for marker in ["roles","generate","answer","review","feedback"]: assert f'id="{marker}"' in html, marker
print("PASS: AI product team demo is complete")
