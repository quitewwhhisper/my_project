#!/bin/bash

echo "Перебираем числа от 1 до 20..."
echo "------------------------"

for i in {1..20}; do
 if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
echo "Нечетное число: $i"
if [ $i -eq 15 ]; then
        echo "Достигнуто число 15. Останавливаем работу."
        break
    fi
done

echo "------------------------"
echo "Цикл завершен."
