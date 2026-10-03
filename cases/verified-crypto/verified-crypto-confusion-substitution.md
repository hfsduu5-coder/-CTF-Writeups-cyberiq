# Case File — Confusion through Substitution
**Status:** VERIFIED REFERENCE
**Platform:** CryptoHack
**Track:** Symmetric Ciphers / How AES Works
**Official source:** https://cryptohack.org/challenges/aes/

## Objective
Study the nonlinear substitution step used by AES.

## Investigation path
1. Inspect the S-box mapping.
2. Apply substitution consistently across the state.
3. Preserve byte ordering.
4. Validate in the official exercise.

## Defensive takeaway
Standard cryptographic nonlinear components should not be replaced with unreviewed custom designs.

## Evidence confidence
**CONFIRMED**.
