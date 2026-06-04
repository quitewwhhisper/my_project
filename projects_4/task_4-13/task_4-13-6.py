n = int(input("Введите число N: "))
summa = 0
for i in range(1, n + 1):
    summa = summa + i * i
print(f"Сумма квадратов чисел от 1² до {n}² = {summa}")