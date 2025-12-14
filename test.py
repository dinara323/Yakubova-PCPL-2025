import pytest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.color import FigureColor

class TestFigures:
    @pytest.fixture
    def sample_rectangle(self):
        return Rectangle("синего", 5, 3)
    
    @pytest.fixture
    def sample_circle(self):
        return Circle("зеленого", 4)
    
    @pytest.fixture
    def sample_square(self):
        return Square("красного", 2)
    
    def test_rectangle_creation_and_square(self, sample_rectangle):
        assert sample_rectangle.square() == 15
        assert sample_rectangle.get_color() == "синего"
        assert sample_rectangle.get_width() == 5
        assert sample_rectangle.get_height() == 3

    def test_circle_creation_and_square(self, sample_circle):
        assert sample_circle.square() == pytest.approx(math.pi * 16, 0.01)
        assert sample_circle.get_color() == "зеленого"
        assert sample_circle.get_radius() == 4

    def test_rectangle_creation_and_square_and_isinstance(self, sample_square):
        assert sample_square.square() == 4
        assert sample_square.get_color() == "красного"
        assert sample_square.get_side() == 2
        assert isinstance(sample_square, Rectangle)

    @pytest.mark.parametrize("width,height,expected_error", [
        (-1, 5, "Ширина и высота должны быть положительными числами"),
        (0, 5, "Ширина и высота должны быть положительными числами"),
        (5, -1, "Ширина и высота должны быть положительными числами"),
        (-5, -1, "Ширина и высота должны быть положительными числами"),
    ])

    def test_rectangle_invalid_parameters(self, width, height, expected_error):
        with pytest.raises(ValueError, match=expected_error):
            Rectangle("синего", width, height)

    @pytest.mark.parametrize("radius,expected_error", [
        (-1, "Радиус должен быть положительным числом"),
        (0, "Радиус должен быть положительным числом"),
    ])

    def test_circle_invalid_parameters(self, radius, expected_error):
        with pytest.raises(ValueError, match=expected_error):
            Circle("зеленого", radius)

    @pytest.mark.parametrize("side,expected_error", [
        (-1, "Сторона должна быть положительным числом"),
        (0, "Сторона должна быть положительным числом"),
    ])

    def test_square_invalid_parameters(self, side, expected_error):
        with pytest.raises(ValueError, match=expected_error):
            Square("красного", side)
    
class TestFigureColorTDD:
    def test_color_operations(self):
        color = FigureColor("синий")
        assert color.get_color() == "синий"
        
        color.set_color("красный")
        assert color.get_color() == "красный"

    @pytest.mark.parametrize("color,expected_error", [
        ("", "Поле цвета не может быть пустым"),
        (None, "Поле цвета не может быть пустым"),
    ])
    def test_color_validation(self, color, expected_error):
        color = FigureColor()
        with pytest.raises(ValueError, match=expected_error):
            color.set_color(color)