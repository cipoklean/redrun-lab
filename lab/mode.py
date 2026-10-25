"""Reads the mode this run is configured for."""

import os


def app_mode() -> str:
    """The deployment mode, which the workflow supplies."""
    return os.environ["LAB_APP_MODE"]
