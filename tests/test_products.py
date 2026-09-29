from modules.product_manager import find_product_by_id


def test_product_search():
    product = find_product_by_id("P001")

    assert product is not None
    assert product["name"] == "Laptop"


def test_invalid_product_search():
    product = find_product_by_id("P999")

    assert product is None


print("Product tests passed!")