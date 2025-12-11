from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
   
    FIGURE_TYPE = "Круг"

    def __init__(self, color_parameter: str,  radius_parameter: float):
        if radius_parameter <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = radius_parameter
        self._figure_color = FigureColor(color_parameter)

    @classmethod
    def get_name(cls) -> str:
        return cls.FIGURE_TYPE
    
    def get_color(self) -> str:
        return self._figure_color.get_color()
    
    def get_radius(self) -> float:
        return self._radius

    def square(self) -> float:
        return math.pi*(self._radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_name(),
            self._figure_color.get_color(),
            self._radius,
            self.square()
        )