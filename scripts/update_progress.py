from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def classify(path: Path) -> str:
    text=path.read_text(encoding="utf-8",errors="replace").lower()
    if "partial historical record" in text or "**unknown:**" in text: return "partial"
    if "practice notes" in text or "practice areas" in text: return "practice"
    return "complete"

def main():
    mapping={"web":"Web","crypto":"Cryptography","forensics":"Forensics","osint":"OSINT","reverse-engineering":"Reverse Engineering","misc":"Misc"}
    tracks={label:{"complete":0,"partial":0,"practice":0} for label in mapping.values()}
    for folder,label in mapping.items():
        for p in (ROOT/folder).glob("*.md"):
            if p.name=="README.md": continue
            tracks[label][classify(p)]+=1
    current=json.loads((ROOT/"data/progress.json").read_text(encoding="utf-8"))
    current["tracks"]=tracks
    (ROOT/"data/progress.json").write_text(json.dumps(current,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("Updated data/progress.json")

if __name__=="__main__": main()
