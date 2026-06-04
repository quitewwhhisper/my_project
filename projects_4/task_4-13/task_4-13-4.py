n = int(input("Введите число N: "))
summa = 0
for i in range(1, n + 1):
    summa = summa + i
print(f"Сумма чисел от 1 до {n} = {summa}")