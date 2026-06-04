type_donor = input("Введите группу крови донора (1, 2, 3, 4): ")
type_patient = input("Введите группу крови реципиента (1, 2, 3, 4): ")

group_names = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4"
}
print(f"Группа донора: {group_names[type_donor]}")
print(f"Группа реципиента: {group_names[type_patient]}")
print("=" * 50)
if type_donor == "1":
        print("Переливание возможно")
        print("Пояснение: Группа крови является универсальным донором")
elif type_donor == type_patient:
        print("Переливание возможно")
        print(f"Пояснение: Группа крови донора ({group_names[type_donor]}) полностью")
        print(f"соответствует группе крови реципиента ({group_names[type_patient]}).")
else:
        print("Переливание невозможно")
        print(f"Пояснение: Группа крови донора ({group_names[type_donor]}) не подходит")
        print(f"для реципиента с группой ({group_names[type_patient]}).")
