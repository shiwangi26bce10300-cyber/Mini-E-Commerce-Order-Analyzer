from modules.product_manager import (
    view_products,
    add_product,
    search_product,
    update_product,
    delete_product,
    sort_products_by_price
)

from modules.order_manager import (
    view_orders,
    add_order
)

from modules.sales_analyzer import show_sales_analysis

from modules.report_generator import (
    generate_sales_report,
    generate_product_report,
    generate_order_report
)


def product_menu():
    while True:
        print("\n========== PRODUCT MANAGEMENT ==========")
        print("1. View Products")
        print("2. Add Product")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Sort Products by Price")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            sort_products_by_price()

        elif choice == "7":
            break

        else:
            print("Invalid choice!")


def order_menu():
    while True:
        print("\n========== ORDER MANAGEMENT ==========")
        print("1. View Orders")
        print("2. Add Order")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_orders()

        elif choice == "2":
            add_order()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


def report_menu():
    while True:
        print("\n========== REPORTS ==========")
        print("1. Sales Report")
        print("2. Product Report")
        print("3. Order Report")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_sales_report()

        elif choice == "2":
            generate_product_report()

        elif choice == "3":
            generate_order_report()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n")
        print("========================================")
        print("       MINI E-COMMERCE ANALYZER")
        print("========================================")
        print("1. Product Management")
        print("2. Order Management")
        print("3. Sales Analysis")
        print("4. Generate Reports")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_menu()

        elif choice == "2":
            order_menu()

        elif choice == "3":
            show_sales_analysis()

        elif choice == "4":
            report_menu()

        elif choice == "5":
            print("Thank you for using Mini E-Commerce Analyzer!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()