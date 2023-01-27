class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.__name = name
        self.__surname = surname
        self.__rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.__rating
        elif isinstance(other, ChessPlayer):
            return other.__rating == self.__rating
        raise NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.__rating > other
        elif isinstance(other, ChessPlayer):
            return self.__rating > other.__rating
        raise NotImplemented

    def __ge__(self, other):
        return self.__rating >= other.__rating


