dna = input("Введите последовательность ДНК: ")
dna_upper = dna.upper()
count_A = dna_upper.count('A')
count_T = dna_upper.count('T')
count_G = dna_upper.count('G')
count_C = dna_upper.count('C')

total = len(dna_upper)

percent_A = (count_A / total) * 100
percent_T = (count_T / total) * 100
percent_G = (count_G / total) * 100
percent_C = (count_C / total) * 100

print(f"\nПоследовательность в верхнем регистре: {dna_upper}")
print("\nПодсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
print(f"\nОбщая длина: {total} нуклеотидов")

print("\nПроцентное содержание нуклеотидов:")
print(f"A: {percent_A:.1f}%")
print(f"T: {percent_T:.1f}%")
print(f"G: {percent_G:.1f}%")
print(f"C: {percent_C:.1f}%")