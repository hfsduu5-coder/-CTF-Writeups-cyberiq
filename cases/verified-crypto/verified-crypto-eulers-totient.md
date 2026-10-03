# Case File — Euler's Totient

**Status:** VERIFIED REFERENCE  
**Platform:** CryptoHack  
**Track:** RSA / Starter  
**Official source:** https://cryptohack.org/challenges/rsa/

## Objective
Understand why knowing RSA's prime factors makes it possible to compute the totient used in private-key derivation.

## Evidence
The exact challenge name is present in CryptoHack's official RSA Starter sequence.

## Investigation path
1. Start from the supplied RSA prime factors.
2. Apply the totient relation for a product of two distinct primes.
3. Preserve the exact integer arithmetic.
4. Validate only against the challenge environment.

## Security concept
Exposure or recovery of RSA's factors collapses the trapdoor assumption: the totient becomes computable and private-key recovery follows.

## Defensive takeaway
Generate strong independent primes, protect private key material, and avoid implementations that leak information about factors.

## Evidence confidence
**CONFIRMED**.
