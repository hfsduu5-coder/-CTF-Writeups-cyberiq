# RSA CTF Practice Notes

## Scope
CyberIQ has practiced RSA-focused CTF challenges in authorized environments. This document records the reusable analysis workflow without inventing challenge-specific parameters that are not preserved here.

## Methodology
For a supplied RSA challenge, first inventory the values actually provided: modulus `n`, public exponent `e`, ciphertext `c`, and any additional hints or leaked values. Then identify whether the challenge intentionally introduces a mathematical weakness.

The important step is not blindly trying attacks. Match the supplied conditions to the relevant RSA property, validate assumptions, and only then use an appropriate solver or script.

## Tools
- Python — arithmetic and reproducible validation.
- RsaCtfTool — used in prior authorized CTF practice to test known RSA challenge weaknesses.

## Evidence
Record the supplied public parameters, the identified mathematical condition, the exact transformation used, and a final verification step.

## Lessons Learned
- Secure RSA depends on correct key generation and parameter handling.
- CTF RSA problems often teach one deliberately weakened assumption.
- A recovered plaintext should be validated rather than accepted only because it looks readable.

## Defensive Takeaway
Use mature cryptographic libraries and safe key-generation defaults instead of implementing production RSA primitives manually.

---
**CyberIQ • CTF / Lab / Authorized Security Education**
