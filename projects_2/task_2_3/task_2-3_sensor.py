name = input("Введите имя оператора: ")
preshuer = input("Введите текущее значение давления (Па):")
with open('sensor_log', 'w', encoding='utf-8') as file:
    file.write(name + '\n')
    file.write(f"- Давление: {preshuer}Па\n")

    print("Данные успешно сохранены в 'sensor_log.txt'")