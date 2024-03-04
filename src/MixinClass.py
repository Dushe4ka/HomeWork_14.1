class MixinLog:

    def __init__(self):
        pass

    def order_log(self):
        print(f"Объект {self.title} создан, {self.description}, {self.price}, {self.quantity_in_stock}")