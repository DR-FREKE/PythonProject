
from abc import ABC, abstractmethod


# this is an interface
class JOSNify(ABC):

    # this shouldn't have any body definition
    @abstractmethod
    def toJson(self):
        pass


# this is an abstract class with an abstract method
class GraphicShape(ABC):

    def __init__(self):
        super().__init__()

    # this shouldn't have any body definition
    @abstractmethod
    def calcArea():
        pass


# implements the JSONify interface and extends the GraphicShape abstract class
# and because it implements the interface, it must implement the toJson function same as the abstract class
class DrawCircle(GraphicShape, JOSNify):
    def __init__(self, radius):
        self.radius = radius

    # implements the calcArea function by force
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    # implements the toJson function from the interface by force
    def toJson():
        pass


class DrawSquare(GraphicShape):
    def __init__(self, side):
        self.side = side

    # implements the calcArea function by force
    def calcArea(self):
        return self.side * self.side


circle = DrawCircle(10)
print(circle.calcArea())
