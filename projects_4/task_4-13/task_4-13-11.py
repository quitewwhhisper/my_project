array = [10, 20, 30, 40, 50, 60, 70, 80]
print("Исходный массив:", array)
sum_even_index = 0
count_even_index = 0

for i in range(len(array)):
    if i % 2 == 0:
        sum_even_index = sum_even_index + array[i]
        count_even_index = count_even_index + 1
if count_even_index > 0:
    average = sum_even_index / count_even_index
    print("Среднее арифметическое элементов с чётными индексами:", average)
else:
    print("Нет элементов с чётными индексами")