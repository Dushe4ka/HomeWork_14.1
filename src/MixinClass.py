class MixinLog:

    def __init__(self, *args, **kwargs):
        """
        Функция печатает информацию для разработчика
        какой объект был создан и с какими свойствами
        """
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for key, value in self.__dict__.items():
            object_attributes += f"{key}: {value}, "
        return f"создан объект со свойствами {object_attributes}"
