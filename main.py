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

inventory = Inventory()
inventory = load_inventory()
inventory.display_all()