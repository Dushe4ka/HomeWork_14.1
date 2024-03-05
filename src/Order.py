from abc import ABC, abstractmethod
from MixinClass import MixinLog

"""класс «Заказ», в котором будет ссылка на то, какой товар был куплен, количество купленного товара, 
а также итоговая стоимость. В заказе может быть указан только один товар."""


class OrderItem(ABC):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def calculate_total(self):
        pass


class OrderCategory(ABC):
    @abstractmethod
    def method(self):
        pass


class Order(OrderItem, OrderCategory, MixinLog):
    def __init__(self, product, quantity, total_cost):
        super().__init__(product, quantity)
        self.total_cost = total_cost

    def calculate_total(self):
        return self.product.price * self.quantity

    def method(self):
        print(f"Some method for {self.product}")

    def __repr__(self):
        return f"Order ({repr(self.product)}, {self.quantity}, {self.total_cost})"
