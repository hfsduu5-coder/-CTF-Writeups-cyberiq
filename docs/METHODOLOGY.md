# CyberIQ CTF Methodology

A repeatable workflow for authorized CTF and lab challenges. The goal is to make every writeup useful to another learner, not merely record a flag.

## 1. Scope First
Record the platform/event, category, supplied target or artifact, objective, and authorization boundary. Never silently broaden the challenge scope.

## 2. Preserve the Starting Point
For file-based challenges, retain the original artifact and record a cryptographic hash before transformations. For web challenges, preserve the relevant supplied request/response or challenge clue.

## 3. Observe Before Acting
Write down facts separately from hypotheses. Identify technologies, file types, protocols, metadata, error messages, and challenge hints before choosing a technique.

## 4. Form a Hypothesis
State what you think is happening and what evidence would confirm or reject it. Prefer the smallest safe test that can answer the question.

## 5. Reproduce
Keep the meaningful commands, scripts, transformations, or request/response pairs needed to reproduce the result in the authorized environment. Remove noise.

## 6. Validate
Do not accept a result only because it looks plausible. Validate decoded data, recovered artifacts, mathematical results, or application behavior against independent evidence when possible.

## 7. Explain the Root Cause
A strong writeup explains *why* the challenge worked: information disclosure, broken access control, weak cryptographic assumption, metadata leakage, unsafe parsing, or another underlying concept.

## 8. Add the Defender View
End with detection, prevention, or hardening lessons. This turns a CTF solution into reusable security knowledge.

## Evidence Labels
Use these labels when helpful:
- **Observed** — directly present in supplied evidence.
- **Derived** — produced through a documented transformation.
- **Hypothesis** — analyst theory awaiting validation.
- **Confirmed** — independently supported conclusion.

## Publication Gate
Before publishing, confirm that the writeup contains no live credentials, private data, unintended secrets, out-of-scope targets, or fabricated details.

---
**CyberIQ • Evidence-driven CTF methodology**
