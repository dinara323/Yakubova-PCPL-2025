# test_main.py
import pytest
from main import (
    Computer, Browser, ComputerBrowser,
    generate_data, get_one_to_many, get_many_to_many,
    find_browsers_starting_with_a, find_computers_min_memory
)


@pytest.fixture
def sample_data():
    """Фикстура с тестовыми данными"""
    computers = [
        Computer(1, 'Dell XPS 15', 'Intel i7', 16),
        Computer(2, 'HP Pavilion', 'AMD Ryzen 5', 8),
        Computer(3, 'Lenovo ThinkPad', 'Intel i5', 16),
    ]
    
    browsers = [
        Browser(1, 'Chrome', '120.0', 512, 1),
        Browser(2, 'Firefox', '115.0', 256, 2),
        Browser(3, 'Arc', '1.0', 320, 1),
        Browser(4, 'Avast', '1.0', 200, 3),
    ]
    
    computer_browsers = [
        ComputerBrowser(1, 1),
        ComputerBrowser(1, 3),
        ComputerBrowser(2, 2),
        ComputerBrowser(3, 4),
    ]
    
    return computers, browsers, computer_browsers


def test_generate_data():
    """Тест генерации данных"""
    computers, browsers, computer_browsers = generate_data()
    
    assert len(computers) == 5
    assert len(browsers) == 8
    assert len(computer_browsers) == 10
    
    # Проверка структуры данных
    assert computers[0].id == 1
    assert computers[0].model == 'Dell XPS 15'
    assert browsers[0].name == 'Chrome'
    assert computer_browsers[0].computer_id == 1


def test_get_one_to_many(sample_data):
    """Тест связи один-ко-многим"""
    computers, browsers, _ = sample_data
    one_to_many = get_one_to_many(computers, browsers)
    
    # Должно быть 4 записи
    assert len(one_to_many) == 4
    
    # Проверка структуры данных
    assert one_to_many[0][0] == 'Chrome'
    assert one_to_many[0][3] == 'Dell XPS 15'
    
    # Проверка связей
    dell_browsers = [b for b in one_to_many if b[3] == 'Dell XPS 15']
    assert len(dell_browsers) == 2  # Chrome и Arc


def test_get_many_to_many(sample_data):
    """Тест связи многие-ко-многим"""
    computers, browsers, computer_browsers = sample_data
    many_to_many = get_many_to_many(computers, browsers, computer_browsers)
    
    # Должно быть 4 записи
    assert len(many_to_many) == 4
    
    # Проверка структуры данных
    assert many_to_many[0][0] == 'Chrome'
    assert many_to_many[0][3] == 'Dell XPS 15'


def test_find_browsers_starting_with_a(sample_data):
    """Тест поиска браузеров, начинающихся с 'A'"""
    computers, browsers, _ = sample_data
    one_to_many = get_one_to_many(computers, browsers)
    
    result = find_browsers_starting_with_a(one_to_many)
    
    # Должно найти 2 браузера: Arc и Avast
    assert len(result) == 2
    
    # Проверка сортировки
    assert result[0][0] == 'Arc'
    assert result[1][0] == 'Avast'
    
    # Проверка структуры данных
    assert result[0][2] == 320  # Память для Arc
    assert result[1][3] == 'Lenovo ThinkPad'  # Компьютер для Avast


def test_find_computers_min_memory(sample_data):
    """Тест поиска минимальной памяти для компьютеров"""
    computers, browsers, _ = sample_data
    one_to_many = get_one_to_many(computers, browsers)
    
    result = find_computers_min_memory(one_to_many)
    
    # Должно быть 3 компьютера
    assert len(result) == 3
    
    # Преобразуем результат в словарь для удобной проверки
    result_dict = dict(result)
    
    # Проверяем значения для каждого компьютера
    assert result_dict['HP Pavilion'] == 256
    assert result_dict['Lenovo ThinkPad'] == 200
    assert result_dict['Dell XPS 15'] == 320
    
    # Проверяем, что результаты отсортированы по минимальной памяти
    memory_values = [memory for _, memory in result]
    assert memory_values == [200, 256, 320] or memory_values == sorted(memory_values)


def test_find_browsers_starting_with_a_no_results():
    """Тест случая, когда нет браузеров, начинающихся с 'A'"""
    computers = [Computer(1, 'Test', 'CPU', 8)]
    browsers = [Browser(1, 'Chrome', '1.0', 100, 1)]
    
    one_to_many = get_one_to_many(computers, browsers)
    result = find_browsers_starting_with_a(one_to_many)
    
    # Не должно быть результатов
    assert len(result) == 0


def test_find_computers_min_memory_empty():
    """Тест случая с пустыми данными"""
    result = find_computers_min_memory([])
    
    # Не должно быть результатов
    assert len(result) == 0


def test_find_computers_min_memory_single_computer():
    """Тест с одним компьютером и одним браузером"""
    computers = [Computer(1, 'Test PC', 'CPU', 16)]
    browsers = [Browser(1, 'Browser', '1.0', 150, 1)]
    
    one_to_many = get_one_to_many(computers, browsers)
    result = find_computers_min_memory(one_to_many)
    
    # Должен быть один результат
    assert len(result) == 1
    assert result[0][0] == 'Test PC'
    assert result[0][1] == 150


def test_find_computers_min_memory_multiple_browsers_same_computer():
    """Тест с одним компьютером и несколькими браузерами"""
    computers = [Computer(1, 'Test PC', 'CPU', 16)]
    browsers = [
        Browser(1, 'Browser1', '1.0', 300, 1),
        Browser(2, 'Browser2', '2.0', 150, 1),
        Browser(3, 'Browser3', '3.0', 200, 1),
    ]
    
    one_to_many = get_one_to_many(computers, browsers)
    result = find_computers_min_memory(one_to_many)
    
    # Должен быть один результат с минимальной памятью 150
    assert len(result) == 1
    assert result[0][0] == 'Test PC'
    assert result[0][1] == 150

