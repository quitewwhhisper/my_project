# task_7_data_analysis.py
# Анализ цен товаров из базы данных student_task

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# ============================================
# ПАРАМЕТРЫ ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ
# ============================================

DB_CONFIG = {
    "host": "localhost",
    "port": "5435",
    "user": "postgres",
    "password": "student",  # ЗАМЕНИТЕ НА ВАШ ПАРОЛЬ
    "database": "student_task"
}

print("=" * 60)
print("АНАЛИЗ ЦЕН ТОВАРОВ ИЗ БАЗЫ ДАННЫХ")
print("=" * 60)

connection = None

try:
    # ---------- ШАГ 1: ПОДКЛЮЧЕНИЕ ----------
    print("\nШаг 1: Подключение к базе данных...")
    connection = psycopg2.connect(**DB_CONFIG)
    print("   Подключение успешно!")

    # ---------- ШАГ 2: ЗАГРУЗКА ДАННЫХ ----------
    print("\nШаг 2: Загрузка данных...")

    query_pie = """
        SELECT 
            p.category,
            COUNT(pr.id) AS price_count
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        GROUP BY p.category
        ORDER BY price_count DESC
    """
    df_pie = pd.read_sql(query_pie, connection)
    print(f"   Загружено категорий: {len(df_pie)}")

    query_all_prices = """
        SELECT pr.price, p.name, p.category
        FROM prices pr
        JOIN products p ON p.id = pr.product_id
        ORDER BY pr.price
    """
    df_prices = pd.read_sql(query_all_prices, connection)
    print(f"   Загружено записей о ценах: {len(df_prices)}")

    # ---------- ШАГ 3: СТАТИСТИЧЕСКИЕ МЕТРИКИ ----------
    print("\nШаг 3: Расчёт статистических метрик...")

    all_prices = df_prices['price']

    stats = {
        'Количество записей': len(all_prices),
        'Среднее (mean)': all_prices.mean(),
        'Медиана (median)': all_prices.median(),
        'Стандартное отклонение (std)': all_prices.std(),
        'Минимум (min)': all_prices.min(),
        'Максимум (max)': all_prices.max(),
        'Q1 (25-й перцентиль)': all_prices.quantile(0.25),
        'Q3 (75-й перцентиль)': all_prices.quantile(0.75),
        'IQR (межквартильный размах)': all_prices.quantile(0.75) - all_prices.quantile(0.25)
    }

    print("\n   Описательная статистика цен:")
    print("-" * 40)
    for name, value in stats.items():
        print(f"   {name:25s}: {value:>10.2f} руб.")
    print("-" * 40)

    # ---------- ШАГ 4: ПОСТРОЕНИЕ ГРАФИКОВ ----------
    print("\nШаг 4: Построение графиков...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Анализ цен товаров', fontsize=16, fontweight='bold')

    # ------------------------------------------------
    # ГРАФИК 1: Круговая диаграмма
    # ------------------------------------------------
    categories = df_pie['category']
    counts = df_pie['price_count']
    pie_colors = ['#9C1A15', '#9B372A', '#994C3E', '#945E54', '#8C706A', '#808080']
    pie_labels = [f"{cat} ({cnt} зап.)" for cat, cnt in zip(categories, counts)]

    wedges, texts, autotexts = ax1.pie(
        counts,
        labels=None,
        autopct='%1.1f%%',
        colors=pie_colors[:len(categories)],
        startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
        pctdistance=0.7
    )

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')

    ax1.set_title('Распределение ценовых записей по категориям', fontsize=12, fontweight='bold')
    ax1.legend(wedges, pie_labels, loc='lower center', bbox_to_anchor=(0.5, -0.25), fontsize=8, frameon=False)

    # ------------------------------------------------
    # ГРАФИК 2: Гистограмма (ИСПРАВЛЕННАЯ ВЕРСИЯ)
    # ------------------------------------------------
    mean_val = all_prices.mean()
    median_val = all_prices.median()
    q1 = all_prices.quantile(0.25)
    q3 = all_prices.quantile(0.75)
    iqr_val = stats['IQR (межквартильный размах)']

    n_bins = 15
    ax2.hist(all_prices, bins=n_bins, color='#4a90d9', edgecolor='white', alpha=0.7)

    # Убираем label= у линий, чтобы не дублировать легенду
    ax2.axvline(mean_val, color='red', linestyle='-', linewidth=2)
    ax2.axvline(median_val, color='green', linestyle='--', linewidth=2)
    ax2.axvline(q1, color='orange', linestyle=':', linewidth=1.5)
    ax2.axvline(q3, color='orange', linestyle=':', linewidth=1.5)
    ax2.axvspan(q1, q3, alpha=0.15, color='orange')

    ax2.set_xlabel('Цена (руб.)', fontsize=11)
    ax2.set_ylabel('Количество товаров', fontsize=11)
    ax2.set_title('Распределение цен товаров', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    # Легенда создаётся ТОЛЬКО ОДИН РАЗ
    legend_elements = [
        Patch(facecolor='#4a90d9', edgecolor='white', label='Распределение цен'),
        Patch(facecolor='orange', alpha=0.3, label='Центральные 50% (IQR)'),
        Patch(facecolor='red', label=f'Среднее: {mean_val:.0f} руб.'),
        Patch(facecolor='green', label=f'Медиана: {median_val:.0f} руб.')
    ]
    ax2.legend(handles=legend_elements, loc='upper left', fontsize=8, bbox_to_anchor=(0.4, 0.98))

    # Текстовая аннотация со статистикой
    stats_text = f"""Всего: {len(all_prices)} зап.
Среднее: {mean_val:.0f} руб.
Медиана: {median_val:.0f} руб.
Q1: {q1:.0f} руб. | Q3: {q3:.0f} руб.
IQR: {iqr_val:.0f} руб."""

    ax2.text(0.95, 0.95, stats_text,
             transform=ax2.transAxes,
             verticalalignment='top',
             horizontalalignment='right',
             fontsize=8,
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # ---------- ШАГ 5: ПОИСК АНОМАЛИЙ ----------
    print("\nШаг 5: Поиск аномалий...")

    lower_bound = q1 - 1.5 * iqr_val
    upper_bound = q3 + 1.5 * iqr_val

    outliers = df_prices[(df_prices['price'] < lower_bound) | (df_prices['price'] > upper_bound)]

    if len(outliers) > 0:
        print(f"\n   Обнаружено {len(outliers)} потенциальных выбросов:")
        for _, row in outliers.iterrows():
            print(f"      - {row['name']} ({row['category']}): {row['price']:.0f} руб.")
    else:
        print("\n   Статистических выбросов не обнаружено")

    zero_or_negative = df_prices[df_prices['price'] <= 0]
    if len(zero_or_negative) > 0:
        print(f"\n   Обнаружены некорректные цены (<= 0): {len(zero_or_negative)} записей")
    else:
        print("\n   Некорректных цен (<= 0) не обнаружено")

    # ---------- ШАГ 6: СОХРАНЕНИЕ ГРАФИКА ----------
    print("\nШаг 6: Сохранение графика...")

    plt.tight_layout()
    output_file = "task_7_price_analysis.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"   График сохранён: {output_file}")

    plt.show()

    # ---------- ШАГ 7: ОБОСНОВАНИЕ ВЫБОРА ГРАФИКОВ ----------
    print("\n" + "=" * 60)
    print("ОБОСНОВАНИЕ ВЫБОРА ТИПОВ ГРАФИКОВ")
    print("=" * 60)

    print("""
1. КРУГОВАЯ ДИАГРАММА (PIE CHART):
   - Выбрана для отображения доли каждой категории в общем количестве ценовых записей
   - Позволяет визуально оценить, какая категория доминирует
   - Подходит для категориальных данных с небольшим количеством групп (3-6)

2. ГИСТОГРАММА (HISTOGRAM):
   - Выбрана для анализа распределения непрерывной переменной (цены)
   - Позволяет увидеть форму распределения (симметричное/скошенное)
   - На одном графике можно отобразить статистические метрики (среднее, медиану, квартили)
   - Помогает обнаружить выбросы и понять структуру данных
""")

    # ---------- ШАГ 8: ВЫВОДЫ ----------
    print("\n" + "=" * 60)
    print("ВЫВОДЫ ПО РЕЗУЛЬТАТАМ АНАЛИЗА")
    print("=" * 60)

    total = df_pie['price_count'].sum()
    max_cat = df_pie.loc[df_pie['price_count'].idxmax()]
    min_cat = df_pie.loc[df_pie['price_count'].idxmin()]

    print("\nВЫВОД 1: Круговая диаграмма")
    print("-" * 50)
    print(f"   - Категория с наибольшим количеством записей: '{max_cat['category']}' "
          f"({max_cat['price_count']} зап., {max_cat['price_count']/total*100:.1f}%)")
    print(f"   - Категория с наименьшим количеством записей: '{min_cat['category']}' "
          f"({min_cat['price_count']} зап., {min_cat['price_count']/total*100:.1f}%)")

    print("\nВЫВОД 2: Гистограмма распределения цен")
    print("-" * 50)
    if mean_val > median_val:
        print(f"   - Распределение имеет ПРАВОСТОРОННЮЮ асимметрию "
              f"(среднее {mean_val:.0f} > медианы {median_val:.0f})")
        print(f"   - Это означает, что есть товары с аномально высокими ценами")
    elif mean_val < median_val:
        print(f"   - Распределение имеет ЛЕВОСТОРОННЮЮ асимметрию")
    else:
        print(f"   - Распределение СИММЕТРИЧНОЕ")

    print(f"   - Центральные 50% цен: [{q1:.0f}, {q3:.0f}] руб.")

    print("\nВЫВОД 3: Аномалии в данных")
    print("-" * 50)
    if len(outliers) > 0:
        print(f"   - Обнаружено {len(outliers)} выбросов")
    else:
        print("   - Выбросов не обнаружено")

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЗАВЕРШЁН")
    print("=" * 60)

except Exception as error:
    print(f"\nОШИБКА: {error}")
    print("\nПроверьте:")
    print("   - Запущен ли Docker Desktop?")
    print("   - Запущен ли контейнер с PostgreSQL?")
    print("   - Правильные ли параметры подключения?")

finally:
    if connection:
        connection.close()
        print("\nСоединение с базой данных закрыто")