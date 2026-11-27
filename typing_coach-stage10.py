# === Stage 10: Поиск по нескольким словам ===
# Project: TypingCoach
def parse_query(query):
    """Разбирает строку поиска упражнения на набор слов с поддержкой исключений.

    Слова, начинающиеся с '-', исключаются из результата. Пустые слова
    (например, после запятой или двоеточия) пропускаются. Возвращается
    список: сначала включаемые слова, затем список исключений.
    """
    query = query.strip()
    if not query:
        return [], []

    tokens = []
    for raw in query.replace(',', ' ').split():
        token = raw
        if token.startswith('-'):
            token = token[1:]
        if token:
            tokens.append(token)

    includes = []
    excludes = []
    for token in tokens:
        if token.startswith('-'):
            excludes.append(token[1:])
        else:
            includes.append(token)

    return includes, excludes


def search_exercises(exercises, includes, excludes):
    """Ищет упражнения по нескольким словам с учётом исключений.

    Упражнение считается найденным, если оно содержит все слова из списка
    includes и не содержит ни одного слова из excludes. Поиск выполняется
    без учёта регистра. Пустой запрос возвращает все упражнения.
    """
    lower_includes = [s.lower() for s in includes]
    lower_excludes = [s.lower() for s in excludes]

    matched = []
    for exercise in exercises:
        fields = (
            exercise.name.lower(),
            exercise.layout.lower(),
            exercise.length.lower(),
            exercise.difficulty.lower(),
        )

        if not all(field in fields for field in lower_includes):
            continue
        if any(field in fields for field in lower_excludes):
            continue

        matched.append(exercise)

    return matched


class Exercise:
    def __init__(self, name, layout, length, difficulty):
        self.name = name
        self.layout = layout
        self.length = length
        self.difficulty = difficulty


if __name__ == '__main__':
    all_exercises = [
        Exercise('Python Basics', 'qwerty', 150, 'easy'),
        Exercise('Russian Text', 'yandex', 300, 'medium'),
        Exercise('Speed Test', 'qwerty', 500, 'hard'),
        Exercise('Code Snippets', 'qwerty', 200, 'medium'),
    ]

    includes, excludes = parse_query('python -code -speed')
    results = search_exercises(all_exercises, includes, excludes)

    for exercise in results:
        print(f"{exercise.name} | {exercise.layout} | {exercise.length} | {exercise.difficulty}")
