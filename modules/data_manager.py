import json
import os


PRODUCT_FILE = "data/products.json"
ORDER_FILE = "data/orders.json"


def load_products():
    try:
        with open(PRODUCT_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_products(products):
    os.makedirs("data", exist_ok=True)

    with open(PRODUCT_FILE, "w") as file:
        json.dump(products, file, indent=4)


def load_orders():
    try:
        with open(ORDER_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_orders(orders):
    os.makedirs("data", exist_ok=True)

    with open(ORDER_FILE, "w") as file:
        json.dump(orders, file, indent=4)