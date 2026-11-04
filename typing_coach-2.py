# === Stage 2: Проверка полей ===
# Project: TypingCoach
from dataclasses import dataclass, field
from typing import List, Optional


# Допустимые раскладки
VALID_LAYOUTS = ("qwerty", "фйвк")


# Допустимые уровни сложности
VALID_DIFFICULTIES = ("easy", "medium", "hard")


@dataclass
class Exercise:
    title: str
    layout: str
    length: int
    difficulty: str

    def validate(self) -> List[str]:
        errors: List[str] = []

        title = self.title.strip()
        if not title:
            errors.append("Название не может быть пустым.")
        elif len(title) > 100:
            errors.append("Название слишком длинное (максимум 100 символов).")

        layout = self.layout.strip().lower()
        if layout not in VALID_LAYOUTS:
            errors.append(
                f"Неверная раскладка '{self.layout}'. "
                f"Допустимы: {', '.join(VALID_LAYOUTS)}."
            )

        try:
            length = int(self.length)
        except (TypeError, ValueError):
            errors.append(f"Длина должна быть целым числом, получено: {self.length!r}.")
        else:
            if length <= 0:
                errors.append("Длина должна быть положительным числом.")
            elif length > 10000:
                errors.append("Длина слишком велика (максимум 10000 символов).")

        difficulty = self.difficulty.strip().lower()
        if difficulty not in VALID_DIFFICULTIES:
            errors.append(
                f"Неверная сложность '{self.difficulty}'. "
                f"Допустимы: {', '.join(VALID_DIFFICULTIES)}."
            )

        return errors


def normalize_input(value: str) -> str:
    """Приводит строку к нормализованному виду: обрезаем пробелы,
    убираем лишние пробелы внутри и приводим к нижнему регистру."""
    if value is None:
        return ""
    result = value.strip()
    result = " ".join(result.split())
    return result.lower()
