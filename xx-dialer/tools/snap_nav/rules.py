# SPDX-License-Identifier: MPL-2.0
# ruff: noqa: F821 -- snap.py execs this with win/app in scope
view = win.dialer_view
view.show_page("rules")
try:
    view.rules._win_unknown.emit("clicked")
except Exception:
    pass
