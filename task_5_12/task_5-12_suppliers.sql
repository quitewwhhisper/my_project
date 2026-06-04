-- Задание 2: Выведите количество поставщиков для каждого товара из таблицы suppliers, сгруппировав данные по product_id
SELECT product_id, COUNT(*) AS количество_поставщиков
FROM suppliers
GROUP BY product_id;

