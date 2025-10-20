import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффициента

    Returns:
        float: Коэффициент биквадратного уравнения
    '''
    while True:
        try:
            if len(sys.argv) > index:
                coef_str = sys.argv[index]
                coef = float(coef_str)
                return coef
            else:
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
                return coef
        except (ValueError, IndexError):
            if len(sys.argv) > index:
                print(f"Некорректное значение коэффициента в командной строке. {prompt}")
            continue

def solve_biquadratic(a, b, c):
    '''
    Вычисление действительных корней биквадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        Список корней в форме кортежа
    '''
    if a == 0:
        return ('Error', 'Коэффициент A не может быть равен нулю для биквадратного уравнения')
    
    D = b*b - 4*a*c
    
    if D < 0.0:
        return ('NoRoots',)
    elif D == 0.0:
        y = -b / (2.0 * a)
        if y < 0:
            return ('NoRoots',)
        elif y == 0:
            return ('OneRoot', 0.0)
        else:
            root = math.sqrt(y)
            return ('TwoRoots', root, -root)
    else:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2.0 * a)
        y2 = (-b - sqD) / (2.0 * a)
        
        roots = []
        
        if y1 > 0:
            root1 = math.sqrt(y1)
            root2 = -math.sqrt(y1)
            roots.extend([root1, root2])
        elif y1 == 0:
            roots.append(0.0)
        
        if y2 > 0:
            root3 = math.sqrt(y2)
            root4 = -math.sqrt(y2)
            if not (math.isclose(y1, y2) and y1 > 0):
                roots.extend([root3, root4])
        elif y2 == 0 and 0.0 not in roots:
            roots.append(0.0)
        
        unique_roots = []
        for root in roots:
            if not any(math.isclose(root, ur) for ur in unique_roots):
                unique_roots.append(root)
        
        unique_roots.sort()
        
        if len(unique_roots) == 0:
            return ('NoRoots',)
        elif len(unique_roots) == 1:
            return ('OneRoot', unique_roots[0])
        elif len(unique_roots) == 2:
            return ('TwoRoots', unique_roots[0], unique_roots[1])
        elif len(unique_roots) == 3:
            return ('ThreeRoots', unique_roots[0], unique_roots[1], unique_roots[2])
        else:
            return ('FourRoots', unique_roots[0], unique_roots[1], unique_roots[2], unique_roots[3])

def print_roots(roots_tuple):
    '''
    Печать корней биквадратного уравнения

    Args:
        Список корней в форме кортежа
    '''
    match roots_tuple:
        case ('FourRoots', root1, root2, root3, root4):
            print(f'Четыре корня: {root1}, {root2}, {root3}, {root4}')
        case ('ThreeRoots', root1, root2, root3):
            print(f'Три корня: {root1}, {root2}, {root3}')
        case ('TwoRoots', root1, root2):
            print(f'Два корня: {root1} и {root2}')
        case ('OneRoot', root):
            print(f'Один корень: {root}')
        case ('NoRoots',):
            print('Нет действительных корней')
        case ('Error', message):
            print(f'Ошибка: {message}')

def main():
    '''
    Основная функция
    '''
    print("Решение биквадратного уравнения вида: A*x⁴ + B*x² + C = 0")
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    
    roots = solve_biquadratic(a, b, c)
    
    print_roots(roots)

if __name__ == "__main__":
    main()