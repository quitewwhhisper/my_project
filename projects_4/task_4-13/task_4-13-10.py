array = [10, 20, 30, 40, 50, 60, 70, 80]
print("Исходный массив:", array)

sum_odd_index = 0
for i in range(len(array)):
    if i % 2 != 0:  # Если индекс НЕЧЁТНЫЙ (1, 3, 5...)
        sum_odd_index = sum_odd_index + array[i]
print("Сумма элементов с нечётными индексами:", sum_odd_index)