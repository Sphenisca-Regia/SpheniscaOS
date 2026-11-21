# SPDX-License-Identifier: MPL-2.0
"""Run the app from a checkout: PYTHONPATH=src python3 -m xx_email."""

from xx_email.main import main

if __name__ == "__main__":
    raise SystemExit(main())
