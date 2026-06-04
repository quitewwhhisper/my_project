# task_5-16.py
# Подключение к PostgreSQL (student_task) из Python

import psycopg2

# ПРАВИЛЬНЫЕ параметры подключения (из вашего скриншота!)
DB_CONFIG = {
    "host": "localhost",  # База на вашем компьютере
    "port": "5435",  # ПОРТ 5435 (НЕ 5432!)
    "user": "postgres",  # Имя пользователя
    "password": "student",  # Пароль
    "database": "student_task"  # ИМЯ БАЗЫ (НЕ testdb!)
}

try:
    print("🔌 Подключаюсь к базе данных student_task...")
    connection = psycopg2.connect(**DB_CONFIG)
    print("✅ Подключение успешно установлено!")

    cursor = connection.cursor()

    # Проверка: какие таблицы есть в student_task
    print("\n📋 Список таблиц в базе student_task:")
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    tables = cursor.fetchall()
    print("-" * 30)
    for table in tables:
        print(f"  • {table[0]}")
    print("-" * 30)
    print(f"📈 Всего таблиц: {len(tables)}")

    # ВЫПОЛНЯЕМ ЗАПРОС К ТАБЛИЦЕ products
    print("\n🔍 Выполняю запрос: SELECT id, name, category FROM products;")
    cursor.execute("SELECT id, name, category FROM products;")

    results = cursor.fetchall()

    print("\n📊 РЕЗУЛЬТАТЫ:")
    print("-" * 50)
    for row in results:
        print(f"  ID: {row[0]} | {row[1]} | {row[2]}")
    print("-" * 50)
    print(f"📈 Всего записей: {len(results)}")

    cursor.close()

except Exception as error:
    print(f"❌ ОШИБКА: {error}")
    print("\n🔧 Проверьте:")
    print("  1. Порт: должен быть 5435 (не 5432)")
    print("  2. База: должна быть 'student_task' (не 'testdb')")
    print("  3. Запущен ли контейнер?")

finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n🔒 Соединение закрыто")