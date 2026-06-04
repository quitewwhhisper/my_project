i = 1
sum_even = 0
while i < 16:
    if i % 2 == 0:
        sum_even = sum_even + i
    i = i + 1
print("Сумма всех чётных чисел от 1 до 15:", sum_even)
