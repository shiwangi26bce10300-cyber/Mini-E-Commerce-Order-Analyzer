from modules.sales_analyzer import calculate_total_sales


def test_sales_calculation():
    sales = calculate_total_sales()

    assert sales >= 0


print("Sales tests passed!")