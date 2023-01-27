class City:

    def __init__(self, name: str):
        if isinstance(name, str):
            self.__name = ' '.join([name_.capitalize() for name_ in name.split()])

        else:
            raise ValueError("Принимает только строки")

    @property
    def name(self):
        return self.__name

