from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rectangle = Rectangle("синего", 1, 1)
    circle = Circle("зеленого", 1)
    square = Square("красного", 1)
    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()