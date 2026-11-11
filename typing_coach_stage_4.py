# === Stage 4: Редактирование записей ===
# Project: TypingCoach
ALLOWED_FIELDS = ("name", "layout", "length", "difficulty")


def edit_exercise(exercise_id, changes):
    allowed = set(ALLOWED_FIELDS)
    unknown = set(changes) - allowed
    if unknown:
        raise ValueError(
            f"Допустимы только поля: {', '.join(sorted(allowed))}, "
            f"получены: {', '.join(sorted(unknown))}"
        )

    def coerce(value):
        if "name" in changes:
            return str(value)
        if "layout" in changes:
            return str(value)
        if "length" in changes:
            return int(value)
        if "difficulty" in changes:
            return str(value).lower()
        return value

    return {field: coerce(changes[field]) for field in changes}
