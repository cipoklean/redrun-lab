"""Builds a small text report."""

from lab.format import format_row


def render(rows: list[tuple[str, float]]) -> str:
    return "\n".join(format_row(name, amount) for name, amount in rows)
