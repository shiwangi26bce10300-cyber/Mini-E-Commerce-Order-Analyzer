from modules.data_manager import load_orders


def get_placed_orders():
    orders = load_orders()

    placed_orders = []

    for order in orders:
        if order["status"] == "PLACED":
            placed_orders.append(order)

    return placed_orders


def calculate_total_sales():
    orders = get_placed_orders()

    total = 0

    for order in orders:

        for item in order["items"]:
            total = total + item["price"] * item["quantity"]

    return total


def calculate_total_items():
    orders = get_placed_orders()

    total_items = 0

    for order in orders:

        for item in order["items"]:
            total_items = total_items + item["quantity"]

    return total_items


def find_best_selling_product():
    orders = get_placed_orders()

    product_sales = {}

    for order in orders:

        for item in order["items"]:

            name = item["product_name"]
            quantity = item["quantity"]

            if name in product_sales:
                product_sales[name] = (
                    product_sales[name] + quantity
                )
            else:
                product_sales[name] = quantity

    if len(product_sales) == 0:
        return "No sales"

    best_product = None
    highest_quantity = 0

    for product in product_sales:

        if product_sales[product] > highest_quantity:
            highest_quantity = product_sales[product]
            best_product = product

    return best_product


def show_sales_analysis():

    orders = get_placed_orders()

    if len(orders) == 0:
        print("No sales available.")
        return

    total_sales = calculate_total_sales()
    total_items = calculate_total_items()

    average_order_value = total_sales / len(orders)

    best_product = find_best_selling_product()

    print("\n========== SALES ANALYSIS ==========")

    print("Total Orders:", len(orders))
    print("Total Items Sold:", total_items)
    print("Total Sales: ₹", round(total_sales, 2))
    print(
        "Average Order Value: ₹",
        round(average_order_value, 2)
    )
    print("Best Selling Product:", best_product)

    print("====================================")