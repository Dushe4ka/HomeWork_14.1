from src.classes import Product
from abstract_class import Abstract


class Smartphone(Product, Abstract):
    performance: float
    model: str
    memory: str
    color: str

    def __init__(self, performance, model, memory, color, name, description, price, quantity_in_stock):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity_in_stock)


class Lawn_Grass(Product, Abstract):
    country: str
    period: str
    color: str

    def __init__(self, country, period, color, name, description, price, quantity_in_stock):
        super().__init__(name, description, price, quantity_in_stock)
        self.country = country
        self.period = period
        self.color = color


