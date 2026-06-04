# ЗАДАЧА 3 (АНАЛИЗ ТЕХНОЛОГИЧЕСКИХ ЛОГОВ)
# Прочитать JSONL-файл, подсчитать события по уровням и записать отчёт.

import json
from typing import Dict


def analyze_process_logs(jsonl_path: str, report_path: str) -> Dict[str, int]:
    """
    Анализирует JSONL-файл с логами процесса.

    Аргументы:
        jsonl_path (str): Путь к JSONL-файлу
        report_path (str): Путь для сохранения отчёта

    Возвращает:
        dict: Словарь с количеством событий по уровням
    """
    level_counts = {}
    total = 0

    try:
        # Читаем JSONL файл построчно
        with open(jsonl_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()

                # Пропускаем пустые строки
                if not line:
                    continue

                # Парсим JSON-строку
                try:
                    record = json.loads(line)

                    # Проверяем, есть ли поле 'level'
                    if 'level' in record:
                        level = record['level']
                    else:
                        level = 'UNKNOWN'

                    # Увеличиваем счётчик для этого уровня
                    if level not in level_counts:
                        level_counts[level] = 0
                    level_counts[level] += 1
                    total += 1

                except json.JSONDecodeError as e:
                    # Выводим предупреждение о некорректной строке
                    print(f"Предупреждение: ошибка в строке {line_num}: {e}")
                    continue

    except FileNotFoundError:
        print(f"Ошибка: файл '{jsonl_path}' не найден")
        return {}
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return {}

    # Записываем отчёт в файл
    try:
        with open(report_path, 'w', encoding='utf-8') as report:
            report.write("Process Log Report\n")
            report.write("==================\n")

            # Выводим в порядке: INFO, WARNING, ERROR (если есть)
            for level in ['INFO', 'WARNING', 'ERROR']:
                count = level_counts.get(level, 0)
                report.write(f"{level}: {count}\n")

            # Добавляем другие уровни (если есть)
            for level, count in level_counts.items():
                if level not in ['INFO', 'WARNING', 'ERROR']:
                    report.write(f"{level}: {count}\n")

            report.write(f"Total: {total}\n")
    except Exception as e:
        print(f"Ошибка при записи отчёта: {e}")
        return {}

    return level_counts


# Пример использования
if __name__ == "__main__":
    # Создаём тестовый JSONL файл
    test_logs = [
        '{"timestamp": "2024-01-01 10:00:00", "level": "INFO", "message": "Нагрев начат"}',
        '{"timestamp": "2024-01-01 10:05:00", "level": "INFO", "message": "Температура достигнута"}',
        '{"timestamp": "2024-01-01 10:10:00", "level": "WARNING", "message": "Колебания температуры"}',
        '{"timestamp": "2024-01-01 10:15:00", "level": "ERROR", "message": "Ошибка датчика"}',
        '{"timestamp": "2024-01-01 10:20:00", "level": "INFO", "message": "Охлаждение начато"}',
    ]

    # Записываем тестовый файл
    with open('test_logs.jsonl', 'w', encoding='utf-8') as f:
        for log in test_logs:
            f.write(log + '\n')

    # Запускаем функцию
    result = analyze_process_logs('test_logs.jsonl', 'report.txt')

    print("\nРезультат функции:")
    print(result)

    print("\nСодержимое отчёта:")
    with open('report.txt', 'r', encoding='utf-8') as f:
        print(f.read())