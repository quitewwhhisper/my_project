# task_7_boxplot_electronics_appliances.py
# Ящик с усами (Boxplot) для категорий "Электроника" и "Бытовая техника"

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
    "password": "student",  # ЗАМЕНИТЕ НА ВАШ ПАРОЛЬ
    "database": "student_task"
}

print("=" * 60)
print("ЯЩИК С УСАМИ (BOXPLOT) ДЛЯ КАТЕГОРИЙ:")
print("ЭЛЕКТРОНИКА И БЫТОВАЯ ТЕХНИКА")
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
    # ШАГ 2: ЗАГРУЗКА ДАННЫХ ДЛЯ ЭЛЕКТРОНИКИ И БЫТОВОЙ ТЕХНИКИ
    # ============================================
    print("\nШаг 2: Загрузка данных о ценах...")

    # Запрос для Электроники
    query_electronics = """
        SELECT 
            p.category,
            pr.price
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        WHERE p.category = 'Электроника'
        ORDER BY pr.price
    """

    # Запрос для Бытовая техника
    query_appliances = """
        SELECT 
            p.category,
            pr.price
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        WHERE p.category = 'Бытовая техника'
        ORDER BY pr.price
    """

    df_electronics = pd.read_sql(query_electronics, connection)
    df_appliances = pd.read_sql(query_appliances, connection)

    print(f"   Электроника: загружено {len(df_electronics)} записей о ценах")
    print(f"   Бытовая техника: загружено {len(df_appliances)} записей о ценах")

    # Получаем массивы цен
    electronics_prices = df_electronics['price'].values
    appliances_prices = df_appliances['price'].values

    # ============================================
    # ШАГ 3: РАСЧЁТ СТАТИСТИК
    # ============================================
    print("\nШаг 3: Расчёт статистических метрик...")
    print("-" * 50)


    def calculate_stats(prices, name):
        stats = {
            'Категория': name,
            'Количество': len(prices),
            'Среднее': np.mean(prices),
            'Медиана': np.median(prices),
            'Q1': np.percentile(prices, 25),
            'Q3': np.percentile(prices, 75),
            'IQR': np.percentile(prices, 75) - np.percentile(prices, 25),
            'Минимум': np.min(prices),
            'Максимум': np.max(prices)
        }
        return stats


    stats_electronics = calculate_stats(electronics_prices, "Электроника")
    stats_appliances = calculate_stats(appliances_prices, "Бытовая техника")

    print("\n   Статистика по категориям:")
    print("   " + "-" * 85)
    print(f"   {'Категория':<20} {'Среднее':>10} {'Медиана':>10} {'Q1':>10} {'Q3':>10} {'IQR':>10}")
    print("   " + "-" * 85)
    print(f"   {stats_electronics['Категория']:<20} {stats_electronics['Среднее']:>10.0f} "
          f"{stats_electronics['Медиана']:>10.0f} {stats_electronics['Q1']:>10.0f} "
          f"{stats_electronics['Q3']:>10.0f} {stats_electronics['IQR']:>10.0f}")
    print(f"   {stats_appliances['Категория']:<20} {stats_appliances['Среднее']:>10.0f} "
          f"{stats_appliances['Медиана']:>10.0f} {stats_appliances['Q1']:>10.0f} "
          f"{stats_appliances['Q3']:>10.0f} {stats_appliances['IQR']:>10.0f}")
    print("   " + "-" * 85)

    # ============================================
    # ШАГ 4: ПОСТРОЕНИЕ ДВУХ ГРАФИКОВ (РЯДОМ)
    # ============================================
    print("\nШаг 4: Построение графиков...")

    # Создаём фигуру с двумя подграфиками (1 строка, 2 колонки)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Сравнение распределения цен: Электроника vs Бытовая техника',
                 fontsize=16, fontweight='bold')

    # ============================================
    # ГРАФИК 1: ЭЛЕКТРОНИКА
    # ============================================

    box1 = ax1.boxplot(
        electronics_prices,
        vert=True,
        patch_artist=True,
        notch=True,
        showmeans=True,
        meanline=False,
        widths=0.6,
        showfliers=True,
        labels=['Электроника']
    )

    # Настройка внешнего вида графика 1
    box1['boxes'][0].set_facecolor('lightblue')
    box1['boxes'][0].set_edgecolor('navy')
    box1['boxes'][0].set_linewidth(2)
    box1['boxes'][0].set_alpha(0.8)

    box1['medians'][0].set_color('red')
    box1['medians'][0].set_linewidth(3)

    for mean in box1['means']:
        mean.set_marker('D')
        mean.set_markerfacecolor('green')
        mean.set_markeredgecolor('darkgreen')
        mean.set_markersize(8)

    for whisker in box1['whiskers']:
        whisker.set_color('darkblue')
        whisker.set_linewidth(2)
        whisker.set_linestyle('--')

    for cap in box1['caps']:
        cap.set_color('purple')
        cap.set_linewidth(2)

    for flier in box1['fliers']:
        flier.set_marker('o')
        flier.set_markerfacecolor('orange')
        flier.set_markeredgecolor('darkred')
        flier.set_markersize(6)
        flier.set_alpha(0.7)

    ax1.set_title('Электроника\nРаспределение цен', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Цена (руб.)', fontsize=11)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    # Добавляем статистику на график 1
    stats_text1 = f"""Статистика:
Всего: {stats_electronics['Количество']} зап.
Среднее: {stats_electronics['Среднее']:.0f} руб.
Медиана: {stats_electronics['Медиана']:.0f} руб.
Q1: {stats_electronics['Q1']:.0f} руб.
Q3: {stats_electronics['Q3']:.0f} руб.
IQR: {stats_electronics['IQR']:.0f} руб."""

    ax1.text(0.95, 0.95, stats_text1,
             transform=ax1.transAxes,
             verticalalignment='top',
             horizontalalignment='right',
             fontsize=8,
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # ============================================
    # ГРАФИК 2: БЫТОВАЯ ТЕХНИКА
    # ============================================

    box2 = ax2.boxplot(
        appliances_prices,
        vert=True,
        patch_artist=True,
        notch=True,
        showmeans=True,
        meanline=False,
        widths=0.6,
        showfliers=True,
        labels=['Бытовая техника']
    )

    # Настройка внешнего вида графика 2
    box2['boxes'][0].set_facecolor('lightcoral')
    box2['boxes'][0].set_edgecolor('navy')
    box2['boxes'][0].set_linewidth(2)
    box2['boxes'][0].set_alpha(0.8)

    box2['medians'][0].set_color('red')
    box2['medians'][0].set_linewidth(3)

    for mean in box2['means']:
        mean.set_marker('D')
        mean.set_markerfacecolor('green')
        mean.set_markeredgecolor('darkgreen')
        mean.set_markersize(8)

    for whisker in box2['whiskers']:
        whisker.set_color('darkblue')
        whisker.set_linewidth(2)
        whisker.set_linestyle('--')

    for cap in box2['caps']:
        cap.set_color('purple')
        cap.set_linewidth(2)

    for flier in box2['fliers']:
        flier.set_marker('o')
        flier.set_markerfacecolor('orange')
        flier.set_markeredgecolor('darkred')
        flier.set_markersize(6)
        flier.set_alpha(0.7)

    ax2.set_title('Бытовая техника\nРаспределение цен', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Цена (руб.)', fontsize=11)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    # Добавляем статистику на график 2
    stats_text2 = f"""Статистика:
Всего: {stats_appliances['Количество']} зап.
Среднее: {stats_appliances['Среднее']:.0f} руб.
Медиана: {stats_appliances['Медиана']:.0f} руб.
Q1: {stats_appliances['Q1']:.0f} руб.
Q3: {stats_appliances['Q3']:.0f} руб.
IQR: {stats_appliances['IQR']:.0f} руб."""

    ax2.text(0.95, 0.95, stats_text2,
             transform=ax2.transAxes,
             verticalalignment='top',
             horizontalalignment='right',
             fontsize=8,
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    # ============================================
    # ШАГ 5: ЛЕГЕНДА (ОБЩАЯ ДЛЯ ОБОИХ ГРАФИКОВ)
    # ============================================

    from matplotlib.patches import Patch

    legend_elements = [
        Patch(facecolor='lightblue', edgecolor='navy', label='Ящик (Q1–Q3)'),
        Patch(facecolor='red', label='Медиана (Q2)'),
        Patch(facecolor='green', label='Среднее арифметическое'),
        Patch(facecolor='orange', label='Выбросы (аномалии)')
    ]
    fig.legend(handles=legend_elements, loc='lower center',
               bbox_to_anchor=(0.5, -0.05), ncol=4, fontsize=9)

    # ============================================
    # ШАГ 6: СОХРАНЕНИЕ ГРАФИКА
    # ============================================

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.12)  # Оставляем место для легенды
    output_file = "task_7_boxplot_electronics_appliances.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"\n   График сохранён: {output_file}")

    plt.show()

    # ============================================
    # ШАГ 7: ВЫВОДЫ ПО РЕЗУЛЬТАТАМ
    # ============================================
    print("\n" + "=" * 60)
    print("ВЫВОДЫ ПО РЕЗУЛЬТАТАМ АНАЛИЗА")
    print("=" * 60)

    print("\n1. СРАВНЕНИЕ ЦЕНТРАЛЬНЫХ ТЕНДЕНЦИЙ:")
    print("-" * 40)
    print(f"   • Электроника: медиана = {stats_electronics['Медиана']:.0f} руб., "
          f"среднее = {stats_electronics['Среднее']:.0f} руб.")
    print(f"   • Бытовая техника: медиана = {stats_appliances['Медиана']:.0f} руб., "
          f"среднее = {stats_appliances['Среднее']:.0f} руб.")

    if stats_electronics['Медиана'] > stats_appliances['Медиана']:
        print(f"\n   ВЫВОД: Электроника в целом дороже бытовой техники "
              f"(медиана выше на {stats_electronics['Медиана'] - stats_appliances['Медиана']:.0f} руб.)")
    else:
        print(f"\n   ВЫВОД: Бытовая техника в целом дороже электроники "
              f"(медиана выше на {stats_appliances['Медиана'] - stats_electronics['Медиана']:.0f} руб.)")

    print("\n2. РАЗБРОС ДАННЫХ (IQR):")
    print("-" * 40)
    print(f"   • Электроника: IQR = {stats_electronics['IQR']:.0f} руб.")
    print(f"   • Бытовая техника: IQR = {stats_appliances['IQR']:.0f} руб.")

    if stats_electronics['IQR'] > stats_appliances['IQR']:
        print(f"\n   ВЫВОД: Цены на электронику имеют БОЛЬШИЙ разброс, "
              f"чем на бытовую технику (на {stats_electronics['IQR'] - stats_appliances['IQR']:.0f} руб.)")
        print("   → В электронике есть как очень дешёвые, так и очень дорогие товары")
    else:
        print(f"\n   ВЫВОД: Цены на бытовую технику имеют БОЛЬШИЙ разброс, "
              f"чем на электронику (на {stats_appliances['IQR'] - stats_electronics['IQR']:.0f} руб.)")

    print("\n3. АСИММЕТРИЯ РАСПРЕДЕЛЕНИЙ:")
    print("-" * 40)


    def check_symmetry(mean, median, name):
        if mean > median:
            print(f"   • {name}: правосторонняя асимметрия (среднее > медианы) → "
                  f"есть дорогие выбросы")
        elif mean < median:
            print(f"   • {name}: левосторонняя асимметрия (среднее < медианы) → "
                  f"есть дешёвые выбросы")
        else:
            print(f"   • {name}: симметричное распределение")


    check_symmetry(stats_electronics['Среднее'], stats_electronics['Медиана'], "Электроника")
    check_symmetry(stats_appliances['Среднее'], stats_appliances['Медиана'], "Бытовая техника")

    print("\n4. ВЫБРОСЫ (АНАМАЛИИ):")
    print("-" * 40)

    # Поиск выбросов для Электроники
    q1_e = stats_electronics['Q1']
    q3_e = stats_electronics['Q3']
    iqr_e = stats_electronics['IQR']
    lower_e = q1_e - 1.5 * iqr_e
    upper_e = q3_e + 1.5 * iqr_e
    outliers_e = electronics_prices[(electronics_prices < lower_e) | (electronics_prices > upper_e)]

    # Поиск выбросов для Бытовая техника
    q1_a = stats_appliances['Q1']
    q3_a = stats_appliances['Q3']
    iqr_a = stats_appliances['IQR']
    lower_a = q1_a - 1.5 * iqr_a
    upper_a = q3_a + 1.5 * iqr_a
    outliers_a = appliances_prices[(appliances_prices < lower_a) | (appliances_prices > upper_a)]

    print(f"   • Электроника: обнаружено {len(outliers_e)} выбросов")
    if len(outliers_e) > 0:
        for out in outliers_e[:5]:  # показываем первые 5
            print(f"     - Цена {out:.0f} руб.")
        if len(outliers_e) > 5:
            print(f"     - ... и ещё {len(outliers_e) - 5} выбросов")

    print(f"\n   • Бытовая техника: обнаружено {len(outliers_a)} выбросов")
    if len(outliers_a) > 0:
        for out in outliers_a[:5]:
            print(f"     - Цена {out:.0f} руб.")
        if len(outliers_a) > 5:
            print(f"     - ... и ещё {len(outliers_a) - 5} выбросов")

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
    print("   - Есть ли данные в таблицах products и prices?")

finally:
    if connection:
        connection.close()
        print("\nСоединение с базой данных закрыто")