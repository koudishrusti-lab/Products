import pytest
from product import get_product_details

def test_get_product_details():
    # sample data
    product_id = "P101"
    name = "Laptop"
    quantity = "5"
    price = "55000"

    # expected result
    expected_output = (
        f"Product ID: {product_id}, Name: {name}, Quantity: {quantity}, Price: {price}"
    )

    # assertion
    assert get_product_details(product_id, name, quantity, price) == expected_output