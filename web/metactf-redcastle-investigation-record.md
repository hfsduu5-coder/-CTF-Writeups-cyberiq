# RedCastle Web Challenge — Investigation Record

> **Status:** Partial historical record. This document deliberately stops where preserved evidence stops.

## Challenge Information
- **Environment:** MetaCTF lab
- **Category:** Web
- **Service:** Python/Werkzeug-based challenge service observed on TCP/7100
- **Authorization:** CTF/lab environment
- **Known application label:** RedCastle

## Preserved Observations
During the authorized challenge investigation, the service identified itself as a Python web application using Werkzeug. The application presented a login surface. A challenge clue also directed attention toward the Python service and a known-vulnerability theme.

A separate MetaCTF investigation in this portfolio involved a `robots.txt` path disclosure. That evidence is documented in its own writeup and is intentionally **not attributed to RedCastle** here because the preserved RedCastle record does not prove the two observations belonged to the same challenge instance.

## Evidence Classification
- **Observed:** Python/Werkzeug service in the challenge environment.
- **Observed:** Login surface associated with RedCastle.
- **Observed:** Challenge clue referenced Python and a known vulnerability.
- **Not attributed here:** The separately documented `robots.txt` path disclosure belongs to another preserved investigation record unless future evidence proves otherwise.
- **Unknown:** The exact vulnerability ultimately intended by the challenge.
- **Unknown:** The final exploit chain and flag value.

## Analyst Reasoning
The correct next step in a preserved investigation would be to identify the exact framework/application version and compare the challenge's behavior and hints against applicable known issues. A version string alone is not proof that a vulnerability is exploitable; the affected component, configuration, reachable code path, and challenge evidence must align.

Because the original final evidence is not preserved here, this repository does **not** reconstruct or invent an exploit chain.

## Lessons Learned
- Separate service fingerprinting from vulnerability confirmation.
- Treat version-based vulnerability matches as hypotheses until application behavior confirms them.
- Preserve request/response evidence while solving so a future writeup can be independently reproduced.
- CTF documentation is stronger when unknowns remain explicitly unknown.

## Defensive Takeaway
Production services should minimize unnecessary version disclosure, keep frameworks and dependencies patched, and avoid relying on obscurity for sensitive routes. Vulnerability management should validate actual exposure rather than treating every version match as confirmed exploitation.

---
**CyberIQ • CTF / Lab / Authorized Security Education**
