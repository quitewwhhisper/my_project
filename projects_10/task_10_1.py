# ЗАДАЧА 1 (УЧЁТ СЫРЬЯ И ПАРТИЙ)
# - Найти расхождения между expected и actual
# - Создать список discrepancies с кортежами (sku, diff)
# - Создать словарь by_category: {category: [sku]}

# Исходные данные
products = [
    {"sku": "A1", "category": "flour", "expected": 100, "actual": 95},
    {"sku": "B2", "category": "sugar", "expected": 50, "actual": 50},
    {"sku": "C3", "category": "enzyme", "expected": 10, "actual": 12},
]

# Шаг 1: Находим расхождения
discrepancies = []  # список для расхождений
by_category = {}  # словарь для категорий

for product in products:  # проходим по каждому продукту
    sku = product["sku"]
    category = product["category"]
    expected = product["expected"]
    actual = product["actual"]

    # Проверяем, есть ли расхождение
    if actual != expected:
        diff = actual - expected  # разница (может быть отрицательной)
        discrepancies.append((sku, diff))

    # Добавляем sku в категорию
    if category not in by_category:
        by_category[category] = []  # создаём список, если категории ещё нет
    by_category[category].append(sku)

# Результаты
print("Расхождения (sku, diff):", discrepancies)
print("Категории со списками sku:", by_category)