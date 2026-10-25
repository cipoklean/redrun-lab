from decimal import Decimal

from lab.calc import split_evenly, total_with_tax


def test_total_with_tax_adds_tax_to_the_subtotal():
    assert total_with_tax(Decimal("100.00"), 0.2) == Decimal("120.00")


def test_split_evenly_keeps_the_total():
    shares = split_evenly(Decimal("10.00"), 3)
    assert sum(shares) == Decimal("10.00")
    assert len(shares) == 3
