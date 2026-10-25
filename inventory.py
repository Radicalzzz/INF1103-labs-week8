from product import Product

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return
        
        print("\nCurrent Inventory:")
        print("-------------------------------------------------------")

        for product in self.__products:
            product.display_information()

        print("-------------------------------------------------------")

inventory = Inventory()
product1 = Product("P005", "Laptop", 1200.00, 15)
inventory.add_product(product1)
inventory.display_all()