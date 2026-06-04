#!/bin/bash

echo "=== Замена пути к базе данных в settings.php ==="
echo ""

# Показываем строку до замены
echo "Строка до замены:"
grep "db_data_path" settings.php
echo ""

# Выполняем замену с использованием альтернативного разделителя |
# Команда выведет результат в терминал (не изменяя файл)
echo "Результат замены (без сохранения в файл):"
sed 's|/var/lib/mysql/data|/mnt/ssd/mysql|' settings.php

echo ""
echo "Чтобы сохранить изменения, используйте флаг -i:"
echo "  sed -i '' 's|/var/lib/mysql/data|/mnt/ssd/mysql|' settings.php"

