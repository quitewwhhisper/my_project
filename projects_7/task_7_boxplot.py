# task_7_boxplot.py
# Ящик с усами (Boxplot) для анализа цен товаров по категориям

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================
# ПАРАМЕТРЫ ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ
# ============================================

DB_CONFIG = {
    "host": "localhost",
    "port": "5435",
    "user": "postgres",
    "password": "student",
    "database": "student_task"
}

print("=" * 60)
print("BOXPLOT ДЛЯ АНАЛИЗА ЦЕН ТОВАРОВ")
print("=" * 60)

connection = None

try:
    # ============================================
    # ШАГ 1: ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
    # ============================================
    print("\nШаг 1: Подключение к базе данных...")
    connection = psycopg2.connect(**DB_CONFIG)
    print("   Подключение успешно!")

    # ============================================
    # ШАГ 2: ЗАГРУЗКА ДАННЫХ (цены по категориям)
    # ============================================
    print("\nШаг 2: Загрузка данных о ценах по категориям...")

    query = """
        SELECT 
            p.category,
            pr.price
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        ORDER BY p.category, pr.price
    """

    df = pd.read_sql(query, connection)
    print(f"   Загружено записей: {len(df)}")
    print(f"   Уникальных категорий: {df['category'].nunique()}")

    # ============================================
    # ШАГ 3: ПОДГОТОВКА ДАННЫХ ДЛЯ BOXPLOT
    # ============================================
    print("\nШаг 3: Подготовка данных для построения графика...")

    # Получаем список всех категорий
    categories = df['category'].unique()
    print(f"   Категории: {list(categories)}")

    # Собираем данные для каждой категории в список
    data_for_boxplot = []
    category_labels = []

    for category in categories:
        prices = df[df['category'] == category]['price'].values
        data_for_boxplot.append(prices)
        category_labels.append(category)
        print(f"   - {category}: {len(prices)} записей, "
              f"диапазон цен [{prices.min():.0f}, {prices.max():.0f}] руб.")

    # ============================================
    # ШАГ 4: РАСЧЁТ СТАТИСТИК ДЛЯ КАЖДОЙ КАТЕГОРИИ
    # ============================================
    print("\nШаг 4: Расчёт статистических метрик...")
    print("-" * 50)

    stats_data = []
    for i, category in enumerate(categories):
        prices = data_for_boxplot[i]
        stats_data.append({
            'Категория': category,
            'Количество': len(prices),
            'Среднее': np.mean(prices),
            'Медиана': np.median(prices),
            'Q1': np.percentile(prices, 25),
            'Q3': np.percentile(prices, 75),
            'IQR': np.percentile(prices, 75) - np.percentile(prices, 25),
            'Минимум': np.min(prices),
            'Максимум': np.max(prices)
        })

    # Выводим статистику в виде таблицы
    print("\n   Статистика цен по категориям:")
    print("   " + "-" * 85)
    print(f"   {'Категория':<20} {'Среднее':>10} {'Медиана':>10} {'Q1':>10} {'Q3':>10} {'IQR':>10}")
    print("   " + "-" * 85)
    for stat in stats_data:
        print(f"   {stat['Категория']:<20} {stat['Среднее']:>10.0f} {stat['Медиана']:>10.0f} "
              f"{stat['Q1']:>10.0f} {stat['Q3']:>10.0f} {stat['IQR']:>10.0f}")
    print("   " + "-" * 85)

    # ============================================
    # ШАГ 5: ПОСТРОЕНИЕ ЯЩИКА С УСАМИ
    # ============================================
    print("\nШаг 5: Построение ящика с усами...")

    # Создаём фигуру
    fig, ax = plt.subplots(figsize=(12, 7))

    # Цвета для ящиков (по количеству категорий)
    box_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue',
                  'lightyellow', 'lightpink', 'plum', 'khaki']

    # Строим ящик с усами (вертикальный)
    box = ax.boxplot(
        data_for_boxplot,
        labels=category_labels,
        patch_artist=True,  # Заливка ящиков цветом
        notch=True,  # Выемка у медианы (для сравнения групп)
        vert=True,  # Вертикальная ориентация
        showmeans=True,  # Показывать среднее (ромбиками)
        meanline=False,  # Среднее как ромбик, а не линия
        widths=0.6,  # Ширина ящиков
        showfliers=True  # Показывать выбросы
    )

    # Настройка цветов ящиков
    for i, box_item in enumerate(box['boxes']):
        box_item.set_facecolor(box_colors[i % len(box_colors)])
        box_item.set_edgecolor('navy')
        box_item.set_linewidth(2)
        box_item.set_alpha(0.8)

    # Настройка медианы (красная линия, толстая)
    for median in box['medians']:
        median.set_color('red')
        median.set_linewidth(3)
        median.set_linestyle('-')

    # Настройка среднего (ромбики зелёные)
    for mean in box['means']:
        mean.set_marker('D')
        mean.set_markerfacecolor('green')
        mean.set_markeredgecolor('darkgreen')
        mean.set_markersize(8)

    # Настройка усов (синие, пунктирные)
    for whisker in box['whiskers']:
        whisker.set_color('darkblue')
        whisker.set_linewidth(2)
        whisker.set_linestyle('--')

    # Настройка засечек на усах (вертикальные чёрточки)
    for cap in box['caps']:
        cap.set_color('purple')
        cap.set_linewidth(2)

    # Настройка выбросов (оранжевые кружочки)
    flier_props = box['fliers']
    if len(flier_props) > 0:
        for flier in flier_props:
            flier.set_marker('o')
            flier.set_markerfacecolor('orange')
            flier.set_markeredgecolor('darkred')
            flier.set_markersize(6)
            flier.set_alpha(0.7)

    # ============================================
    # ШАГ 6: НАСТРОЙКА ВНЕШНЕГО ВИДА ГРАФИКА
    # ============================================

    # Заголовок и подписи осей
    ax.set_title('Распределение цен товаров по категориям\n(Boxplot)',
                 fontsize=14, fontweight='bold')
    ax.set_ylabel('Цена (руб.)', fontsize=12)
    ax.set_xlabel('Категория товара', fontsize=12)

    # Поворот подписей оси X для лучшей читаемости
    plt.xticks(rotation=30, ha='right', fontsize=10)

    # Сетка (только по вертикали)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Легенда (ручное создание для пояснения элементов)
    from matplotlib.patches import Patch

    legend_elements = [
        Patch(facecolor='lightblue', edgecolor='navy', label='Ящик (Q1–Q3)'),
        Patch(facecolor='red', label='Медиана (Q2)'),
        Patch(facecolor='green', label='Среднее арифметическое'),
        Patch(facecolor='orange', label='Выбросы (аномалии)')
    ]
    ax.legend(handles=legend_elements, loc='upper right', fontsize=9)

    # Добавляем текстовую аннотацию с пояснениями
    annotation_text = """
    Как читать ящик с усами:
    • Верхний ус: максимальное значение (без выбросов)
    • Верхняя граница ящика (Q3): 75% данных ниже
    • Красная линия: медиана (50% данных)
    • Нижняя граница ящика (Q1): 25% данных ниже
    • Нижний ус: минимальное значение (без выбросов)
    • Оранжевые точки: статистические выбросы
    """

    ax.text(1.02, 0.98, annotation_text,
            transform=ax.transAxes,
            fontsize=8,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # ============================================
    # ШАГ 7: СОХРАНЕНИЕ ГРАФИКА
    # ============================================
    plt.tight_layout()
    output_file = "task_7_boxplot.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n   График сохранён: {output_file}")

    plt.show()

    # ============================================
    # ШАГ 8: ВЫВОДЫ ПО ГРАФИКУ
    # ============================================
    print("\n" + "=" * 60)
    print("ВЫВОДЫ ПО РЕЗУЛЬТАТАМ АНАЛИЗА ГРАФИКА")
    print("=" * 60)

    print("\n1. СРАВНЕНИЕ КАТЕГОРИЙ:")
    print("-" * 40)

    # Находим категорию с самой высокой медианой
    max_median_idx = np.argmax([stat['Медиана'] for stat in stats_data])
    print(f"   • Самая дорогая категория: '{stats_data[max_median_idx]['Категория']}' "
          f"(медиана = {stats_data[max_median_idx]['Медиана']:.0f} руб.)")

    # Находим категорию с самой низкой медианой
    min_median_idx = np.argmin([stat['Медиана'] for stat in stats_data])
    print(f"   • Самая дешёвая категория: '{stats_data[min_median_idx]['Категория']}' "
          f"(медиана = {stats_data[min_median_idx]['Медиана']:.0f} руб.)")

    print("\n2. РАЗБРОС ДАННЫХ (IQR):")
    print("-" * 40)
    for stat in stats_data:
        print(f"   • {stat['Категория']}: IQR = {stat['IQR']:.0f} руб. "
              f"(центральные 50% цен)")

    print("\n3. НАЛИЧИЕ ВЫБРОСОВ (АНОМАЛИЙ):")
    print("-" * 40)

    # Проверяем наличие выбросов в каждой категории
    outliers_found = False
    for i, category in enumerate(categories):
        prices = data_for_boxplot[i]
        q1 = np.percentile(prices, 25)
        q3 = np.percentile(prices, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = prices[(prices < lower_bound) | (prices > upper_bound)]

        if len(outliers) > 0:
            outliers_found = True
            print(f"   • {category}: обнаружено {len(outliers)} выбросов")
            for out in outliers:
                print(f"     - Цена {out:.0f} руб.")

    if not outliers_found:
        print("   • Выбросов (аномалий) не обнаружено во всех категориях")

    print("\n4. ОБЩИЕ ВЫВОДЫ:")
    print("-" * 40)
    print("   • Ящик с усами позволяет компактно сравнить распределения цен")
    print("   • Красная линия (медиана) лучше среднего показывает типичную цену")
    print("   • Ящик (Q1-Q3) показывает, где находятся центральные 50% цен")
    print("   • Выбросы помогают выявить аномальные товары")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)

except Exception as error:
    print(f"\nОШИБКА: {error}")
    print("\nПроверьте:")
    print("   - Запущен ли Docker Desktop?")
    print("   - Запущен ли контейнер с PostgreSQL?")
    print("   - Правильные ли параметры подключения (порт 5435, база student_task)?")
    print("   - Правильный ли пароль в DB_CONFIG?")

finally:
    if connection:
        connection.close()
        print("\nСоединение с базой данных закрыто")