# Robots.txt Path Discovery — MetaCTF Lab

## Challenge Information
- **Platform/Event:** MetaCTF challenge environment
- **Category:** Web
- **Target used during the challenge:** `host3.metaproblems.com`
- **Authorization:** CTF/lab environment
- **Objective:** Discover content intentionally hidden through challenge clues.

## Initial Observations
Service enumeration during the challenge showed multiple isolated web services. One HTTP service exposed a `robots.txt` file containing a disallowed path:

```text
/secret-robot-3099a500f658ef87/
```

## Methodology
The key lesson was that `robots.txt` is not an access-control mechanism. In a CTF, entries can deliberately disclose challenge paths. The investigation therefore treated the disallowed entry as a clue and inspected that path inside the authorized lab.

## Tools
- Browser / HTTP client — inspect the challenge web service.
- `robots.txt` — identify the challenge-provided disallowed path.

## Evidence
The challenge's `robots.txt` disclosed the secret-looking directory above. No brute force or credential attack was required for this step.

## Solution
Follow the path disclosed by `robots.txt` on the same CTF web service and inspect the returned challenge content.

## Flag
`REDACTED`

## Lessons Learned
- `robots.txt` communicates crawler preferences; it does not protect sensitive resources.
- Enumeration should begin with simple, low-noise application metadata before complex techniques.
- A challenge can reward understanding of information disclosure rather than exploitation.

## Defensive Takeaway
Never place sensitive paths, credentials, backup locations, or administrative secrets in `robots.txt`. Protect resources with real authentication and authorization.

---
**CyberIQ • CTF / Lab / Authorized Security Education**
