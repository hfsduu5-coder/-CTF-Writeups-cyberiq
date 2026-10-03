# Case File — Bringing It All Together
**Status:** VERIFIED REFERENCE
**Platform:** CryptoHack
**Track:** Symmetric Ciphers / How AES Works
**Official source:** https://cryptohack.org/challenges/aes/

## Objective
Combine the AES transformations into a complete educational AES-128 flow.

## Investigation path
1. Expand the key into round keys.
2. Apply inverse round operations in the required order.
3. Account for the special final round.
4. Convert the final state to bytes and validate in CryptoHack.

## Defensive takeaway
Understanding internals is valuable for auditing, while production encryption should use authenticated modes and maintained libraries.

## Evidence confidence
**CONFIRMED**.
