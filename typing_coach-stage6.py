# === Stage 6: Связи между сущностями ===
# Project: TypingCoach
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List, Optional


class Layout(str, Enum):
    RU = "ru"
    EN = "en"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass
class Exercise:
    title: str
    layout: Layout
    length: int
    difficulty: Difficulty


@dataclass
class Attempt:
    exercise_title: str
    timestamp: datetime
    words_per_minute: float
    errors: int
    total_keys: int


def fetch_attempts_by_exercise(
    exercise: Exercise,
    attempts: List[Attempt],
) -> List[Attempt]:
    return [
        attempt
        for attempt in attempts
        if attempt.exercise_title == exercise.title
    ]


def verify_attempt_relation(
    exercise: Exercise,
    attempts: List[Attempt],
) -> bool:
    related = fetch_attempts_by_exercise(exercise, attempts)
    return len(related) > 0


def summarize_attempts(
    exercise: Exercise,
    attempts: List[Attempt],
) -> dict:
    related = fetch_attempts_by_exercise(exercise, attempts)
    return {
        "exercise_title": exercise.title,
        "layout": exercise.layout.value,
        "length": exercise.length,
        "difficulty": exercise.difficulty.value,
        "attempt_count": len(related),
        "total_errors": sum(attempt.errors for attempt in related),
        "total_keys": sum(attempt.total_keys for attempt in related),
        "average_wpm": (
            sum(attempt.words_per_minute for attempt in related)
            / len(related)
            if related
            else 0.0
        ),
        "latest_attempt": max(
            (attempt for attempt in related),
            key=lambda attempt: attempt.timestamp,
            default=None,
        ),
    }


def find_orphan_exercises(
    exercises: List[Exercise],
    attempts: List[Attempt],
) -> List[Exercise]:
    attempted_titles = {attempt.exercise_title for attempt in attempts}
    return [
        exercise
        for exercise in exercises
        if exercise.title not in attempted_titles
    ]
