class City:

    def __init__(self, name: str):
        if isinstance(name, str):
            self.__name = ' '.join([name_.capitalize() for name_ in name.split()])

        else:
            raise ValueError("Принимает только строки")

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Экземпляр класса City - {self.__name}"

    def __bool__(self):
        return not self.__name[-1] in ("aeiou")


