# Case Metadata Standard

Every CyberIQ case or writeup should make its evidence status understandable without requiring the reader to infer certainty.

## Required metadata

- **Status:** complete, partial historical record, practice note, or reference-only.
- **Category:** Web, Cryptography, Forensics, OSINT, Reverse Engineering, or Misc.
- **Authorization / Scope:** identify the CTF, lab, training environment, or other authorized context.
- **Evidence confidence:** separate observed facts from hypotheses and unknowns.
- **Defensive takeaway:** explain what a defender or developer can learn from the case.

## Evidence language

Use **Observed** only for information preserved in the case record. Use **Hypothesis** for interpretations that still need validation. Use **Unknown** when the original evidence is missing. Never reconstruct flags, exploit chains, rankings, challenge results, or technical facts from memory when repository evidence does not support them.

## Cross-case isolation

Evidence from one challenge must not be copied into another challenge record merely because the investigations happened around the same time. Cross-links are welcome, but attribution must remain explicit.

## Sensitive data

Do not commit credentials, private target information, API keys, session tokens, or unnecessary live flags. Use synthetic or reserved examples where a demonstration needs sample data.
