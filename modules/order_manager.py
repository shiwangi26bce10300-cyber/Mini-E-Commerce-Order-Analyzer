from modules.data_manager import (
    load_orders,
    save_orders,
    load_products,
    save_products
)

from modules.validation import validate_quantity


def generate_order_id():
    orders = load_orders()

    if len(orders) == 0:
        return "O001"

    last_order = orders[-1]

    number = int(last_order["id"][1:])
    number = number + 1

    return "O" + str(number).zfill(3)


def find_order_by_id(order_id):
    orders = load_orders()

    for order in orders:
        if order["id"] == order_id:
            return order

    return None


def calculate_order_total(order):
    total = 0

    for item in order["items"]:
        total = total + item["price"] * item["quantity"]

    return total


def view_orders():
    orders = load_orders()

    if len(orders) == 0:
        print("No orders available.")
        return

    print("\n--------------- ORDERS ---------------")

    for order in orders:

        print("Order ID:", order["id"])
        print("Customer:", order["customer"])
        print("Status:", order["status"])

        total = calculate_order_total(order)

        print("Total: ₹", total)

        print("--------------------------------------")


def add_order():
    products = load_products()

    customer = input("Enter customer name: ")

    if customer.strip() == "":
        print("Customer name cannot be empty.")
        return

    product_id = input("Enter product ID: ")

    selected_product = None

    for product in products:

        if product["id"] == product_id:
            selected_product = product
            break

    if selected_product is None:
        print("Product not found.")
        return

    quantity = input("Enter quantity: ")

    if not validate_quantity(quantity):
        print("Invalid quantity.")
        return

    quantity = int(quantity)

    if quantity > selected_product["stock"]:
        print("Not enough stock available.")
        return

    order = {
        "id": generate_order_id(),
        "customer": customer,
        "status": "PLACED",
        "items": [
            {
                "product_id": selected_product["id"],
                "product_name": selected_product["name"],
                "price": selected_product["price"],
                "quantity": quantity
            }
        ]
    }

    orders = load_orders()
    orders.append(order)

    selected_product["stock"] = (
        selected_product["stock"] - quantity
    )

    save_orders(orders)
    save_products(products)

    print("\nOrder placed successfully!")
    print("Order ID:", order["id"])
    print("Total: ₹", calculate_order_total(order))