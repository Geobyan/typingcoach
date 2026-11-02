# === Stage 1: Каркас модуля ===
# Project: TypingCoach
from dataclasses import dataclass, field
from typing import List


@dataclass
class Exercise:
    title: str
    layout: str
    length: int
    difficulty: str


def make_demo_exercises() -> List[Exercise]:
    return [
        Exercise(
            title="Разминка",
            layout="QWERTY",
            length=50,
            difficulty="easy",
        ),
        Exercise(
            title="Средний темп",
            layout="QWERTY",
            length=120,
            difficulty="medium",
        ),
        Exercise(
            title="Продвинутый",
            layout="QWERTY",
            length=250,
            difficulty="hard",
        ),
        Exercise(
            title="Йо-ки-а-п",
            layout="ЙЦУКЕН",
            length=100,
            difficulty="medium",
        ),
    ]


def main() -> None:
    exercises = make_demo_exercises()
    print("TypingCoach")
    print("Тренажёр печати")
    print()
    print(f"Доступно упражнений: {len(exercises)}")
    print()
    for exercise in exercises:
        print(
            f"- {exercise.title} | "
            f"раскладка: {exercise.layout} | "
            f"длина: {exercise.length} | "
            f"сложность: {exercise.difficulty}"
        )
    print()
    print("Скоро: скорость, ошибки и прогресс.")


if __name__ == "__main__":
    main()
