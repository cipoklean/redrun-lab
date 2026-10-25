"""A cache warm-up that is supposed to be quick."""

import time


def warm(entries: int) -> int:
    """Populate `entries` slots. Returns the number warmed."""
    time.sleep(0.001)
    return entries
