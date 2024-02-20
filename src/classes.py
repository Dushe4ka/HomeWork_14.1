class Category:
    title: str
    description: str
    products: list

    total_numbers_of_category = 0
    unique_products = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.__products = products

        Category.total_numbers_of_category += 1
        Category.unique_products += 1

    def get_name(self):
        return self.title

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products

    @property
    def products(self):
        list_product = []
        for products in self.__products:
            list_product.append(f"{products["name"]}, {products["price"]} руб. Остаток: {products["quantity"]} шт.\n")

        return "".join(list_product)

    def add_products(self, value):
        self.__products.append({
            "name": value[0],
            "description": value[1],
            "price": value[2],
            "quantity": value[3]
        })




class Product:
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self._price = price
        self.quantity_in_stock = quantity_in_stock

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    @property
    def get_price(self):
        return self._price

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена не корректно")
        elif value < self._price:
            while True:
                answer = input("Новая цена ниже чем старая, вы уверены что хотите изменить цену (y/n): ").lower()
                if answer == 'y':
                    self._price = value
                    break
                elif answer == "n":
                    self._price = self._price
                    break
        else:
            self._price = value

    @classmethod
    def create_product(cls, new_product):
        name, description, price, quantity = \
            (
                new_product['name'], new_product['description'], new_product['price'], new_product['quantity']
            )

        return cls(name, description, price, quantity)

