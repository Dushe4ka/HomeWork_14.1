from classes import Category
from Order import Order


class ZeroQuantityException(Exception):
    def __init__(self, message="Quantity should be greater than zero"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
