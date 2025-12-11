class FigureColor:

    def __init__(self, color: str = None):
        self._color = color

    def get_color(self) -> str:
        return self._color

    def set_color(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Поле цвета не может быть пустым")
        self._color = value