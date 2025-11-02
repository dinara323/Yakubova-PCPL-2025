from queries import get_one_to_many, get_many_to_many, query1, query2, query3

def main():
    """Основная функция"""
    one_to_many = get_one_to_many()
    many_to_many = get_many_to_many()

    print('Задание В1')
    res1 = query1(one_to_many)
    print(res1)

    print('\nЗадание В2')
    res2 = query2(one_to_many)
    print(res2)

    print('\nЗадание В3')
    res3 = query3(many_to_many)
    print(res3)

if __name__ == '__main__':
    main()