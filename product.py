class Product:
    def __init__(self, product_id, product_name, price, stock):        
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.update_stock(stock)

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__product_name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

product1 = Product("P005", "Laptop", 1200.00, 15)

print(product1.get_stock())

product1.update_stock(25)
print(product1.get_stock())