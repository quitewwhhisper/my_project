files = ["seq1", "seq2", "seq3", "seq4"]

date = "03/03/2026"

print("=== Обработка файлов с добавлением даты ===")

# Цикл for для перебора всех элементов списка
for name in files:
    # Добавляем расширение .fasta и дату
    new_name = name + "_" + date + ".fasta"
    print(new_name)