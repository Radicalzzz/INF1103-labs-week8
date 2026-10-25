import json

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(data):
    with open('inventory.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_product():
    data = load_inventory()
    product_name = input("Enter the product name: ").capitalize()
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    product = {
        #:03d, 0 = fill empty spaces with zeros, 3 = use 3 digits, d = integer, 
        'id': f'P{len(data) + 1:03d}',
        'name': product_name,
        'price': price,
        'stock': quantity
    }
    data.append(product)
    save_inventory(data)
    print("Product added successfully!")
    
def display_all():
    data = load_inventory()
    print("\nCurrent Inventory:")
    print("-------------------------------------------------------")

    for product in data:
       print(
            f"ID: {product['id']} |",
            f"Name: {product['name']} |",
            f"Price: ${product['price']:.2f} |", # .2f = 2 decimal places | floating point value
            f"Stock: {product['stock']}"
        )
    print("-------------------------------------------------------")

def search_product():
    data = load_inventory()
    search_name = input("Enter the product ID to search: ").capitalize()

    found_products = [product for product in data if product['id'] == search_name]

    if found_products:
        print("\nSearch Results:")
        print("-------------------------------------------------------")
        for product in found_products:
            print(
                f"ID: {product['id']} |",
                f"Name: {product['name']} |",
                f"Price: ${product['price']:.2f} |",
                f"Stock: {product['stock']}"
            )
        print("-------------------------------------------------------")
    else:
        print("Product not found.")

def update_stock():
    data = load_inventory()
    product_id = input("Enter the product ID to update stock: ").capitalize()

    for product in data:
        if product['id'] == product_id:
            new_stock = int(input(f"Enter the new stock quantity for {product['name']}: "))
            product['stock'] = new_stock
            save_inventory(data)
            print("Stock updated successfully!")
            return
    print("Product not found.")

while True:
    print("\n==================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==================================")

    print("\n----------MENU----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

    choice = input("\nEnter option: ")
    if choice == "1":
        display_all()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_stock()
    elif choice == "4":
        search_product()
    elif choice == "5":
        data = load_inventory()
        save_inventory(data)
        print("\nInventory saved successfully!")
    elif choice == "6":
        data = load_inventory()
        save_inventory(data)
        print("\nSaving Inventory before exiting...", "\nInventory saved successfully.")
        print("\nThank you for using Inventory Management System", "\nProgram terminated.")
        break
    else:
        print("Invalid choice. Please enter a valid option from 1 to 6.")