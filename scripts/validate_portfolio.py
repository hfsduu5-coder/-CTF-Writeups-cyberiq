from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
required=["README.md","WRITEUPS.md","SKILLS.md","TOOLS.md","SECURITY.md","CONTRIBUTING.md","data/progress.json","templates/WRITEUP-TEMPLATE.md","templates/QUALITY-CHECKLIST.md","docs/METHODOLOGY.md"]
errors=[f"missing: {p}" for p in required if not (root/p).exists()]
try:
 data=json.loads((root/"data/progress.json").read_text(encoding="utf-8"))
 if not isinstance(data,dict): errors.append("progress.json must contain an object")
 elif not isinstance(data.get("tracks"),dict): errors.append("progress.json tracks must be an object")
 else:
  for track,counts in data["tracks"].items():
   if not isinstance(counts,dict): errors.append(f"track {track} must contain count fields"); continue
   for key,value in counts.items():
    if not isinstance(value,int) or value<0: errors.append(f"track {track}.{key} must be a non-negative integer")
except Exception as exc: errors.append(f"invalid progress.json: {exc}")
case_docs=list((root/"web").glob("*.md"))+list((root/"crypto").glob("*.md"))+list((root/"forensics").glob("*.md"))
for p in case_docs:
 text=p.read_text(encoding="utf-8",errors="replace")
 if p.name.lower()=="readme.md": continue
 if "Authorization" not in text and "authorized" not in text.lower(): errors.append(f"missing authorization/scope language: {p.relative_to(root)}")
 if "Defensive Takeaway" not in text and "defensive" not in text.lower(): errors.append(f"missing defensive takeaway: {p.relative_to(root)}")
for p in root.rglob("*.md"):
 text=p.read_text(encoding="utf-8",errors="replace")
 if "BEGIN PRIVATE KEY" in text or "ghp_" in text: errors.append(f"possible secret marker: {p.relative_to(root)}")
if errors:
 print("\n".join(errors)); sys.exit(1)
print("portfolio validation passed")
