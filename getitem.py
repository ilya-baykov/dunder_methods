class Data:
    def __init__(self, dictionary: dict):
        self.data = dictionary

    def __repr__(self):
        return f"{self.data}"

    def __getitem__(self, item):
        if isinstance(item, (int, str, float)):
            if item in self.data:
                return self.data[item]
            else:
                raise ValueError(f"Такого ключа нет в {Data}")
        else:
            raise ValueError("Может быть только int,str,float")

    def __setitem__(self, key, value):
        if isinstance(key, (int, str, float)):
            self.data[key] = value
        else:
            raise ValueError("Недопустимый тип")

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]


