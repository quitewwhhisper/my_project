a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвёртое число: "))
min_value = a
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d
print("Минимальное число:", min_value)