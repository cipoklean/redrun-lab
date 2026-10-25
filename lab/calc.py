"""Arithmetic helpers."""

from decimal import Decimal


def total_with_tax(subtotal: Decimal, rate: float) -> Decimal:
    """Subtotal plus tax at `rate`, rounded to whole cents."""
    return (subtotal * Decimal(str(1 + rate))).quantize(Decimal("0.01"))


def split_evenly(amount: Decimal, parts: int) -> list[Decimal]:
    """Split `amount` into `parts` shares; the rounding remainder rides the first."""
    if parts < 1:
        raise ValueError("parts must be at least 1")
    share = (amount / parts).quantize(Decimal("0.01"))
    return [amount - share * (parts - 1)] + [share] * (parts - 1)
