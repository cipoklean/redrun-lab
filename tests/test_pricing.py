from decimal import Decimal

from lab.pricing import order_total


def test_free_shipping_over_the_threshold():
    assert order_total(Decimal("60.00")) == Decimal("60.00")


def test_standard_shipping_under_the_threshold():
    assert order_total(Decimal("10.00")) == Decimal("14.99")


def test_express_adds_a_surcharge():
    assert order_total(Decimal("10.00"), express=True) == Decimal("24.98")
