# Данные о приборах
test_tube_name = "Пробирка"
test_tube_number = 101
test_tube_status = "исправен"
test_tube_quantity = 50

wurtz_flask_name = "Колба Вюрца"
wurtz_flask_number = 202
wurtz_flask_status = "исправен"
wurtz_flask_quantity = 15

pipette_name = "Пипетка"
pipette_number = 303
pipette_status = "исправен"
pipette_quantity = 100

spectrophotometer_name = "Спектрофотометр"
spectrophotometer_number = 404
spectrophotometer_status = "исправен"
spectrophotometer_quantity = 3

# Вывод таблицы
print("Название прибора\tИнв. номер\tСостояние\tКоличество")
print(test_tube_name + "\t\t" + str(test_tube_number) + "\t\t" + test_tube_status + "\t\t" + str(test_tube_quantity))
print(wurtz_flask_name + "\t" + str(wurtz_flask_number) + "\t\t" + wurtz_flask_status + "\t\t" + str(wurtz_flask_quantity))
print(pipette_name + "\t\t" + str(pipette_number) + "\t\t" + pipette_status + "\t\t" + str(pipette_quantity))
print(spectrophotometer_name + "\t" + str(spectrophotometer_number) + "\t\t" + spectrophotometer_status + "\t\t" + str(spectrophotometer_quantity))