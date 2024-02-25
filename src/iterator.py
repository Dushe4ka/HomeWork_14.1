from src.classes import Category
from src.classes import Product


class IteratorClass:

    def __init__(self, cat: Category):
        self.__products = cat.products
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration()
