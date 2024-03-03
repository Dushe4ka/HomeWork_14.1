from src.classes import Product


class Smartphone(Product):
    performance: float
    model: str
    memory: str
    color: str

    def __init__(self, performance, model, memory, color, name, description, price, quantity_in_stock):
        super().__init__(name, description, price, quantity_in_stock)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class Lawn_Grass(Product):
    country: str
    period: str
    color: str

    def __init__(self, country, period, color, name, description, price, quantity_in_stock):
        super().__init__(name, description, price, quantity_in_stock)
        self.country = country
        self.period = period
        self.color = color


