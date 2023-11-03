# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
from collections import defaultdict


class Factorial:

    def __init__(self):
        self.results = defaultdict(list)
        self.termkresults = []
        self.kresults = []

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.results[number].append(result)
        self.termkresults.append(result)
        if number < len(self.termkresults):
            for i in range(len(self.termkresults)) - number, len(self.termkresults):
                self.kresults.append(self.termkresults[i])
        else:
            for i in range(0, len(self.termkresults)):
                self.kresults.append(self.termkresults[i])

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.results.items())) + "\n" + '\n'.join((f' {v}' for v in self.kresults))
        return txt


factor = Factorial()

factor(1)
factor(10)
factor(6)

print(factor)