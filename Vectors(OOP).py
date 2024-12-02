from math import sqrt
# На входе мы подаем любое количество векторов и они сравниваются\складываюся\смотрим чтобы их len был одинаковый и тд
class Vector:
    def __init__(self, *args):
        self.args = args
    def long(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')
    def __str__(self):
        return str(*self.args)

    def __add__(self,other):
        self.long(other)
        if isinstance(other, self.__class__):
            return self.__class__(tuple(sum(i) for i in zip(self.args,other.args)))
        return NotImplemented
    def __sub__(self,other):
        self.long(other)
        if isinstance(other, self.__class__):
            return self.__class__(tuple(a-b for a,b in zip(self.args,other.args)))
        return NotImplemented
    def __mul__(self,other):
        self.long(other)
        if isinstance(other, self.__class__):
            return self.__class__(sum((a*b for a,b in zip(self.args,other.args))))

        return NotImplemented
    def norm(self):
        l = [i**2 for i in self.args]
        return sqrt(sum(l))

    def __eq__(self, other):
        self.long(other)
        if isinstance(other, self.__class__):
            return self.args == other.args
        return NotImplemented
    def __len__(self):
        return len(self.args)


vector1 = Vector(1, 2, 3, 4)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 + vector2)
except ValueError as e:
    print(e)
