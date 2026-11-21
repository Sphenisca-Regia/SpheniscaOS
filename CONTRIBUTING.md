# Contributing to xx-os

Small fixes: open a PR. Anything bigger (a new app, a new D-Bus interface, a
change to how the shell owns a surface): open an issue first so nobody builds
the wrong thing.

## Where things live

Each top-level directory is its own meson project with its own `tests/`,
`README.md` and version. `common/` is shared code (`xx_ui`, `xx_phone`), not an
app. How the apps talk to each other and to the shell is in
[`docs/dbus.md`](docs/dbus.md). The shell's direction and open work are in
[`xx-wm/design.md`](xx-wm/design.md) and [`xx-wm/todo.md`](xx-wm/todo.md).

## Set up

On Arch, `scripts/ci-setup.sh` installs everything CI uses (read it first, it
runs `pacman -Syu`). On other distros you need: Python 3, PyGObject, GTK4,
libadwaita, gtk4-layer-shell, meson, ninja, Rust, and Xvfb for the widget
tests.

```sh
python3 -m venv --system-site-packages .venv && .venv/bin/pip install pytest ruff
sh scripts/check-all.sh          # every project's tests + lint
sh scripts/check-all.sh txxt     # just one
```

To reproduce CI exactly:

```sh
podman run --rm -v "$PWD":/src:ro archlinux:latest sh /src/scripts/ci-setup.sh --run
```

## The rules CI enforces

- **Tests and ruff pass** for every project you touched.
- **Bump the version** of any app whose behavior you changed, in the same PR:
  `python3 scripts/app_versions.py bump <app> [patch|minor|major]`. It edits
  the app's `meson.build` and regenerates `apps.json`. A change to `common/`
  bumps `common`. Details in [`docs/versioning.md`](docs/versioning.md).

## The rules a reviewer enforces

- **Test on a device when it touches hardware.** Calls, SMS, suspend, the modem,
  the lock screen, touch feel. Say which phone and OS in the PR. If you only had
  a VM, say that.
- **Phone-first.** Every screen works at 360×720 and still reads at 320 px wide.
- **Text over icons.** Black background, one accent, monospace for values. No
  icon grids.
- **UI copy is plain.** Buttons are a verb and an object ("Delete 3 notes",
  not "OK"). Errors name the thing and say what to do. Empty states are one line.
- **Nothing phones home.** No telemetry, no analytics, no network call the user
  didn't ask for. If a feature needs a server, it's the user's server.

## Commits

Imperative subject, no prefix ceremony: `xx-dialer: ring through a repeat
caller during DnD`. The body says what changed, why, and how you verified it.
One logical change per commit.

## License

xx-os is GPL-3.0. By sending a PR you agree your contribution is released under
the same license.
