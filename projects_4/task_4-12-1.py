array = [7, 3, 8, 1, 4, 6, 2, 5]
print("Исходный массив:", array)
n = len(array)  # n = 8
for i in range(n):
    for j in range(n - 1 - i):
        # Если текущий элемент больше следующего — меняем их местами
        if array[j] > array[j + 1]:
            # Обмен значениями (без временной переменной)
            array[j], array[j + 1] = array[j + 1], array[j]

            # Можно выводить массив после каждого обмена
            print(f"  Меняем {array[j + 1]} и {array[j]}: {array}")

    print(f"После прохода {i + 1}: {array}")

print("\nОтсортированный массив:", array)