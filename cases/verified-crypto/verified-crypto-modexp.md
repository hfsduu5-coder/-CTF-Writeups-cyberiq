# Case File — Modular Exponentiation

**Status:** VERIFIED REFERENCE  
**Platform:** CryptoHack  
**Track:** RSA / Starter  
**Official source:** https://cryptohack.org/challenges/rsa/

## Objective
Understand modular exponentiation, the arithmetic primitive used throughout RSA.

## Evidence
- The challenge appears in CryptoHack's official RSA challenge index.
- CryptoHack describes RSA operations in terms of modular exponentiation.
- This repository does **not** claim personal completion.

## Investigation path
1. Identify base, exponent, and modulus.
2. Compute the modular power with an efficient modular-exponentiation routine.
3. Validate the result against the challenge interface.

## Security concept
Modular exponentiation is efficient in the forward direction; RSA combines it with the hardness of recovering hidden structure such as prime factors.

## Defensive takeaway
Cryptographic strength does not come from hiding the algorithm. It depends on sound parameter generation, key protection, and correct protocol use.

## Evidence confidence
**CONFIRMED** — challenge name and track verified from the official CryptoHack source.
