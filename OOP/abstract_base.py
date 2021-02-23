# implement a drawing program that lets a user create 2 dimensional type of shapes
# to make a class an abstract class we need to import from abc package

from abc import ABC, abstractmethod


class GraphicShape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class DrawCircle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    # implements the calcArea function by force
    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class DrawSquare(GraphicShape):
    def __init__(self, side):
        self.side = side

    # implements the calcArea function by force
    def calcArea(self):
        return self.side * self.side


c1 = DrawCircle(10)
print(c1.calcArea())

s1 = DrawSquare(20)
print(s1.calcArea())
