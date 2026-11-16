# Maintaining this profile

The profile uses native Markdown links and tables, with repository-owned SVG images. No external stats server, model API key, JavaScript embed, scheduled job or tracking image is required.

Regenerate the six theme-aware images with Python 3:

```sh
python scripts/build_assets.py
```

SVG motion honors `prefers-reduced-motion`; the page remains readable if animation is unavailable. Images are illustrations, not application screenshots or measured telemetry. Both light and dark assets are selected through GitHub's supported `<picture>` markup.

`contributions.json` records the statuses checked while preparing the README. Update both that file and the visible status date when checking PRs again. A merged PR is distinct from an open PR or an accepted historical commit.

RepoLens and Practical Agent Skills are local builds without a linked public repository at the time of this profile update. Add public links only after verifying the destination. No local filesystem paths or unpublished source code belong in the public README.

Keep descriptions tied to reproducible behavior. Evaluation fixtures, prototypes and local labs do not establish production performance or general model accuracy.
