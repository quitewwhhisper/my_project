array = [7, 3, 8, 1, 4, 6, 2, 5]
print("Исходный массив:", array)
summa = 0
for element in array:
    summa = summa + element
n = len(array)
average = summa / n
print("Среднее арифметическое:", average)
