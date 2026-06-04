# ЗАДАЧА 4 (КОНТРОЛЬ КАЧЕСТВА / БИОТЕХНОЛОГИИ)
# Обработать результаты анализов проб с конвертацией значений в числа и определением качества.

from typing import List, Tuple, Dict


def process_samples(records: List[Dict]) -> Tuple[List[Dict], List[str]]:
    """
    Обрабатывает список проб с результатами анализов.

    Конвертирует поле "value" из строки в float и добавляет поле "quality".

    Аргументы:
        records (list[dict]): Список словарей с ключами "id" и "value"

    Возвращает:
        tuple: (processed_records, errors)
            - processed_records (list[dict]): Успешно обработанные записи с полями "id", "value", "quality"
            - errors (list[str]): Список ошибок в формате "Sample <id>: <error_message>"

    Пример:
        >>> samples = [
        ...     {"id": "S001", "value": "7.5"},
        ...     {"id": "S002", "value": "invalid"},
        ... ]
        >>> processed, errors = process_samples(samples)
        >>> print(processed[0]["quality"])  # 'normal'
        normal
    """
    processed_records = []
    errors = []

    for record in records:
        sample_id = record.get("id", "unknown")
        value_str = record.get("value", "")

        # Пытаемся конвертировать value в float
        try:
            value = float(value_str)
        except (ValueError, TypeError) as e:
            # Если конвертация не удалась, добавляем ошибку
            errors.append(f"Sample {sample_id}: {e}")
            continue  # Пропускаем эту запись, переходим к следующей

        # Определяем качество на основе значения
        if value < 5:
            quality = "low"
        elif value <= 10:
            quality = "normal"
        else:
            quality = "high"

        # Создаём обработанную запись
        processed_record = {
            "id": sample_id,
            "value": value,
            "quality": quality
        }
        processed_records.append(processed_record)

    return processed_records, errors