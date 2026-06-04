n = int(input("Сколько чисел вы хотите ввести? "))
first = float(input("Введите число 1: "))
max_value = first
for i in range(2, n + 1):
    num = float(input(f"Введите число {i}: "))
    if num > max_value:
        max_value = num
print("Максимальное число:", max_value)