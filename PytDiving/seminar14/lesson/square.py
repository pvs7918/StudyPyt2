class Square:

    def __init__(self, a, b=None):
        self.a = a
        if b:
            self.b = b
        else:
            self.b = a

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)