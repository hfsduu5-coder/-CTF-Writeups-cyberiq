# Case File — Public Keys

**Status:** VERIFIED REFERENCE  
**Platform:** CryptoHack  
**Track:** RSA / Starter  
**Official source:** https://cryptohack.org/challenges/rsa/

## Objective
Model the RSA public key as the modulus and public exponent, then apply the public operation to a message representative.

## Evidence
CryptoHack's official RSA index lists **Public Keys** in its Starter sequence. This is a reference case, not a personal-completion claim.

## Investigation path
1. Form the modulus from the supplied prime factors when the exercise provides them.
2. Use the public exponent.
3. Apply modular exponentiation to the message.
4. Check the resulting ciphertext in the authorized challenge environment.

## Security concept
The public key is intentionally distributable; secrecy belongs to the private key and its underlying factors.

## Defensive takeaway
RSA deployments require adequate modulus sizes, secure key generation, modern padding, and separation of public and private material.

## Evidence confidence
**CONFIRMED** — official platform reference.
