#!/bin/bash

echo "=== Поиск информации о текущем пользователе ==="
echo "Имя пользователя: $USER"
echo ""

# Ищем строку с именем пользователя в /etc/passwd
grep "^$USER:" /etc/passwd

# Проверяем результат
if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Пользователь найден!"
else
    echo ""
    echo "✗ Пользователь не найден в /etc/passwd"
fi
