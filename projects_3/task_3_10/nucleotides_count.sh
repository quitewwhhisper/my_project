#!/bin/bash
# Проверяем, есть ли файлы *.fasta в папке
if [ -z "$(ls *.fasta 2>/dev/null)" ]; then
    echo "Ошибка: нет файлов *.fasta в текущей папке"
    exit 1
fi

# Выводим заголовок таблицы
echo "============================================================"
printf "%-20s %-8s %-8s %-8s %-8s\n" "Файл" "A" "T" "G" "C"
echo "============================================================"
# Перебираем все FASTA-файлы
for file in *.fasta; do
    # Проверяем, что файл не пустой (-s: size > 0)
    if [ ! -s "$file" ]; then
        echo "Пропускаем пустой файл: $file"
        continue
    fi
    
    # Извлекаем последовательность (убираем заголовки >)
    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d '\r')
    
    # Считаем нуклеотиды
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)
    # Выводим результат в таблице
    printf "%-20s %-8s %-8s %-8s %-8s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done

echo "============================================================"

