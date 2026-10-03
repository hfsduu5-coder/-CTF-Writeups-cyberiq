from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
required=["README.md","WRITEUPS.md","SKILLS.md","TOOLS.md","SECURITY.md","CONTRIBUTING.md","data/progress.json","templates/WRITEUP-TEMPLATE.md"]
errors=[f"missing: {p}" for p in required if not (root/p).exists()]
try:
 data=json.loads((root/"data/progress.json").read_text(encoding="utf-8"))
 if not isinstance(data,(dict,list)): errors.append("progress.json must contain an object or list")
except Exception as exc: errors.append(f"invalid progress.json: {exc}")
for p in root.rglob("*.md"):
 text=p.read_text(encoding="utf-8",errors="replace")
 if "BEGIN PRIVATE KEY" in text or "ghp_" in text: errors.append(f"possible secret marker: {p.relative_to(root)}")
if errors:
 print("\n".join(errors)); sys.exit(1)
print("portfolio validation passed")
