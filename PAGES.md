# GitHub Pages Deployment

The repository is structurally ready for GitHub Pages: the site entry point is `index.html`, static assets are repository-local, and the Pages-readiness workflow validates the static portfolio.

## Deployment verification

Deployment is considered verified only when the published GitHub Pages endpoint returns the portfolio successfully. Repository structure or a guessed Pages URL is not proof of deployment.

Expected project URL after Pages is enabled for the default branch/root:

`https://hfsduu5-coder.github.io/-CTF-Writeups-cyberiq/`

If the endpoint is unavailable, enable GitHub Pages in repository settings (Deploy from a branch, `main`, root) or configure an official Pages deployment workflow. Do not mark deployment complete until the public endpoint is reachable.
