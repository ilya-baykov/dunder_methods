import time


class Addition:
    def __call__(self, *args, **kwargs):
        print(f"Сумма переданных значений = {sum([arg for arg in args if isinstance(arg, (int, float))])}")


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func()
        finish_time = time.time()
        print(f"Время выполнения Функции {self.func.__name__} составило {finish_time - start_time}c")


@Timer
def calculate():
    for i in range(10_000_000):
        2 ** 100


@Timer
def calculate_2():
    [i for i in range(10_000_000)]


if __name__ == "__main__":
    pass
