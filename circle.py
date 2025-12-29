import math
from geometric_figure import GeometricFigure
from color import FigureColor

class Circle(GeometricFigure):
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return (
            "{}: радиус = {}, цвет = {}, площадь = {:.2f}"
            .format(
                self.figureName(),
                self.radius,
                self.color.color,
                self.area()
            )
        )
