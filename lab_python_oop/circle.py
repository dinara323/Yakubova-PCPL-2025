import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Circle(Figure):
    """Класс Круг"""
    
    FIGURE_TYPE = "Круг"
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.color = color
    
    def square(self):
        return math.pi * self.radius ** 2
    
    @property
    def name(self):
        return self.FIGURE_TYPE
    
    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {:.2f}.'.format(
            self.name,
            self.color.color,
            self.radius,
            self.square()
        )