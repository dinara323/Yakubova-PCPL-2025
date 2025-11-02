from models import ProgrammingLanguage, SyntaxConstruct, LangConstruct

# Языки программирования
langs = [
    ProgrammingLanguage(1, 'Python'),
    ProgrammingLanguage(2, 'JavaScript'),
    ProgrammingLanguage(3, 'Java'),
    ProgrammingLanguage(4, 'C++'),
    ProgrammingLanguage(5, 'TypeScript'),
]

# Синтаксические конструкции
constructs = [
    SyntaxConstruct(1, 'if-else', 2, 1),
    SyntaxConstruct(2, 'for loop', 3, 1),
    SyntaxConstruct(3, 'function', 4, 2),
    SyntaxConstruct(4, 'class', 5, 3),
    SyntaxConstruct(5, 'lambda', 3, 1),
    SyntaxConstruct(6, 'arrow function', 3, 2),
    SyntaxConstruct(7, 'interface', 4, 5),
]

# Связь многие-ко-многим
langs_constructs = [
    LangConstruct(1, 1),
    LangConstruct(1, 2),
    LangConstruct(1, 5),
    LangConstruct(2, 3),
    LangConstruct(2, 6),
    LangConstruct(3, 4),
    LangConstruct(4, 1),
    LangConstruct(4, 2),
    LangConstruct(4, 4),
    LangConstruct(5, 3),
    LangConstruct(5, 6),
    LangConstruct(5, 7),
]