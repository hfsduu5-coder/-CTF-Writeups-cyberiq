# Case File — Round Keys
**Status:** VERIFIED REFERENCE
**Platform:** CryptoHack
**Track:** Symmetric Ciphers / How AES Works
**Official source:** https://cryptohack.org/challenges/aes/

## Objective
Understand how AES mixes round-key material into the state.

## Investigation path
1. Preserve state and round-key layout.
2. Apply byte-wise XOR for AddRoundKey.
3. Convert the state back to the expected byte form.
4. Validate in the authorized challenge.

## Defensive takeaway
Key scheduling and state handling are security-critical; production code should rely on audited implementations.

## Evidence confidence
**CONFIRMED**.
