# CyberIQ Tool Map

A compact map of tools already represented in documented CyberIQ practice. Tools are selected for a specific evidence question rather than used automatically.

| Tool / Technique | Track | Purpose in CTF work | Evidence produced |
|---|---|---|---|
| Browser / HTTP client | Web | Inspect supplied challenge resources and responses | Request/response observations |
| robots.txt review | Web | Review crawler directives and disclosed challenge paths | Disclosed path |
| Python | Crypto / General | Reproducible transformations and validation | Scripted derivation |
| RsaCtfTool | Crypto | Test known RSA CTF weakness conditions | Candidate/recovered values to validate |
| EXIF inspection | Forensics | Read embedded image metadata | Metadata fields |
| Spectrogram | Forensics | Visualize frequency-domain audio content | Derived visual evidence |
| binwalk | Forensics | Identify embedded signatures/content | Offset/signature observations |
| foremost | Forensics | Recover recognizable files from supplied artifacts | Derived files |

## Selection Rule
Start from the question, not the tool:

```text
Evidence question → smallest suitable tool → preserve output → validate conclusion
```

A large command list is not evidence of a strong investigation. Reproducible reasoning is.
\n## Crosslinks\n- [Knowledge Base](KNOWLEDGE-BASE.md)\n- [Methodology](docs/METHODOLOGY.md)\n- [Writeup Index](WRITEUPS.md)\n- [Skills](SKILLS.md)\n