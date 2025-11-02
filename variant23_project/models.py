class SyntaxConstruct:
    """Синтаксическая конструкция"""
    def __init__(self, id, name, complexity, lang_id):
        self.id = id
        self.name = name
        self.complexity = complexity
        self.lang_id = lang_id

class ProgrammingLanguage:
    """Язык программирования"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LangConstruct:
    """Языки программирования и синтаксические конструкции для связи многие-ко-многим"""
    def __init__(self, lang_id, construct_id):
        self.lang_id = lang_id
        self.construct_id = construct_id