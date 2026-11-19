# === Stage 7: Генерация идентификаторов ===
# Project: TypingCoach
import uuid
import string
import random


PROJECT_PREFIX = "tc"


def generate_unique_id(field_name):
    """Генерирует уникальный идентификатор с префиксом проекта и проверкой коллизий."""
    counter = 0
    while True:
        candidate = f"{PROJECT_PREFIX}_{field_name}_{uuid.uuid4().hex[:8]}"
        if candidate not in _known_ids:
            _known_ids[candidate] = True
            return candidate


def _is_valid_id(candidate):
    return (
        candidate.startswith(f"{PROJECT_PREFIX}_")
        and len(candidate) > len(f"{PROJECT_PREFIX}_")
    )


_known_ids = set()


def reserve_id(field_name, value=None):
    """Резервирует уникальный идентификатор, опционально привязывая к значению поля."""
    if value is not None and not isinstance(value, str):
        raise TypeError("Значение поля должно быть строкой")
    return generate_unique_id(field_name)


def make_id(field_name, length=8):
    """Генерирует короткий уникальный идентификатор с префиксом проекта."""
    while True:
        candidate = f"{PROJECT_PREFIX}_{field_name}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=length))}"
        if candidate not in _known_ids:
            _known_ids.add(candidate)
            return candidate
