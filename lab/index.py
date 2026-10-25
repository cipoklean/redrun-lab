"""Index building for the search page."""


def build_index(rows: list[str]) -> dict[str, int]:
    """Map each row to its position."""
    return {row: position for position, row in enumerate(rows)}
