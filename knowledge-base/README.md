# CyberIQ CTF Knowledge Base

The Knowledge Base connects challenge writeups to reusable security concepts. It is intentionally evidence-driven: concepts may be documented broadly, but a challenge is linked only when the repository contains supporting material.

## Knowledge Map

| Concept | Track | What to recognize | Validation mindset | Defensive lesson | Related material |
|---|---|---|---|---|---|
| Information disclosure | Web | Public metadata reveals unintended application details | Confirm the disclosed resource exists and is relevant to scope | Do not expose secrets through public metadata | [MetaCTF robots.txt](../web/metactf-robots-path-discovery.md) |
| Version fingerprinting | Web | Framework/server identifiers appear in responses or banners | A version match is a hypothesis, not proof of exploitability | Patch dependencies and minimize unnecessary disclosure | [RedCastle record](../web/metactf-redcastle-investigation-record.md) |
| Metadata leakage | Forensics | Files retain EXIF or other embedded metadata | Correlate fields with challenge evidence | Strip unnecessary metadata before publishing | [Artifact practice](../forensics/artifact-discovery-practice.md) |
| Embedded/recoverable files | Forensics | Container data may hold recognizable file signatures | Hash and separate recovered artifacts | Validate distributed files and sanitize sensitive remnants | [Artifact practice](../forensics/artifact-discovery-practice.md) |
| RSA weakened assumptions | Crypto | Supplied parameters/hints imply a deliberate mathematical weakness | Match conditions before selecting a technique; verify plaintext | Use mature libraries and safe key generation | [RSA notes](../crypto/rsa-practice-notes.md) |

## Analyst Loop

```text
Scope
  ↓
Observe ──→ Preserve Evidence
  ↓
Hypothesis
  ↓
Smallest Valid Test
  ↓
Validate
  ↓
Explain Root Cause
  ↓
Defensive Takeaway
  ↓
Publish / Keep as Practice Note
```

## Confidence Vocabulary
- **Observed** — directly visible in supplied challenge evidence.
- **Derived** — reproducibly produced from observed evidence.
- **Confirmed** — conclusion supported by validation.
- **Unknown** — evidence is insufficient.
- **Hypothesis** — plausible explanation still requiring validation.

## Why this exists
Flags expire as learning artifacts. Reasoning patterns do not. The Knowledge Base turns individual challenges into reusable analyst knowledge without pretending that historical details are known when they were not preserved.
