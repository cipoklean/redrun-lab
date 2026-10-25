"""Order pricing."""

from decimal import Decimal

FREE_SHIPPING_OVER = Decimal("50.00")
STANDARD_SHIPPING = Decimal("4.99")
EXPRESS_SURCHARGE = Decimal("9.99")


def order_total(subtotal: Decimal, express: bool = False) -> Decimal:
    """Subtotal plus shipping; shipping is free over the threshold."""
    shipping = Decimal("0.00") if subtotal >= FREE_SHIPPING_OVER else STANDARD_SHIPPING
    if express:
        shipping += EXPRESS_SURCHARGE
    return (subtotal + shipping).quantize(Decimal("0.01"))
