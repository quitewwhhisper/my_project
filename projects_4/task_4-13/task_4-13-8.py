array = [7, -3, 8, -1, 4, -6, 2, -5]
print("Исходный массив:", array)
count_positive = 0
for element in array:
    if element > 0:
        count_positive = count_positive + 1
print("Количество положительных чисел:", count_positive)