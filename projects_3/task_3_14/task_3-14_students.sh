#!/bin/bash

echo "=== Анализ файла students.txt ==="
echo ""

echo "1. Только имена студентов:"
awk '{print $1}' students.txt

echo ""
echo "2. Только оценки:"
awk '{print $2}' students.txt

echo ""
echo "3. Номер строки и имя:"
awk '{print NR, $1}' students.txt

