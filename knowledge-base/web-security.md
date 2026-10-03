# Web Security Concepts

## Information Disclosure
Information disclosure occurs when an application exposes details that were not intended to be useful to an untrusted visitor. In CTFs this can be deliberate; in production it can reveal paths, technologies, identifiers, or operational details.

### Analyst questions
1. What was directly disclosed?
2. Is the disclosed information actually sensitive or merely descriptive?
3. Does it identify a reachable resource inside scope?
4. Can the observation be reproduced without broadening scope?

### Defensive controls
Use authentication and authorization for sensitive resources, review public metadata, avoid publishing secrets in crawler directives, and minimize unnecessary implementation details.

## Fingerprint ≠ Vulnerability
A server or framework version is evidence about software identity. It is not by itself evidence that a specific vulnerability is reachable or exploitable.

A defensible workflow is:
```text
Fingerprint → affected-version check → component/configuration check
            → reachable code-path evidence → controlled validation
```

This distinction is used in the RedCastle investigation record.
