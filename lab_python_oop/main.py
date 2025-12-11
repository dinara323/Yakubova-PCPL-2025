from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = 23
    
    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")
    
    print(rectangle)
    print(circle)
    print(square)
    
    try:
        from colorama import Fore, Style, init
        init()  # Инициализация colorama
        print(Fore.CYAN + "\nЭто сообщение выведено с использованием внешнего пакета colorama!" + Style.RESET_ALL)
    except ImportError:
        print("\nПакет colorama не установлен. Установите его: pip install colorama")

if __name__ == "__main__":
    main()