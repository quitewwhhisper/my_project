array = [7, 3, 8, 1, 4, 6, 2, 5]
print("Исходный массив:", array)
sum_odd = 0
for element in array:
    if element % 2 != 0:  # Если остаток от деления на 2 НЕ равен 0
        sum_odd = sum_odd + element
print("Сумма нечётных элементов:", sum_odd)