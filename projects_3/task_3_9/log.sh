#!/bin/bash
log_file="report.log"
error_code=1
if [ -e "$log_file" ]; then
    echo "Файл $log_file существует."
else
    echo "Файл $log_file не найден."
fi
if [ "$error_code" -eq 0 ]; then
    echo "Ошибок не обнаружено. Работа завершена успешно."
elif [ "$error_code" -eq 1 ]; then
    echo "Обнаружена ошибка: неверный ввод данных."
elif [ "$error_code" -eq 2 ]; then
    echo "Обнаружена ошибка: файл не найден."
else
    echo "Неизвестный код ошибки: $error_code"
fi

