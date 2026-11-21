# Third-party notices

SpheniscaOS's own code is under the Mozilla Public License 2.0 (`LICENSE`). The parts below come from other
projects and keep their own licences. Each source file says which licence it is under in its
`SPDX-License-Identifier` line or its own header.

## Kept under the GNU GPL v3 or later

Text: `LICENSES/GPL-3.0-or-later.txt`.

| Path | Origin |
|---|---|
| `xx-keyboard/` | A fork of Stevia (phosh-osk-stevia), the Phosh on-screen keyboard. The whole directory stays GPL-3.0-or-later; its files keep their upstream headers (`xx-keyboard/COPYING`). |
| `xx-keyboard/glide/latinime/` | AOSP LatinIME native decoder, Apache License 2.0, each file with its upstream header (`xx-keyboard/glide/NOTICE`). Linked into the GPL keyboard. |
| `common/xx_phone/mmi.py` | USSD detection and session handling ported from GNOME Calls (`calls-util.c`, `calls-mm-origin.c`). |
| `xx-wm/launcher/data/gnome-osk/us.json` | Colemak layout for GNOME Shell's on-screen keyboard, derived from squeekboard's layouts. |

The MPL-2.0 files in this repository are not marked "Incompatible With Secondary Licenses", so they can be combined
with these GPL parts (MPL-2.0 § 3.3).

## Wayland protocol files

Kept under their own licences (MIT-style), with their copyright lines inside each file:

- `xx-wm/launcher/data/*.xml`: wayland.xml (Kristian Høgsberg, Intel, Collabora), wlr protocols (Simon Ser,
  Andri Yngvason, Ilia Bozhinov), phosh-private.xml and wlr-output-power-management (Purism SPC).
- `xx-wm/wm/protocols/river-*.xml` (Isaac Freund).

## Sounds

`xx-wm/launcher/data/sounds/` holds original sounds synthesized for SpheniscaOS
(`NOTICE-original-sounds.txt`). They are covered by `LICENSE` like the code.

## Dependencies

Python packages, GTK, libadwaita, Rust crates and system libraries are installed separately and keep their own
licences. Nothing from them is vendored in this repository except as listed above.
