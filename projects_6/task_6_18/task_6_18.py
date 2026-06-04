# statistics_lab.py
# Анализ цен товаров с использованием Python и SQL

import psycopg2
import pandas as pd

# Параметры подключения к вашей базе данных (из предыдущего задания)
DB_CONFIG = {
    "host": "localhost",
    "port": "5435",  # ВАШ порт (из скриншота)
    "user": "postgres",
    "password": "student",  # ВАШ пароль (замените на правильный)
    "database": "student_task"  # ВАША база данных
}

print("=" * 60)
print("📊 АНАЛИЗ ЦЕН ТОВАРОВ")
print("=" * 60)

try:
    # ============================================
    # 1. ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
    # ============================================
    print("\n🔌 1. Подключение к базе данных...")
    connection = psycopg2.connect(**DB_CONFIG)
    print("   ✅ Подключение успешно установлено!")

    # ============================================
    # 2. SQL-ЗАПРОС: объединяем products и prices
    # ============================================
    print("\n📝 2. Выполнение SQL-запроса (JOIN products и prices)...")

    query = """
        SELECT 
            p.id AS product_id,
            p.name AS product_name,
            p.category AS category,
            pr.price AS price,
            pr.created_at AS price_date
        FROM products p
        JOIN prices pr ON p.id = pr.product_id
        ORDER BY p.category, p.name, pr.price
    """

    # Загружаем результат в DataFrame
    df = pd.read_sql(query, connection)
    print(f"   ✅ Загружено записей: {len(df)}")

    # Закрываем соединение (данные уже в DataFrame)
    connection.close()
    print("   🔒 Соединение закрыто")

    # ============================================
    # 3. ПЕРВИЧНЫЙ ОСМОТР ДАННЫХ
    # ============================================
    print("\n📋 3. Первичный осмотр данных:")
    print("-" * 50)
    print("\nПервые 5 строк:")
    print(df.head())

    print("\nИнформация о данных:")
    print(df.info())

    print(f"\n📊 Статистика по DataFrame:")
    print(f"   - Всего записей о ценах: {len(df)}")
    print(f"   - Уникальных товаров: {df['product_id'].nunique()}")
    print(f"   - Уникальных категорий: {df['category'].nunique()}")
    print(f"   - Диапазон цен: от {df['price'].min():.2f} до {df['price'].max():.2f} руб.")

    # ============================================
    # 4. ОПИСАТЕЛЬНАЯ СТАТИСТИКА ПО ЦЕНАМ
    # ============================================
    print("\n" + "=" * 60)
    print("📈 4. ОПИСАТЕЛЬНАЯ СТАТИСТИКА ЦЕН")
    print("=" * 60)

    # Автоматический отчет pandas
    print("\n📊 Метод describe() pandas:")
    print(df['price'].describe().round(2))

    # Ручной расчет метрик
    print("\n📊 Ручной расчет метрик (в рублях):")
    metrics = {
        'Среднее (mean)': df['price'].mean(),
        'Медиана (median)': df['price'].median(),
        'Стандартное отклонение (std)': df['price'].std(),
        'Минимум (min)': df['price'].min(),
        'Максимум (max)': df['price'].max()
    }

    for name, value in metrics.items():
        print(f"   {name:30s}: {value:>10.2f} руб.")

    # ============================================
    # 5. КВАРТИЛИ И ВЫБРОСЫ
    # ============================================
    print("\n" + "=" * 60)
    print("📊 5. КВАРТИЛИ И АНАЛИЗ ВЫБРОСОВ")
    print("=" * 60)

    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50)  # это медиана
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1

    print(f"\n📐 Квартили:")
    print(f"   Q1 (25% товаров дешевле):  {q1:>10.2f} руб.")
    print(f"   Q2 (50% товаров, медиана): {q2:>10.2f} руб.")
    print(f"   Q3 (75% товаров дешевле):  {q3:>10.2f} руб.")
    print(f"   IQR (межквартильный размах): {iqr:>10.2f} руб.")

    # Товары с ценой выше Q3 (дорогие)
    expensive_products = df[df['price'] > q3]
    print(f"\n💰 Товары с ценой выше Q3 (дороже {q3:.2f} руб.):")
    print(f"   Количество записей: {len(expensive_products)}")
    print("\n   Список товаров:")
    for _, row in expensive_products.iterrows():
        print(f"   • {row['product_name']:35s} | {row['category']:20s} | {row['price']:>10.2f} руб.")

    # ============================================
    # 6. СТАТИСТИКА ПО КАТЕГОРИЯМ
    # ============================================
    print("\n" + "=" * 60)
    print("📊 6. СТАТИСТИКА ПО КАТЕГОРИЯМ ТОВАРОВ")
    print("=" * 60)

    # Группировка по категориям
    category_stats = df.groupby('category')['price'].agg(
        count='count',  # количество записей
        mean='mean',  # средняя цена
        median='median',  # медиана
        std='std'  # стандартное отклонение
    ).round(2)

    # Сортируем по убыванию средней цены
    category_stats = category_stats.sort_values('mean', ascending=False)

    print("\n📊 Статистика по категориям (отсортировано по средней цене):")
    print("-" * 70)
    print(category_stats.to_string())

    # ============================================
    # 7. АНАЛИЗ РАЗБРОСА ЦЕН ПО ТОВАРАМ
    # ============================================
    print("\n" + "=" * 60)
    print("📊 7. ТОВАРЫ С НАИБОЛЬШИМ РАЗБРОСОМ ЦЕН")
    print("=" * 60)

    # Для каждого товара: мин, макс, разница
    price_range = df.groupby(['product_id', 'product_name']).agg(
        min_price=('price', 'min'),
        max_price=('price', 'max')
    ).reset_index()

    price_range['price_diff'] = price_range['max_price'] - price_range['min_price']

    # Сортируем по разнице и берем топ-5
    top5_variation = price_range.sort_values('price_diff', ascending=False).head(5)

    print("\n🏆 Топ-5 товаров с наибольшим разбросом цен:")
    print("-" * 70)
    for _, row in top5_variation.iterrows():
        print(f"   • {row['product_name']:35s}")
        print(
            f"     Мин: {row['min_price']:>10.2f} руб. | Макс: {row['max_price']:>10.2f} руб. | Разница: {row['price_diff']:>10.2f} руб.")

    # ============================================
    # 8. ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ (для понимания)
    # ============================================
    print("\n" + "=" * 60)
    print("📊 8. ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ")
    print("=" * 60)

    # Самый дорогой и самый дешевый товар
    max_price_row = df.loc[df['price'].idxmax()]
    min_price_row = df.loc[df['price'].idxmin()]

    print(f"\n💎 Самый дорогой товар:")
    print(f"   • {max_price_row['product_name']} ({max_price_row['category']})")
    print(f"   • Цена: {max_price_row['price']:.2f} руб.")

    print(f"\n🪙 Самый дешевый товар:")
    print(f"   • {min_price_row['product_name']} ({min_price_row['category']})")
    print(f"   • Цена: {min_price_row['price']:.2f} руб.")

    # Распределение цен по диапазонам
    print("\n📊 Распределение цен по диапазонам:")
    bins = [0, 1000, 5000, 10000, 50000, float('inf')]
    labels = ['< 1000', '1000-5000', '5000-10000', '10000-50000', '> 50000']
    df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels)

    price_distribution = df['price_range'].value_counts().sort_index()
    for range_name, count in price_distribution.items():
        print(f"   {range_name:15s}: {count:4d} записей ({count / len(df) * 100:.1f}%)")

    print("\n" + "=" * 60)
    print("✅ АНАЛИЗ ЗАВЕРШЕН")
    print("=" * 60)

except Exception as error:
    print(f"\n❌ ОШИБКА: {error}")
    print("\n🔧 Проверьте:")
    print("   - Запущен ли Docker Desktop?")
    print("   - Запущен ли контейнер с PostgreSQL?")
    print("   - Правильные ли параметры подключения (порт 5435, база student_task)?")
    print("   - Правильный ли пароль?")

finally:
    # Закрываем соединение, если оно еще открыто
    if 'connection' in locals() and connection and not connection.closed:
        connection.close()
        print("\n🔒 Соединение закрыто")