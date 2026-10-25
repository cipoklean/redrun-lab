"""One-line headline built from summary totals."""

from lab.summary import format_total


def headline(totals: list[float]) -> str:
    return " | ".join(format_total(total) for total in totals)
