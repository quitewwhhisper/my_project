#!/bin/bash
if [ $# -lt 2 ]; then
    echo "Ошибка! Недостаточно аргументов."
    echo "Использование: ./impulse.sh <имя_гена> <уровень_экспрессии>"
    exit 1
fi
gene_name=$1
expression_level=$2
echo "Экспрессия гена [$gene_name] составляет $expression_level единиц"

