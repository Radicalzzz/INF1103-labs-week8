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

# Only run the following code if this script is executed directly (not imported)
if __name__ == "__main__":
    inventory = Inventory()
    product1 = Product("P005", "Laptop", 1200.00, 15)
    inventory.add_product(product1)

    found_product = inventory.search_product("P009")
    if found_product is not None:
        print("Product found:", found_product.get_product_id())
    else:
        print("Product not found.")
        
    inventory.display_all()