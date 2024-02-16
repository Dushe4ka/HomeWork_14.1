class Category:
    title: str
    description: str
    products: list

    total_numbers_of_category = 0
    unique_products = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products

        Category.total_numbers_of_category += 1
        Category.unique_products += 1

    def get_name(self):
        return self.title

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products




class Product:
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity_in_stock(self):
        return self.quantity_in_stock