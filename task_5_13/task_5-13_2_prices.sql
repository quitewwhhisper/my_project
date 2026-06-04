-- Задание 2: Увеличить цену на 5% для product_id <= 5 И цена < 10000

-- Шаг 1 (проверка): Посмотрим, какие товары подпадают под обновление
SELECT id, product_id, price, 'будет изменено на ' || (price * 1.05) AS новое_значение
FROM prices
WHERE product_id <= 5 AND price > 10000;

-- Шаг 2 (обновление): Увеличиваем цену на 5%
UPDATE prices
SET price = price * 1.05
WHERE product_id <= 5 AND price < 10000;

-- Шаг 3 (проверка результата): Посмотрим, что изменилось
SELECT id, product_id, price
FROM prices
WHERE product_id <= 5;