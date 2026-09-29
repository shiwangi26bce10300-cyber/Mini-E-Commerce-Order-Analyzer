from modules.order_manager import find_order_by_id


def test_order_search():
    order = find_order_by_id("O001")

    assert order is not None


def test_invalid_order_search():
    order = find_order_by_id("O999")

    assert order is None


print("Order tests passed!")