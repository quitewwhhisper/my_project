# ЗАДАЧА 2 (КОНФИГУРАЦИЯ ОБОРУДОВАНИЯ)
# Написать функцию, которая парсит конфиг-файл формата KEY=VALUE

def parse_config(text):
    """
    Парсит текстовый конфиг в формате KEY=VALUE.

    Аргументы:
        text (str): Многострочный текст конфигурации

    Возвращает:
        dict: Словарь {ключ: значение}
    """
    config = {}

    # Разбиваем текст на строки
    lines = text.splitlines()

    for line in lines:
        # Удаляем пробелы в начале и конце строки
        line = line.strip()

        # Пропускаем пустые строки и комментарии (#)
        if not line or line.startswith('#'):
            continue

        # Делим строку по первому знаку равенства
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()  # удаляем лишние пробелы у ключа
            value = value.strip()  # удаляем лишние пробелы у значения
            config[key] = value

    return config


# Пример использования
config_text = """
# Настройки биореактора
TEMPERATURE=37.5
PH=7.2
STIRRER_SPEED=300
# Это комментарий
OXYGEN_LEVEL=95
"""

result = parse_config(config_text)
print(result)