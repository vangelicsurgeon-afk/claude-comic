# Scheduled routine setup

Create the routine at claude.ai/code/routines (New routine → Cloud).

- **Repository:** this repo
- **Environment:** Default (Trusted network is enough; PyPI is allowlisted)
- **Connectors:** remove all. The routine doesn't need any.
- **Schedule:** see the current cadence in the project notes
- **Prompt:**

> Run one production cycle of the webcomic in this repository by following the
> playbook in `pipeline/publish-episode.md` from start
> to finish. You are the comic's sole creator and have full creative control;
> do not ask for input or approval. When finished, commit and push directly to
> the `main` branch with `git push origin HEAD:main`. This is intended, because
> the website deploys from `main:/docs`.
