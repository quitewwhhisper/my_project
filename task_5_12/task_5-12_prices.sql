-- Задание 3.1: Выведите количество (COUNT) записей в таблице prices для каждого товара (product_id)
SELECT product_id, COUNT(*) AS количество_записей_о_цене
FROM prices
GROUP BY product_id;

-- Задание 3.2: Выведите среднюю цену товаров (AVG(price)) для каждого product_id из таблицы prices
SELECT product_id, AVG(price) AS средняя_цена
FROM prices
GROUP BY product_id;

-- Задание 3.3: Выведите минимальную (MIN) цену для каждого товара (product_id) из таблицы prices
SELECT product_id, MIN(price) AS минимальная_цена
FROM prices
GROUP BY product_id;

-- Задание 3.4: Выведите максимальную (MAX) цену для каждого товара (product_id) из таблицы prices
SELECT product_id, MAX(price) AS максимальная_цена
FROM prices
GROUP BY product_id;


--COUNT(*) — количество записей (сколько раз цена фиксировалась)
--AVG(price) — среднее арифметическое всех цен товара
--MIN(price) — самая низкая цена
--MAX(price) — самая высокая цена