# 📌Создайте декоратор с параметром.
# 📌Параметр - целое число, количество запусков декорируемой функции.

def counter(number):
    def dec(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(number):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return dec

@counter(10)
def func(a, b):
    return a + b

print(func(2, 4))