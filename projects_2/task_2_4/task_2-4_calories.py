# расчет энергоценности продукта
protein_put = input("Введите массу белков в продукте (г).: ")
fat_put = input("Введите массу жиров в продукте (г).: ")
crabs_put = input("Введите массу углеводов в продукте (г).: ")

protein = int(protein_put)
fat = int(fat_put)
crabs = int(crabs_put)
# сам расчет
res_protein = protein * 4
res_fat = fat * 9
res_crabs = crabs * 4
result = res_protein + res_fat + res_crabs

print(f"Энергетическая ценность: {result}")