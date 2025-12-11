from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, color_parameter: str, width_parameter: float, height_parameter: float):
        if width_parameter <= 0 or height_parameter <=0:
            raise ValueError("Ширина и высота должны быть положительными числами")
        self._width = width_parameter
        self._height = height_parameter
        self._figure_color = FigureColor(color_parameter)
    
    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE
    
    def get_color(self):
        return self._figure_color.get_color()
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def square(self):
        return self._width*self._height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_name(),
            self._figure_color.get_color(),
            self._width,
            self._height,
            self.square()
        )