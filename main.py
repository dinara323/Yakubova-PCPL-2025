# main.py
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any
from operator import itemgetter

@dataclass
class Computer:
    id: int
    model: str
    processor: str
    ram_gb: int

@dataclass
class Browser:
    id: int
    name: str
    version: str
    memory_usage: int
    computer_id: int

@dataclass
class ComputerBrowser:
    computer_id: int
    browser_id: int


def generate_data() -> tuple[List[Computer], List[Browser], List[ComputerBrowser]]:
    """Функция для генерации тестовых данных"""
    computers: List[Computer] = [
        Computer(1, 'Dell XPS 15', 'Intel i7', 16),
        Computer(2, 'HP Pavilion', 'AMD Ryzen 5', 8),
        Computer(3, 'Lenovo ThinkPad', 'Intel i5', 16),
        Computer(4, 'Apple MacBook Pro', 'M1 Pro', 32),
        Computer(5, 'ASUS ROG', 'Intel i9', 64),
    ]

    browsers: List[Browser] = [
        Browser(1, 'Chrome', '120.0', 512, 1),
        Browser(2, 'Firefox', '115.0', 256, 2),
        Browser(3, 'Edge', '119.0', 384, 3),
        Browser(4, 'Safari', '17.0', 128, 4),
        Browser(5, 'Opera', '105.0', 192, 5),
        Browser(6, 'Chrome', '121.0', 520, 2),
        Browser(7, 'Firefox', '116.0', 265, 3),
        Browser(8, 'Arc', '1.0', 320, 1),
    ]

    computer_browsers: List[ComputerBrowser] = [
        ComputerBrowser(1, 1),
        ComputerBrowser(1, 8),
        ComputerBrowser(2, 2),
        ComputerBrowser(2, 6),
        ComputerBrowser(3, 3),
        ComputerBrowser(3, 7),
        ComputerBrowser(4, 4),
        ComputerBrowser(5, 5),
        ComputerBrowser(1, 2),
        ComputerBrowser(3, 1),
    ]

    return computers, browsers, computer_browsers


def get_one_to_many(computers: List[Computer], browsers: List[Browser]) -> List[Tuple[str, str, int, str, str]]:
    """Получение связи один-ко-многим"""
    return [
        (b.name, b.version, b.memory_usage, c.model, c.processor)
        for c in computers
        for b in browsers
        if b.computer_id == c.id
    ]


def get_many_to_many(computers: List[Computer], browsers: List[Browser], 
                     computer_browsers: List[ComputerBrowser]) -> List[Tuple[str, str, int, str, str]]:
    """Получение связи многие-ко-многим"""
    temp = [
        (c.model, c.processor, cb.computer_id, cb.browser_id)
        for c in computers
        for cb in computer_browsers
        if c.id == cb.computer_id
    ]

    return [
        (b.name, b.version, b.memory_usage, comp_model, comp_processor)
        for comp_model, comp_processor, comp_id, browser_id in temp
        for b in browsers if b.id == browser_id
    ]


def find_browsers_starting_with_a(one_to_many: List[Tuple[str, str, int, str, str]]) -> List[Tuple[str, str, int, str, str]]:
    """Поиск браузеров, начинающихся с 'A'"""
    res = [
        (browser_name, version, memory, comp_model, processor)
        for browser_name, version, memory, comp_model, processor in one_to_many
        if browser_name.startswith('A')
    ]
    return sorted(res, key=itemgetter(0))


def find_computers_min_memory(one_to_many: List[Tuple[str, str, int, str, str]]) -> List[Tuple[str, int]]:
    """Поиск минимального использования памяти для каждого компьютера"""
    computer_memory_dict: Dict[str, List[int]] = {}
    
    for _, _, memory, comp_model, _ in one_to_many:
        if comp_model not in computer_memory_dict:
            computer_memory_dict[comp_model] = []
        computer_memory_dict[comp_model].append(memory)
    
    res: List[Tuple[str, int]] = []
    for comp_model, memories in sorted(computer_memory_dict.items()):
        min_memory = min(memories)
        res.append((comp_model, min_memory))
    
    return sorted(res, key=itemgetter(1))


def print_table(data: List[Any], headers: List[str], title: str) -> None:
    """Функция для вывода данных в виде таблицы"""
    print(f"\n{title}")
    print("=" * 50)
    print(" | ".join(f"{header:<20}" for header in headers))
    print("-" * 50)
    
    for row in data:
        print(" | ".join(f"{str(item):<20}" for item in row))


def main() -> None:
    """Основная функция программы"""
    computers, browsers, computer_browsers = generate_data()
    
    one_to_many = get_one_to_many(computers, browsers)
    many_to_many = get_many_to_many(computers, browsers, computer_browsers)
    
    print('Задание В1')
    first_res = find_browsers_starting_with_a(one_to_many)
    if first_res:
        print_table(first_res, ["Браузер", "Версия", "Память", "Компьютер", "Процессор"], 
                   'Браузеры, начинающиеся с "А":')
    else:
        print('Браузеры, начинающиеся с "А": не найдены')
    
    print('\nЗадание В2')
    second_res = find_computers_min_memory(one_to_many)
    print_table(second_res, ["Компьютер", "Мин. память"], 
               'Компьютеры с минимальной памятью браузеров:')
    
    print('\nЗадание В3')
    third_res = sorted(many_to_many, key=itemgetter(0))
    print_table(third_res, ["Браузер", "Версия", "Память", "Компьютер", "Процессор"], 
               'Все связанные браузеры и компьютеры:')


if __name__ == '__main__':
    main()