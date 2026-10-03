# Case File — Private Keys

**Status:** VERIFIED REFERENCE  
**Platform:** CryptoHack  
**Track:** RSA / Starter  
**Official source:** https://cryptohack.org/challenges/rsa/

## Objective
Connect the public exponent and Euler totient to RSA private-key derivation.

## Investigation path
1. Compute the totient from the known prime factors.
2. Find the modular multiplicative inverse of the public exponent modulo the totient.
3. Treat the resulting private exponent as sensitive material.
4. Validate in the authorized lab.

## Security concept
RSA's private exponent is mathematically related to the public exponent through modular inversion, but deriving it should require secret factorization data.

## Defensive takeaway
Private-key confidentiality is fundamental. Use vetted cryptographic libraries rather than implementing production RSA primitives manually.

## Evidence confidence
**CONFIRMED** — exact challenge verified on CryptoHack.
