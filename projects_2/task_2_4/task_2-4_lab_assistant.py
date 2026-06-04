volume_total = int(input("Введите нужный объем раствора (в мл): "))
salt_mass = volume_total * 0.009
salt_mass_rounded = round(salt_mass, 2)
volume_water = volume_total
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume_total:.1f} мл\n")
    file.write(f"Масса соли:  {salt_mass_rounded:.2f} г\n")
    file.write(f"Объем воды:  {volume_water:.1f} мл\n")

    print("Рецепт сохранён в файл recipe.txt")