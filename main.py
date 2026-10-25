import json

from product import Product
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return inventory        

    for product_data in data:
        product = Product(
            product_data["id"],
            product_data["name"],
            product_data["price"],
            product_data["stock"]
        )
        inventory.add_product(product)
    return inventory

def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        product_data = {
            "id": product.get_product_id(),
            "name": product.get_product_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }
        data.append(product_data)

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

def add_product(inventory):
    product_name = input("Enter the product name: ").strip()
    if not product_name:
        raise ValueError("Product name cannot be empty.")

    price = float(input("Enter the product price: "))
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
    quantity = int(input("Enter the product quantity: "))
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    # Placeholder for generating a unique product ID
    number = 1

    while inventory.search_product(f"P{number:03d}") is not None:
        number += 1

    product_id = f"P{number:03d}"
    product = Product(product_id, product_name, price, quantity)
    inventory.add_product(product)
    save_inventory(inventory)

    print(f"Product '{product_name}' added successfully with ID: {product_id}")

def update_stock(inventory):
    product_id = input("Enter the product ID to update stock: ").strip().upper()

    product = inventory.search_product(product_id)
    if product is None:
        print(f"Product with ID '{product_id}' not found.")
        return

    new_stock = int(input(f"Enter the new stock quantity for '{product.get_product_name()}': "))
    if new_stock < 0:
        raise ValueError("Stock quantity cannot be negative.")

    product.update_stock(new_stock)
    save_inventory(inventory)

    print(f"Stock for product '{product.get_product_name()}' updated to {new_stock}.")

def search_product(inventory):
    product_id = input("Enter the product ID to search: ").strip().upper()

    product = inventory.search_product(product_id)
    if product is None:
        print(f"Product with ID '{product_id}' not found.")
        return
    else:
        print("Product found:")
        product.display_information()

def main():
    inventory = load_inventory()

    while True:
        print("\n============================")
        print("Inventory Management System")
        print("============================")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("\nEnter option: ").strip()

        try:
            if choice == "1":
                inventory.display_all()
            elif choice == "2":
                add_product(inventory)
            elif choice == "3":
                update_stock(inventory)
            elif choice == "4":
                search_product(inventory)
            elif choice == "5":
                save_inventory(inventory)
                print("\nInventory saved successfully.")
            elif choice == "6":
                save_inventory(inventory)
                print("\nInventory saved successfully.")
                print("Thank you for using Inventory Management System.")
                break

            else:
                print("\nInvalid option. Please choose a valid option from 1 to 6.")

        except ValueError as error:
            print(f"\nInvalid input: {error}")

if __name__ == "__main__":
    main()