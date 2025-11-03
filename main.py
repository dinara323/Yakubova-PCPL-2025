from enum import Enum
from operator import itemgetter

class Computer:
    __slots__ = ('id', 'model', 'processor', 'ram_gb')
    
    def __init__(self, id: int, model: str, processor: str, ram_gb: int) -> None:
        self.id: int = id
        self.model: str = model
        self.processor: str = processor
        self.ram_gb: int = ram_gb

class Browser:
    __slots__ = ('id', 'name', 'version', 'memory_usage', 'computer_id')
    
    def __init__(self, id: int, name: str, version: str, memory_usage: int, computer_id: int) -> None:
        self.id: int = id
        self.name: str = name
        self.version: str = version
        self.memory_usage: int = memory_usage
        self.computer_id: int = computer_id

class ComputerBrowser:
    __slots__ = ('computer_id', 'browser_id')
    
    def __init__(self, computer_id: int, browser_id: int) -> None:
        self.computer_id: int = computer_id
        self.browser_id: int = browser_id

computers: list[Computer] = [
    Computer(1, 'Dell XPS 15', 'Intel i7', 16),
    Computer(2, 'HP Pavilion', 'AMD Ryzen 5', 8),
    Computer(3, 'Lenovo ThinkPad', 'Intel i5', 16),
    Computer(4, 'Apple MacBook Pro', 'M1 Pro', 32),
    Computer(5, 'ASUS ROG', 'Intel i9', 64),
]

browsers: list[Browser] = [
    Browser(1, 'Chrome', '120.0', 512, 1),
    Browser(2, 'Firefox', '115.0', 256, 2),
    Browser(3, 'Edge', '119.0', 384, 3),
    Browser(4, 'Safari', '17.0', 128, 4),
    Browser(5, 'Opera', '105.0', 192, 5),
    Browser(6, 'Chrome', '121.0', 520, 2),
    Browser(7, 'Firefox', '116.0', 265, 3),
    Browser(8, 'Arc', '1.0', 320, 1),
]

computer_browsers: list[ComputerBrowser] = [
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

def main() -> None:
    # Связь один ко многим
    one_to_many: list[tuple[str, str, int, str, str]] = [
        (b.name, b.version, b.memory_usage, c.model, c.processor)
        for c in computers
        for b in browsers
        if b.computer_id == c.id
    ]

    # Временная таблица для связи многие ко многим
    temp: list[tuple[str, str, int, int]] = [
        (c.model, c.processor, cb.computer_id, cb.browser_id)
        for c in computers
        for cb in computer_browsers
        if c.id == cb.computer_id
    ]

    # Связь многие ко многим
    many_to_many: list[tuple[str, str, int, str, str]] = [
        (b.name, b.version, b.memory_usage, comp_model, comp_processor)
        for comp_model, comp_processor, comp_id, browser_id in temp
        for b in browsers if b.id == browser_id
    ]

    print('Задание В1')
    first_res: list[tuple[str, str, int, str, str]] = find_browsers_starting_with_a(one_to_many)
    print('Браузеры, у которых название начинается с буквы "А":')
    for browser_name, version, memory, comp_model, processor in first_res:
        print(f'{browser_name} {version} - {memory} МБ - {comp_model} ({processor})')

    print()

    print('Задание В2')
    second_res: list[tuple[str, int]] = find_computers_min_memory(one_to_many)
    print('Компьютеры с минимальной памятью браузеров:')
    for comp_model, min_memory in second_res:
        print(f'{comp_model}: {min_memory} МБ')

    print()

    print('Задание В3')
    third_res = sorted(many_to_many, key=itemgetter(0))
    print('Все связанные браузеры и компьютеры:')
    for browser_name, version, memory, comp_model, processor in third_res:
        print(f'{browser_name} {version} - {memory} МБ - {comp_model} ({processor})')

def find_browsers_starting_with_a(one_to_many: list[tuple[str, str, int, str, str]]) -> list[tuple[str, str, int, str, str]]:
    res: list[tuple[str, str, int, str, str]] = [
        (browser_name, version, memory, comp_model, processor)
        for browser_name, version, memory, comp_model, processor in one_to_many
        if browser_name.startswith('A')
    ]
    return sorted(res, key=itemgetter(0))

def find_computers_min_memory(one_to_many: list[tuple[str, str, int, str, str]]) -> list[tuple[str, int]]:
    computer_memory_dict: dict[str, list[int]] = {}
    
    for browser_name, version, memory, comp_model, processor in one_to_many:
        if comp_model not in computer_memory_dict:
            computer_memory_dict[comp_model] = []
        computer_memory_dict[comp_model].append(memory)
    
    res: list[tuple[str, int]] = []
    for comp_model, memories in sorted(computer_memory_dict.items()):
        min_memory = min(memories)
        res.append((comp_model, min_memory))
    
    return sorted(res, key=itemgetter(1))

if __name__ == '__main__':
    main()