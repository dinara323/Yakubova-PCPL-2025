class FigureColor:
    """Класс Цвет фигуры"""
    
    def __init__(self):
        self._color = None
    
    @property
    def color(self):
        """Геттер для цвета"""
        return self._color
    
    @color.setter
    def color(self, value):
        """Сеттер для цвета"""
        self._color = value