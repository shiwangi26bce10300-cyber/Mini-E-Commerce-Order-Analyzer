from modules.data_manager import load_products, save_products
from modules.validation import (
    validate_non_empty,
    validate_positive_number,
    validate_quantity
)


def find_product_by_id(product_id):
    products = load_products()

    for product in products:
        if product["id"] == product_id:
            return product

    return None


def view_products():
    products = load_products()

    if len(products) == 0:
        print("No products available.")
        return

    print("\n---------------- PRODUCTS ----------------")

    for product in products:
        print("ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: ₹", product["price"])
        print("Stock:", product["stock"])
        print("------------------------------------------")


def add_product():
    products = load_products()

    product_id = input("Enter product ID: ")

    if find_product_by_id(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = input("Enter price: ")
    stock = input("Enter stock quantity: ")

    if not validate_non_empty(name):
        print("Product name cannot be empty.")
        return

    if not validate_non_empty(category):
        print("Category cannot be empty.")
        return

    if not validate_positive_number(price):
        print("Price must be a positive number.")
        return

    if not validate_quantity(stock):
        print("Stock must be a positive number.")
        return

    new_product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": float(price),
        "stock": int(stock)
    }

    products.append(new_product)
    save_products(products)

    print("Product added successfully.")


def search_product():
    keyword = input("Enter product name to search: ")

    products = load_products()
    found = False

    for product in products:
        if keyword.lower() in product["name"].lower():
            print("\nProduct Found")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: ₹", product["price"])
            print("Stock:", product["stock"])

            found = True

    if not found:
        print("Product not found.")


def update_product():
    product_id = input("Enter product ID to update: ")

    products = load_products()

    for product in products:

        if product["id"] == product_id:

            print("Leave input empty if you don't want to change it.")

            new_name = input("Enter new name: ")
            new_price = input("Enter new price: ")
            new_stock = input("Enter new stock: ")

            if new_name != "":
                product["name"] = new_name

            if new_price != "":
                if validate_positive_number(new_price):
                    product["price"] = float(new_price)
                else:
                    print("Invalid price.")
                    return

            if new_stock != "":
                if validate_quantity(new_stock):
                    product["stock"] = int(new_stock)
                else:
                    print("Invalid stock.")
                    return

            save_products(products)

            print("Product updated successfully.")
            return

    print("Product not found.")


def delete_product():
    product_id = input("Enter product ID to delete: ")

    products = load_products()

    for product in products:

        if product["id"] == product_id:
            products.remove(product)

            save_products(products)

            print("Product deleted successfully.")
            return

    print("Product not found.")


def sort_products_by_price():
    products = load_products()

    # Simple Bubble Sort
    for i in range(len(products)):

        for j in range(0, len(products) - i - 1):

            if products[j]["price"] > products[j + 1]["price"]:

                temp = products[j]
                products[j] = products[j + 1]
                products[j + 1] = temp

    print("\nProducts sorted by price:")

    for product in products:
        print(
            product["name"],
            "- ₹",
            product["price"]
        )