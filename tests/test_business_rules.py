from business_rules import (
    requires_prepayment,
    calculate_bean_cost,
    get_bulk_discount,
    calculate_shipment_total,
)
def test_calculate_bean_cost():
    """Check the original bean cost."""
    assert calculate_bean_cost(14.0, 10) == 140.0


def test_no_discount():
    assert get_bulk_discount(19) == 0.0


def test_medium_discount():
    assert get_bulk_discount(20) == 0.09


def test_large_discount():
    assert get_bulk_discount(80) == 0.14


def test_partner_discount():
    assert round(get_bulk_discount(25, True), 2) == 0.13

def test_shipment_with_shipping():
    assert calculate_shipment_total(14.0, 10) == 175.0


def test_shipment_without_shipping():
    assert round(calculate_shipment_total(13.0, 40), 2) == 473.20


def test_partner_shipment():
    assert round(calculate_shipment_total(12.0, 50, True), 2) == 522.00


def test_shipping_fee_boundary():
    assert calculate_shipment_total(250.0, 1) == 250.0

def test_prepayment_boundary():
    assert requires_prepayment(1500.0) is True