made_count = int(input("Введите общее количество произведенных капсул: "))
one_pack_count = int(input("Введите количество капсул в одной упаковке: "))
# расчет
full_packs = made_count // one_pack_count
forgotten_count = made_count % one_pack_count
print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{forgotten_count}")