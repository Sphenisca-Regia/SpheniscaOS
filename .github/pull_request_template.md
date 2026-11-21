## What and why

<!-- One or two sentences. Link the issue if there is one: Fixes #123 -->

## How you verified it

<!-- Tests added or run. Device and OS if it touches hardware, or "VM only". -->

## Checklist

- [ ] `sh scripts/check-all.sh <projects you touched>` passes
- [ ] Bumped the version of every app whose behavior changed (`scripts/app_versions.py bump`)
- [ ] Works at 360×720 and reads at 320 px wide (UI changes)
