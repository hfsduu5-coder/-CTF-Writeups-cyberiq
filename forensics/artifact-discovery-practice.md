# Forensics Practice Notes — Artifact Discovery

## Scope
These notes capture real CTF practice areas previously worked on by CyberIQ. Exact challenge-specific values are intentionally omitted where the original evidence is not currently available.

## Techniques Practiced

### Spectrogram WAV
Audio challenges can hide visual information in frequency content. The workflow is to preserve the supplied WAV, inspect basic metadata, then render a spectrogram and look for structured visual patterns rather than assuming the audible track contains the answer.

### EXIF / GPS
Image challenges may retain EXIF fields such as timestamps, device information, or GPS coordinates. The workflow is to inspect metadata first, record relevant fields as evidence, and correlate only what the challenge requires.

### File Carving
When supplied artifacts contain embedded or deleted content, carving can recover recognizable file signatures. Tools used in prior practice include `binwalk` and `foremost`. Recovered artifacts should be hashed and kept separate from the original evidence.

## Evidence Discipline
- Preserve the original challenge file.
- Record hashes before analysis.
- Work on copies when modification is required.
- Keep extracted files in a separate directory.
- Do not infer a flag or conclusion without supporting artifact evidence.

## Defensive Takeaway
Metadata leakage and embedded content can expose information unintentionally. Strip unnecessary metadata before publication and validate files distributed outside trusted environments.

---
**CyberIQ • CTF / Lab / Authorized Security Education**
