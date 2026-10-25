"""Row formatting."""


def format_row(name: str, amount: float) -> str:
    """One `name: amount` line."""
    return f"{name}: {amount:.2f}"
