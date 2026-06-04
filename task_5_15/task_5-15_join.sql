-- Задание 5-15: JOIN (объединение таблиц)
-- Выводим список товаров с их ценами

SELECT 
    p.name AS "Название товара",
    pr.price AS "Цена"
FROM products AS p
JOIN prices AS pr ON p.id = pr.product_id;