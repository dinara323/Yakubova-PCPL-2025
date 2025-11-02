from operator import itemgetter
from data import langs, constructs, langs_constructs

def get_one_to_many():
    """Соединение данных один-ко-многим"""
    return [(c.name, c.complexity, l.name)
            for l in langs
            for c in constructs
            if c.lang_id == l.id]

def get_many_to_many():
    """Соединение данных многие-ко-многим"""
    many_to_many_temp = [(l.name, lc.lang_id, lc.construct_id)
                        for l in langs
                        for lc in langs_constructs
                        if l.id == lc.lang_id]
    
    return [(c.name, c.complexity, lang_name)
            for lang_name, lang_id, construct_id in many_to_many_temp
            for c in constructs if c.id == construct_id]

def query1(one_to_many):
    """Запрос 1: Синтаксические конструкции, начинающиеся на 'f'"""
    return list(filter(lambda i: i[0].startswith('f'), one_to_many))

def query2(one_to_many):
    """Запрос 2: Языки с минимальной сложностью конструкций"""
    res_unsorted = []
    for l in langs:
        l_constructs = list(filter(lambda i: i[2] == l.name, one_to_many))
        if l_constructs:
            complexities = [comp for _, comp, _ in l_constructs]
            res_unsorted.append((l.name, min(complexities)))
    
    return sorted(res_unsorted, key=itemgetter(1))

def query3(many_to_many):
    """Запрос 3: Все связанные конструкции и языки, отсортированные по конструкциям"""
    return sorted(many_to_many, key=itemgetter(0))