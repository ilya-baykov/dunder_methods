class UnitedKingdom:

    @staticmethod
    def capital():
        print("London is the capital of Great Britain")

    @staticmethod
    def language():
        print("English is the primary language of Great Britain")


class Spain:
    @staticmethod
    def capital():
        print("Madrid is the capital of Spain")

    @staticmethod
    def language():
        print("Spanish is the primary language of Spain")


if __name__ == '__main__':

    UK = UnitedKingdom()
    Sp_n = Spain()

    data = [UnitedKingdom(), Spain()]
    for country in data:
        country.capital()
        country.language()
