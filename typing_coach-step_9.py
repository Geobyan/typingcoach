# === Stage 9: Текстовый поиск ===
# Project: TypingCoach
import re


def highlight_matches(text: str, query: str, *, case_insensitive: bool = True,
                      highlight_char: str = "✓") -> str:
    """Подсвечивает в строке все вхождения запроса.

    Возвращает строку, в которой совпадения заменены на запрос,
    префиксанный символом подсветки. Поиск без учёта регистра
    по умолчанию.
    """
    if not query:
        return text

    flags = re.IGNORECASE if case_insensitive else 0

    def _replace(match: re.Match) -> str:
        return highlight_char + match.group(0)

    return re.sub(re.escape(query), _replace, text, flags=flags)


def find_exercises(name: str, query: str, *, case_insensitive: bool = True) -> list:
    """Фильтрует список упражнений по текстовому полю «название».

    Поиск без учёта регистра по умолчанию. Возвращает новый список,
    содержащий только те упражнения, чьё название совпадает с запросом.
    """
    if not query:
        return list(name)

    flags = re.IGNORECASE if case_insensitive else 0

    def _matches(exercise: dict) -> bool:
        return query.lower() in exercise["name"].lower()

    return [exercise for exercise in name if _matches(exercise)]
