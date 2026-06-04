#!/bin/bash

echo "=== Анализ CSV-файла data.csv ==="
echo ""

echo "1. Названия товаров:"
awk -F "," '{print $2}' data.csv

echo ""
echo "2. Товары дороже 20:"
awk -F "," '$3 > 20 {print $2, $3}' data.csv

echo ""
echo "3. Общая стоимость всех товаров:"
awk -F "," '{sum += $3} END {print sum}' data.csv

