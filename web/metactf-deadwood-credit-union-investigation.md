# Deadwood Credit Union — MetaCTF Investigation Record

> **Status:** Partial historical record. Only preserved observations are documented; no exploit or flag is reconstructed.

## Challenge Information
- **Platform/Event:** MetaCTF challenge environment
- **Category:** Web
- **Application label:** Deadwood Credit Union
- **Observed service:** TCP/5990
- **Authorization:** CTF/lab environment

## Preserved Observations
The challenge exposed a login-only web application. During the authorized investigation, the service identified itself with **Werkzeug 2.0.3** and **Python 3.6.9**.

The login form requested a **5-digit member ID** and a **password**.

Historical investigation notes recorded that no useful robots.txt, sitemap, obvious API, or hidden path was found during the checks performed at that time.

## Evidence Confidence
- **Observed:** Deadwood Credit Union login surface.
- **Observed:** TCP/5990 challenge service.
- **Observed:** Werkzeug 2.0.3 / Python 3.6.9 identification.
- **Observed:** 5-digit member ID plus password input model.
- **Observed:** Historical checks did not reveal a useful robots/sitemap/API/hidden path.
- **Unknown:** Intended vulnerability.
- **Unknown:** Final solution chain.
- **Unknown:** Flag.

## Analyst Reasoning
The preserved evidence is enough to describe the application surface, but not enough to claim a vulnerability. A framework version can guide research, yet version identification alone does not establish exploitability.

The absence of a discovery result is also evidence: it helps explain why an analyst would change hypotheses rather than repeatedly enumerate the same paths.

## Lessons Learned
- Record negative findings; they prevent duplicated work.
- Authentication-field structure is an observation, not proof of an authentication flaw.
- Separate technology fingerprinting from vulnerability confirmation.
- Preserve exact request/response evidence during the challenge when possible.

## Defensive Takeaway
Production applications should keep dependencies patched, minimize unnecessary version disclosure, enforce robust authentication controls, and monitor repeated authentication or enumeration behavior.

---
**CyberIQ • CTF / Lab / Authorized Security Education**
