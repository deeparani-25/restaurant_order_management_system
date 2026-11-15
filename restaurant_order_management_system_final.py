"""
Restaurant Order Management System
PS No.: 31
Project: Restaurant Order Management System
Language: Python 3

This console application allows a waiter to select a table, take orders
from a fixed menu, view the running order, and generate a final bill.

Menu:
    Burger = Rs. 100
    Pizza  = Rs. 200
    Coffee = Rs. 50

Charges:
    Service charge = 10% of subtotal
    GST            = 5% of subtotal

Tables:
    1 to 20
"""


MENU = {
    "Burger": 100.0,
    "Pizza": 200.0,
    "Coffee": 50.0
}

SERVICE_CHARGE_RATE = 0.10
GST_RATE = 0.05
MIN_TABLE = 1
MAX_TABLE = 20


def display_menu():
    """Display the restaurant menu."""
    print("\n========== MENU ==========")
    for item, price in MENU.items():
        print(f"{item:<10} Rs. {price:.2f}")
    print("===========================")


def get_table_number():
    """Read and validate a table number from 1 to 20."""
    while True:
        try:
            table = int(input("Enter table number (1-20): "))

            if MIN_TABLE <= table <= MAX_TABLE:
                return table

            print("Invalid table number. Enter a number between 1 and 20.")

        except ValueError:
            print("Invalid table number. Enter a number between 1 and 20.")


def get_menu_item():
    """Read and validate an item name from the menu."""
    while True:
        item = input("Order item: ").strip()

        # Match the entered item without changing the menu dictionary keys.
        for menu_item in MENU:
            if item.lower() == menu_item.lower():
                return menu_item

        available_items = ", ".join(MENU.keys())
        print(f"Item not on the menu. Available: {available_items}")


def get_quantity():
    """Read and validate a positive whole-number quantity."""
    while True:
        try:
            quantity = int(input("Quantity: "))

            if quantity > 0:
                return quantity

            print("Invalid quantity. Enter a whole number.")

        except ValueError:
            print("Invalid quantity. Enter a whole number.")


def add_orders(table_orders, table_number):
    """
    Take one or more items for the selected table.

    Each order is stored as a tuple:
        (item_name, quantity)
    """
    while True:
        display_menu()

        item = get_menu_item()
        quantity = get_quantity()

        amount = MENU[item] * quantity
        table_orders.append((item, quantity))

        print(
            f"{item} x{quantity} added to Table {table_number} | "
            f"Amount: {amount:.0f}"
        )

        another = input("Add another item? (y/n): ").strip().lower()

        if another != "y":
            break


def calculate_subtotal(table_orders):
    """Calculate the subtotal of all items in a table's order."""
    subtotal = 0.0

    for item, quantity in table_orders:
        subtotal += MENU[item] * quantity

    return subtotal


def view_running_order(table_orders, table_number):
    """Display all currently ordered items for the selected table."""
    print(f"\n========== RUNNING ORDER - TABLE {table_number} ==========")

    if not table_orders:
        print("No items ordered yet.")
        print("==========================================================")
        return

    for item, quantity in table_orders:
        amount = MENU[item] * quantity
        print(f"{item} x{quantity} = {amount:.0f}")

    subtotal = calculate_subtotal(table_orders)
    print(f"Current subtotal: Rs. {subtotal:.2f}")
    print("==========================================================")


def generate_bill(table_orders, table_number):
    """Generate and display the final bill."""
    if not table_orders:
        print("No order found. Add an item before generating the bill.")
        return

    print(f"\n================ FINAL BILL - TABLE {table_number} ================")

    for item, quantity in table_orders:
        amount = MENU[item] * quantity
        print(f"{item} x{quantity} = {amount:.0f}")

    subtotal = calculate_subtotal(table_orders)
    service_charge = subtotal * SERVICE_CHARGE_RATE
    gst = subtotal * GST_RATE
    total = subtotal + service_charge + gst

    print("------------------------------------------------------------------")
    print(f"Subtotal:             {subtotal:.2f}")
    print(f"Service charge (10%): {service_charge:.2f}")
    print(f"GST (5%):             {gst:.2f}")
    print(f"Total:                {total:.2f}")
    print("==================================================================")


def show_main_menu():
    """Display the main application menu."""
    print("\n========== RESTAURANT ORDER MANAGEMENT SYSTEM ==========")
    print("1. View Menu")
    print("2. Add Order")
    print("3. View Running Order")
    print("4. Generate Final Bill")
    print("5. Change Table")
    print("6. Exit")
    print("=========================================================")


def main():
    """
    Main program.

    table_orders is a dictionary where:
        key   = table number
        value = list of ordered items for that table
    """
    table_orders = {
        table: []
        for table in range(MIN_TABLE, MAX_TABLE + 1)
    }

    print("Welcome to the Restaurant Order Management System!")

    current_table = get_table_number()
    print(f"Table {current_table} selected.")

    while True:
        show_main_menu()

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid choice. Enter a number from 1 to 6.")
            continue

        if choice == 1:
            display_menu()

        elif choice == 2:
            add_orders(table_orders[current_table], current_table)

        elif choice == 3:
            view_running_order(table_orders[current_table], current_table)

        elif choice == 4:
            generate_bill(table_orders[current_table], current_table)

        elif choice == 5:
            current_table = get_table_number()
            print(f"Table {current_table} selected.")

        elif choice == 6:
            print("Thank you! Restaurant Order Management System closed.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
