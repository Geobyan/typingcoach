# === Stage 3: Хранилище в памяти ===
# Project: TypingCoach
# typing_store.py

import uuid


class Exercise:
    """Упражнение для печати.

    Поля:
        id - уникальный идентификатор упражнения
        title - название упражнения
        layout - раскладка (например, "ru" или "en")
        length - длина упражнения в символах
        difficulty - уровень сложности
    """

    def __init__(self, title, layout, length, difficulty):
        self.id = str(uuid.uuid4())
        self.title = title
        self.layout = layout
        self.length = length
        self.difficulty = difficulty

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "layout": self.layout,
            "length": self.length,
            "difficulty": self.difficulty,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            layout=data["layout"],
            length=data["length"],
            difficulty=data["difficulty"],
        )


class ExerciseStore:
    """Хранилище упражнений в памяти.

    Поддерживает добавление, получение по идентификатору и получение списка.
    """

    def __init__(self):
        self._exercises = {}

    def add(self, exercise):
        self._exercises[exercise.id] = exercise
        return exercise

    def get(self, exercise_id):
        return self._exercises.get(exercise_id)

    def list_exercises(self):
        return list(self._exercises.values())
