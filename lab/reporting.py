"""Reporting rows. PEP 604 unions mean this needs Python 3.10 or newer."""

from dataclasses import dataclass, field


@dataclass
class Row:
    label: str
    amount: float | None = None
    tags: list[str] = field(default_factory=list)


def describe(row: Row) -> str:
    if row.amount is None:
        return f"{row.label}: n/a"
    return f"{row.label}: {row.amount:.2f}"
