# input() - функция, которая ждёт, пока пользователь введёт текст
# в скобках - подсказка
name = input("Введите название питательной среды: ")
agar = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации (°C): ")
# 'w' - write
# with open закроет файл после завершения работы
# encoding='utf-8' — кодировка, чтобы правильно отображались русские буквы
with open('recipe.txt', 'w', encoding='utf-8') as file:
    file.write(name + '\n')
    file.write(f"- Агар: {agar}%\n")
    file.write(f"- Температура стерилизации: {temperature}°C\n")
    print("Файл 'recipe.txt' успешно сформирован!")