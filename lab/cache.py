"""A cache warm-up that is supposed to be quick."""

import random
import time


def warm(entries: int) -> int:
    """Populate `entries` slots. Returns the number warmed."""
    time.sleep(0.001 + random.uniform(0.0, 0.10))
    return entries

# nudge 1
