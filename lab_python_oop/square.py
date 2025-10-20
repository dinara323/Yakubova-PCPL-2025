from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """Класс Квадрат"""
    
    FIGURE_TYPE = "Квадрат"
    
    def __init__(self, side, color):
        # Квадрат - это прямоугольник с равными сторонами
        super().__init__(side, side, color)
    
    @property
    def name(self):
        return self.FIGURE_TYPE
    
    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.name,
            self.color.color,
            self.width,  # или self.height - они равны
            self.square()
        )