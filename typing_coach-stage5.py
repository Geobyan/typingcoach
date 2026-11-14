# === Stage 5: Удаление и восстановление ===
# Project: TypingCoach
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional


class DeletionKind(str, Enum):
    HARD = "hard"
    SOFT = "soft"


@dataclass
class Exercise:
    title: str
    layout: str
    length: int
    difficulty: str
    deleted: bool = False
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[str] = None

    @classmethod
    def create(cls, title, layout, length, difficulty) -> "Exercise":
        return cls(title=title, layout=layout, length=length, difficulty=difficulty)

    def hard_delete(self, who: Optional[str] = None) -> None:
        self.deleted = True
        self.deleted_at = datetime.now()
        self.deleted_by = who

    def soft_delete(self, who: Optional[str] = None) -> None:
        if self.deleted:
            raise ValueError("Упражнение уже удалено")
        self.deleted = True
        self.deleted_at = datetime.now()
        self.deleted_by = who


class ExerciseStore:
    def __init__(self) -> None:
        self._by_id: Dict[str, Exercise] = {}

    def register(self, exercise: Exercise) -> str:
        exercise_id = exercise.title
        self._by_id[exercise_id] = exercise
        return exercise_id

    def get(self, exercise_id: str) -> Optional[Exercise]:
        return self._by_id.get(exercise_id)

    def list_active(self) -> List[Exercise]:
        return [e for e in self._by_id.values() if not e.deleted]

    def list_deleted(self) -> List[Exercise]:
        return [e for e in self._by_id.values() if e.deleted]

    def restore(self, exercise_id: str) -> bool:
        exercise = self._by_id.get(exercise_id)
        if not exercise or not exercise.deleted:
            return False
        exercise.deleted = False
        exercise.deleted_at = None
        exercise.deleted_by = None
        return True

    def clear_deleted(self) -> List[Exercise]:
        removed = [e for e in self._by_id.values() if e.deleted]
        for exercise in removed:
            del self._by_id[exercise.title]
        return removed


def demo() -> None:
    store = ExerciseStore()
    exercise = Exercise.create("Текст про печать", "qwerty", 120, "easy")
    store.register(exercise)
    print("Активные:", len(store.list_active()))
    exercise.soft_delete("admin")
    print("Активные:", len(store.list_active()))
    print("Удалённые:", len(store.list_deleted()))
    print("Восстановлено:", store.restore("Текст про печать"))
    print("Активные:", len(store.list_active()))
    store.register(Exercise.create("Удалить навсегда", "qwerty", 50, "hard"))
    store.get("Удалить навсегда").hard_delete("admin")
    print("Остались после очистки:", len(store.list_active()))
