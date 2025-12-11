from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):

    FIGURE_TYPE = "Квадрат"

    def __init__(self, color_parameter, side_parameter):
        if side_parameter <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        self._side = side_parameter
        super().__init__(color_parameter, self._side, self._side)

    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE
    
    def get_side(self) -> float:
        return self._side
    
    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_name(),
            self._figure_color.get_color(),
            self._side,
            self.square()
        )