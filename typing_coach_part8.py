# === Stage 8: Сортировка записей ===
# Project: TypingCoach
import datetime


def parse_date(text):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"):
        try:
            return datetime.datetime.strptime(text, fmt).toordinal()
        except (ValueError, TypeError):
            continue
    return datetime.datetime.now().toordinal()


def sort_exercises(exercises, key="title", ascending=True):
    return sorted(
        exercises,
        key=lambda exercise: (
            str(getattr(exercise, key, "")).lower(),
            parse_date(getattr(exercise, "created_at", "")),
        ),
        reverse=not ascending,
    )


def sort_attempts(attempts, key="created_at", ascending=True):
    return sorted(
        attempts,
        key=parse_date,
        reverse=not ascending,
    )


if __name__ == "__main__":
    exercises = [
        {"title": "Python Basics", "created_at": "2024-01-15"},
        {"title": "Advanced Regex", "created_at": "2023-11-02"},
        {"title": "Data Structures", "created_at": "2024-03-20"},
    ]

    print("По названию, возрастание:")
    for exercise in sort_exercises(exercises, ascending=True):
        print(f"  {exercise['title']} ({exercise['created_at']})")

    print("По названию, убывание:")
    for exercise in sort_exercises(exercises, ascending=False):
        print(f"  {exercise['title']} ({exercise['created_at']})")

    attempts = [
        {"created_at": "2024-05-01"},
        {"created_at": "2024-02-15"},
        {"created_at": "2024-04-10"},
    ]

    print("Попытки по дате, возрастание:")
    for attempt in sort_attempts(attempts, ascending=True):
        print(f"  {attempt['created_at']}")

    print("Попытки по дате, убывание:")
    for attempt in sort_attempts(attempts, ascending=False):
        print(f"  {attempt['created_at']}")
