from abc import ABC, abstractmethod

class Abstract(ABC):

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def get_quantity_in_stock(self):
        pass