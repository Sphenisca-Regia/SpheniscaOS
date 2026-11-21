# SPDX-License-Identifier: MPL-2.0
# ruff: noqa: F821 -- snap.py execs this with win/app in scope
view = win.dialer_view
view.show_page("keypad")
try:
    view.keypad.set_digits("61455501")
except Exception:
    pass
