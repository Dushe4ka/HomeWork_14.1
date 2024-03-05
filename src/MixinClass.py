class MixinLog:

    def __init__(self, *args, **kwargs):
        """
        Функция печатает информацию для разработчика
        какой объект был создан и с какими свойствами
        """
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__.items})"