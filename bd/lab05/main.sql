-- 1. Копирование в json данных о водителях
COPY 
(
	SELECT row_to_json(drivers_data) 
    FROM 
	(
        SELECT *
        FROM drivers
    ) drivers_data 
) TO 'D:\git\p0rn\bd\lab05\tmp.json';

-- 2.

-- . Импорт json
CREATE TEMP TABLE drivers_temp(doc JSON);
COPY drivers_temp FROM 'D:\git\p0rn\bd\lab05\tmp.json';

SELECT * FROM drivers_temp

CREATE TABLE IF NOT EXISTS drivers_copy(LIKE drivers INCLUDING ALL); 

-- . Распаковка json
INSERT INTO drivers_copy
SELECT d.*
FROM drivers_temp, json_populate_record(null::drivers, doc) AS d;

SELECT * FROM drivers_copy

-- . Сравнение
(	SELECT * FROM drivers_copy
	EXCEPT
 	SELECT * FROM drivers
)
UNION
(
	SELECT * FROM drivers
	EXCEPT
	SELECT * FROM drivers_copy
)

-- 3. Таблица с полем jsonb
CREATE TABLE IF NOT EXISTS tmp_table (
	id int NOT NULL,
	doc jsonb NOT NULL
)

INSERT INTO tmp_table
VALUES (1, '{"tram_id":{"1": "1", "2": "2"}, "driver_id": {"1":"1", "2":"2"}, "null_atr": "not null"}'),
(2, '{"tram_id":{"1": "3", "2": "4"}, "driver_id": {"1":"3", "2":"4"}}'),
(3, '{"tram_id":{"1": "5", "2": "6"}, "driver_id": {"1":"5", "2":"6"}}'),
(4, '{"tram_id":{"1": "7", "2": "8"}, "driver_id": {"1":"7", "2":"8"}}')

SELECT * FROM tmp_table

-- 4. Вывод
SELECT doc->'tram_id' FROM tmp_table

SELECT doc->'tram_id'->>'1' FROM tmp_table

SELECT doc FROM tmp_table WHERE doc->'null_atr' IS NOT NULL;

UPDATE tmp_table 
SET doc = jsonb_set(DOC, '{null_atr}', 'null') 
WHERE id = 3

SELECT *
FROM json_each_text('{"tram_id":{"1": "1", "2": "2"}, "driver_id": {"1":"1", "2":"2"}, "null_atr": "not null"}')