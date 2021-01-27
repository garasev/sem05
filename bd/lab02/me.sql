-- 1. Получить список всех моделей трамвайев с вместимостью 90
-- 1. Предикат сравнения
SELECT *
FROM models
WHERE capacity = 90

-- 2. Получить список штрафов за лето 2019 года
-- 2. Between 
SELECT *
FROM drivers
WHERE exp BETWEEN 2 AND 4

-- 3. Получить список Моделей начинающихся с буквы А
-- 3. Инструкция SELECT, использующая предикат LIKE.
SELECT *
FROM models 
WHERE model LIKE 'model-A%'

-- 4. Получить расписание трамваев, пробег которых больше 10 000
-- 4. Инструкция SELECT, использующая предикат IN с вложенным подзапросом.
SELECT time, tram_id
FROM schedules
WHERE tram_id IN
(
	SELECT schedules.tram_id
	FROM trams JOIN schedules ON schedules.tram_id = trams.tram_id
	WHERE mileage > 10000
)
-- 5. Список "неэффективных" запросов
-- 5. Инструкция SELECT, использующая предикат EXISTS с вложенным подзапросом.
SELECT conductor_id, name
FROM conductors
WHERE not EXISTS
(
	SELECT *
	FROM fines
	WHERE fines.conductor_id = conductors.conductor_id
)

-- 6. Список всех водителей, рейтинг которых больше рейтинга любого водителя с опытом работы 1 год
-- 6. Инструкция SELECT, использующая предикат сравнения с квантором.
SELECT *
FROM drivers
WHERE raiting > ALL
(
	SELECT raiting
	FROM drivers
	WHERE exp = 1
)

-- 7. Средний рейтинг водителй по стажу
-- 7. Инструкция SELECT, использующая агрегатные функции в выражениях столбцов.
SELECT ROUND(AVG(raiting)::numeric, 2) AS average_raiting, exp
FROM drivers 
GROUP BY exp

-- 8.* Минимальный и максимальный рейтинг водителей по стажу
-- 8.* Инструкция SELECT, использующая скалярные подзапросы в выражениях столбцов.
SELECT driver_id, name,
(
    SELECT MIN(time)
    FROM schedules
	WHERE schedules.driver_id = drivers.driver_id
) AS min_data
FROM drivers

-- 9. Проверка готовности трамвайев
-- 9. Инструкция SELECT, использующая простое выражение CASE.
SELECT *,
CASE readiness
WHEN 'True' THEN 'Готов'
ELSE 'Не готов'
END as tag
FROM trams

-- 10. Распределение трамвайев по пробегу по тегам
-- 10. Инструкция SELECT, использующая поисковое выражение CASE.
SELECT tram_id, plate, mileage,
CASE 
WHEN mileage < 10000 THEN 'Мало'
WHEN mileage < 40000 THEN 'Средне'
WHEN mileage < 90000 THEN 'Много'
ELSE 'Невероятно'
END as tag
FROM trams

-- 11. Временная таблица 
-- 11. Создание новой временной локальной таблицы из результирующего набора данных инструкции SELECT. 
SELECT tram_id, plate, trams.model_id, model
INTO local_tab
FROM trams JOIN models ON trams.model_id = models.model_id

SELECT *
FROM local_tab

DROP TABLE local_tab

-- 12. Расписание трамваев с пробегом 95км +
-- 12. Инструкция SELECT, использующая вложенные коррелированные подзапросы в качестве производных таблиц в предложении FROM.
SELECT time, schedules.tram_id, driver_id, mileage
FROM schedules JOIN
(
	trams JOIN models
	ON trams.model_id = models.model_id
) AS tr ON tr.tram_id = schedules.tram_id
WHERE mileage > 95000
order by time

-- 13. Имена водителей, которые водят трамваи, модель которых начинается с буквы А, по расписанию.
-- 13. Инструкция SELECT, использующая вложенные подзапросы с уровнем вложенности 3.
SELECT name
FROM drivers JOIN
(
	SELECT *
	FROM schedules JOIN 
	(
		SELECT *
		FROM trams JOIN
		(
			SELECT * 
			FROM models
			WHERE model LIKE 'model-A%'
		) AS mo ON trams.model_id = mo.model_id
	) AS tr ON schedules.tram_id = tr.tram_id
) AS dr ON drivers.driver_id = dr.driver_id

-- 14. Все встречающиеся оценки кондукторов
-- 14. Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY, но без предложения HAVING.
SELECT raiting
FROM conductors
GROUP BY raiting
Order by raiting

-- 15. Все встречающиеся оценки кондукторов 3 раза
-- 15. Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY и предложения HAVING.
SELECT raiting, COUNT(*)
FROM conductors
GROUP BY raiting
HAVING COUNT(*) = 3
Order by raiting

-- 16. Вставка Модели
-- 16. Однострочная инструкция INSERT, выполняющая вставку в таблицу одной строки значений.
INSERT INTO models VALUES (11, 'model-AAA', 100, 'Россия');

-- 17. Перевыпуск маловместительных моделей трамваев
-- 17. Многострочная инструкция INSERT, выполняющая вставку в таблицу результирующего набора данных вложенного подзапроса.
INSERT INTO models (model_id, model, capacity, country)
SELECT model_id + 11 AS model_id, model, capacity + 10 AS capacity, country
FROM models
WHERE capacity = 90

-- 18. Увеличить стаж на год
-- 18. Простая инструкция UPDATE.
UPDATE drivers
SET exp = exp + 1

-- 19. Установка нового максимального пробега всем трамваям, модели которых ниже 5 по id.
-- 19. Инструкция UPDATE со скалярным подзапросом в предложении SET.
UPDATE trams
SET mileage = 
(
	SELECT MAX(mileage)
	FROM trams
)
WHERE model_id < 5

-- 20. без комментариев
-- 20. Простая инструкция DELETE.
DELETE from models
WHERE country = 'Россия'

-- 21. Удаление трамваем ссылающиеся на модели с id больше 10
-- 21. Инструкция DELETE с вложенным коррелированным подзапросом в предложении WHERE.
DELETE from trams
WHERE model_id IN
(
	SELECT model_id
	FROM models
	WHERE model_id > 10
)

-- 22. Количество зайцев и дата
-- 22. Инструкция SELECT, использующая простое обобщенное табличное выражение
WITH CTE (data_, total)
AS
(
	SELECT fines.data, count(*) AS total
	FROM fines
	GROUP BY fines.data
)
SELECT *
FROM CTE

-- 23. Рекурсивный папа - псих у моделей трамваев
-- 23. Инструкция SELECT, использующая рекурсивное обобщенное табличное выражение.
SELECT model_id, model, capacity, country
INTO local_tab
FROM models
WHERE model_id < 11;

ALTER TABLE local_tab ADD COLUMN father INT;

UPDATE local_tab
SET father = model_id + 1;

UPDATE local_tab
SET father = NULL
WHERE father = 11;

WITH RECURSIVE rec (model_id, model, father) as
	(
		SELECT model_id, model, father
		FROM local_tab
		WHERE model_id = 10

		UNION ALL

		SELECT local_tab.model_id, local_tab.model, local_tab.father
		FROM rec, local_tab
		WHERE rec.model_id = local_tab.father
	)
select *
from rec;

DROP TABLE local_tab

-- 24. Мин и макс количество пойманных зайцев в пределах своего рейтинга.
-- 24. Оконные функции. Использование конструкций MIN/MAX/AVG OVER().
SELECT name, raiting, finer_count,
	   MIN(finer_count) OVER (PARTITION BY raiting) AS min_finer,
	   MAX(finer_count) OVER (PARTITION BY raiting) AS max_finer
FROM conductors

-- 25. Список водителей разных стажей без дублежей.
-- 25. Оконные функции для устранения дублей.
CREATE TABLE IF NOT EXISTS cop(LIKE schedules INCLUDING ALL);
INSERT INTO cop 
SELECT * FROM schedules

SELECT * FROM cop JOIN drivers ON drivers.driver_id = cop.driver_id

DELETE 
FROM cop WHERE route_id in (
SELECT route_id
FROM
	(
		SELECT route_id, row_number() OVER (PARTITION BY drivers.exp) AS row
		FROM schedules JOIN drivers ON schedules.driver_id = drivers.driver_id
	) as tttt
	WHERE row > 1)
