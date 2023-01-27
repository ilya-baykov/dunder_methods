class Addition:
    def __call__(self, *args, **kwargs):
        print(f"Сумма переданных значений = {sum([arg for arg in args if isinstance(arg, (int, float))])}")


if __name__ == "__main__":
    add = Addition()
    add(10, 20)
    add(1, 2, 3.4)
    add(1, 2, "hELLO", [1, 2], 3)
