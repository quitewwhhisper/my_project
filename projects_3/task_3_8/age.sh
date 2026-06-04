#!/bin/bash
read -p "Введите год вашего рождения: " birth_year
current_year=$(date +%Y)
age=$((current_year - birth_year))
echo "Ваш возраст: $age лет"
