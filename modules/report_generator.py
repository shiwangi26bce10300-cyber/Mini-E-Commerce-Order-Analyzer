import os

from modules.data_manager import (
    load_products,
    load_orders
)

from modules.sales_analyzer import (
    calculate_total_sales,
    calculate_total_items,
    find_best_selling_product
)


def generate_sales_report():

    orders = load_orders()

    placed_orders = []

    for order in orders:
        if order["status"] == "PLACED":
            placed_orders.append(order)

    total_sales = calculate_total_sales()
    total_items = calculate_total_items()

    if len(placed_orders) > 0:
        average_order = total_sales / len(placed_orders)
    else:
        average_order = 0

    best_product = find_best_selling_product()

    report = ""

    report += "MINI E-COMMERCE SALES REPORT\n"
    report += "============================\n\n"

    report += "Total Orders: " + str(len(placed_orders)) + "\n"
    report += "Total Items Sold: " + str(total_items) + "\n"
    report += "Total Sales: ₹" + str(round(total_sales, 2)) + "\n"
    report += "Average Order Value: ₹" + str(
        round(average_order, 2)
    ) + "\n"

    report += "Best Selling Product: " + str(best_product) + "\n"

    os.makedirs("reports", exist_ok=True)

    with open("reports/sales_report.txt", "w") as file:
        file.write(report)

    print("Sales report generated successfully.")
    print("Saved at: reports/sales_report.txt")


def generate_product_report():

    products = load_products()

    total_stock_value = 0
    low_stock_products = []

    for product in products:

        total_stock_value += (
            product["price"] * product["stock"]
        )

        if product["stock"] <= 5:
            low_stock_products.append(product["name"])

    report = ""

    report += "PRODUCT REPORT\n"
    report += "==============\n\n"

    report += "Total Products: " + str(len(products)) + "\n"

    report += (
        "Total Stock Value: ₹"
        + str(round(total_stock_value, 2))
        + "\n\n"
    )

    report += "Low Stock Products:\n"

    if len(low_stock_products) == 0:
        report += "None\n"
    else:
        for product in low_stock_products:
            report += "- " + product + "\n"

    os.makedirs("reports", exist_ok=True)

    with open("reports/product_report.txt", "w") as file:
        file.write(report)

    print("Product report generated successfully.")
    print("Saved at: reports/product_report.txt")


def generate_order_report():

    orders = load_orders()

    report = ""

    report += "ORDER REPORT\n"
    report += "============\n\n"

    for order in orders:

        report += "Order ID: " + order["id"] + "\n"
        report += "Customer: " + order["customer"] + "\n"
        report += "Status: " + order["status"] + "\n"

        total = 0

        for item in order["items"]:
            total += item["price"] * item["quantity"]

        report += "Order Total: ₹" + str(round(total, 2)) + "\n"
        report += "--------------------------\n"

    os.makedirs("reports", exist_ok=True)

    with open("reports/order_report.txt", "w") as file:
        file.write(report)

    print("Order report generated successfully.")
    print("Saved at: reports/order_report.txt")