# Case File — Structure of AES
**Status:** VERIFIED REFERENCE
**Platform:** CryptoHack
**Track:** Symmetric Ciphers / How AES Works
**Official source:** https://cryptohack.org/challenges/aes/

## Objective
Understand the AES state representation and the transformations used by AES-128.

## Investigation path
1. Represent a 16-byte block as the challenge state.
2. Track AddRoundKey, SubBytes, ShiftRows and MixColumns.
3. Preserve byte ordering during conversions.
4. Validate within CryptoHack.

## Defensive takeaway
Use maintained cryptographic libraries for production systems; hand-written AES is best kept for education and research.

## Evidence confidence
**CONFIRMED**.
