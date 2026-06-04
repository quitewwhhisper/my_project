#!/bin/bash

echo "=== Часть 1: Создание файлов ==="
for i in {1..10}; do
    filename="test$i.txt"
    echo "Создаю файл: $filename"
    echo "Это содержимое файла $filename" > "$filename"
done

echo ""
echo "Список созданных файлов:"
ls -l test*.txt

echo ""
echo "=== Часть 2: Удаление файлов в обратном порядке ==="
counter=10
while [ $counter -gt 0 ]; do
    filename="test$counter.txt"
    echo "Удаляю файл: $filename"
    rm -f "$filename"
    let "counter--"
done

echo ""
echo "Проверка: файлы удалены"
ls -l test*.txt 2>/dev/null || echo "Файлов test*.txt не найдено"
