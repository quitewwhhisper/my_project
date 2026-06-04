print("=== Электронный лабораторный журнала ===\n")
name = input("Введите ФИО исследователя: ")
date = input("Введите дату эусперимента: ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")
width = 50
top_bottom_line = "+" + "-" * (width - 2) + "+\n"
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write(top_bottom_line)
    title = "Электронный лабораторный журнал"
    spaces = (width - 2 - len(title)) // 2
    centered_title = "|" + " " * spaces + title + " " * (width - 2 - spaces - len(title)) + "|\n"
    file.write(centered_title)
    file.write(top_bottom_line)
    line1 = f"| ФИО исследователя : {name}"
    line1 = line1 + " " * (width - len(line1) - 1) + "|\n"
    file.write(line1)
    line2 = f"| Дата : {date}"
    line2 = line2 + " " * (width - len(line2) - 1) + "|\n"
    file.write(line2)
    line3 = f"| Эксперимент : {experiment}"
    line3 = line3 + " " * (width - len(line3) - 1) + "|\n"
    file.write(line3)
    file.write(top_bottom_line)
    line_conclusion = "| Вывод :"
    line_conclusion_title = line_conclusion + " " * (width - len(line_conclusion) - 1) + "|\n"
    file.write(line_conclusion)
    max_line_length = 44
    file.write(top_bottom_line)

    print("Данные успешно сохранены в 'journal.txt'")