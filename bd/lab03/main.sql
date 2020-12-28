-- A. Функции
-- 1. Скалярная функция
-- 1.
CREATE OR REPLACE FUNCTION get_tram_count() RETURNS BIGINT AS $$
	SELECT COUNT(*)
	FROM trams
$$  LANGUAGE SQL;

SELECT get_tram_count();

-- 2. Подставляемая табличная функция
-- 2.
CREATE OR REPLACE FUNCTION get_top_drivers(_raiting real) RETURNS TABLE(driver_id int, name varchar, raiting real, exp int) AS $$
	SELECT *
	FROM drivers
	WHERE raiting > _raiting;
$$  LANGUAGE SQL;

SELECT *
FROM get_top_drivers(4);

-- 3. Многооператорную табличную функцию
-- 3.
CREATE TABLE IF NOT EXISTS schedule_copy(LIKE schedules INCLUDING ALL);

CREATE OR REPLACE FUNCTION get_shedule_top_driver_after_hour(hours varchar) RETURNS TABLE
(
	route_id int, 
	times varchar,
	tram_id int,
	driver_id int,
	conductor_id int
) 
AS 
$$	
	DELETE FROM schedule_copy;
	
	INSERT INTO schedule_copy
	SELECT s.*
	FROM schedules AS s JOIN drivers ON s.driver_id = drivers.driver_id
	WHERE raiting >= 4.5;
	
	SELECT *
	FROM schedule_copy
	WHERE time >= hours
	ORDER BY time
$$  LANGUAGE SQL;

SELECT * 
FROM get_shedule_top_driver_after_hour('02:00');

-- 4. Рекурсивную функцию или функцию с рекурсивным ОТВ
-- 4.
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

CREATE OR REPLACE FUNCTION get_next(id int) RETURNS SETOF local_tab AS
$$
BEGIN
    RETURN QUERY 
	(
		SELECT *
    	FROM local_tab
        WHERE model_id = id 
	);
    IF EXISTS (SELECT * FROM local_tab WHERE father IS NOT null AND model_id = id) 
	THEN
        RETURN QUERY
        SELECT *
        FROM get_next(id + 1);
    END IF;
END;
$$ language plpgsql;

SELECT * FROM get_next(1);

-- B. Четыре хранимых процедуры
-- 1. Хранимую процедуру без параметров или с параметрами
-- 1. 
CREATE OR REPLACE PROCEDURE inc_capacity(id int, cap int)
AS $$
BEGIN
    UPDATE models
    SET capacity = capacity + cap
    WHERE model_id = id;
END;
$$
LANGUAGE 'plpgsql';

SELECT * FROM models;
CALL inc_capacity(1, 10);

-- 2. Рекурсивную хранимую процедуру или хранимую процедур с рекурсивным ОТВ
-- 2.
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

CREATE OR REPLACE PROCEDURE rec_upd_models(pid int, cap int)
AS $$
BEGIN
    UPDATE local_tab
    SET capacity = cap
    WHERE model_id = pid;
    IF EXISTS (SELECT * FROM local_tab WHERE father IS NOT null AND model_id = pid)  
	THEN
         CALL rec_upd_models(pid + 1, cap + 10);
    END IF;
END;
$$
LANGUAGE 'plpgsql';

CALL rec_upd_models(1, 100);
SELECT * FROM local_tab;

-- 3. Хранимую процедуру с курсором
-- 3.
CREATE OR REPLACE PROCEDURE cur_upd_cap(s integer, e integer, cap integer)
    LANGUAGE 'plpgsql'
    
AS $BODY$
DECLARE
        row record;
        cur cursor FOR
        	SELECT * FROM models
        	WHERE model_id >= s AND model_id <= e;
BEGIN
	OPEN cur;
		LOOP
			FETCH cur INTO row;
			EXIT WHEN NOT FOUND;
			UPDATE models 
			SET capacity = capacity + cap
			WHERE models.model_id = row.model_id;
		END LOOP;
    CLOSE cur;
END;
$BODY$;

CALL cur_upd_cap(2, 5, 10)
SELECT * FROM models

-- 4. Хранимую процедуру доступа к метаданным
-- 4.
CREATE OR REPLACE PROCEDURE table_size() AS
$$
DECLARE
	cur cursor
	FOR 
	SELECT table_name, pg_relation_size(CAST(table_name AS varchar)) AS SIZE FROM information_schema.tables
	WHERE table_schema NOT IN ('information_schema','pg_catalog');
	row record;
BEGIN
	OPEN cur;
        LOOP
		    FETCH cur INTO row;
		    EXIT WHEN NOT FOUND;
			RAISE NOTICE '{tab_name: %}{size: %}', row.table_name, row.size;
		END LOOP;
	CLOSE cur;
END;
$$ LANGUAGE 'plpgsql';

CALL table_size();

-- C. DML триггер
-- 1. Триггер AFTER
-- 1.
CREATE OR REPLACE FUNCTION upd_cnt()
RETURNS trigger AS
$$
BEGIN
	UPDATE conductors
	SET finer_count = finer_count + 1
	WHERE conductors.conductor_id = NEW.conductor_id;

	UPDATE finers
	SET fine_count = fine_count + 1
	WHERE finers.finer_id = NEW.finer_id;
	
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER upd_cnts
	AFTER INSERT ON fines
	FOR EACH ROW
	EXECUTE PROCEDURE upd_cnt();
	
INSERT INTO fines VALUES(5004, '2020-12-25', 32, 32);
SELECT * 
FROM fines 
	JOIN conductors ON conductors.conductor_id = fines.conductor_id 
	JOIN finers ON finers.finer_id = fines.finer_id 
WHERE finers.finer_id = 32 AND conductors.conductor_id = 32

-- 2. Триггер INSTEAD OF
-- 2.
CREATE VIEW schedules_view AS
SELECT *
FROM schedules;

CREATE OR REPLACE FUNCTION func_disable_insert()
RETURNS trigger AS
$$
BEGIN
	RAISE NOTICE 'Cant insert';
	RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_disable_insert
	INSTEAD OF INSERT ON schedules_view
	FOR EACH ROW
	EXECUTE PROCEDURE func_disable_insert();
	
INSERT INTO schedules_view VALUES(361, '00:01', 1, 1, 1);

-- Защита.
CREATE TABLE IF NOT EXISTS paid_fines(LIKE fines INCLUDING ALL);

CREATE OR REPLACE FUNCTION ins_paid()
RETURNS trigger AS
$$
BEGIN
	INSERT INTO paid_fines VALUES(OLD.fine_id, OLD.data, OLD.finer_id, OLD.conductor_id);
	RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER paid
	AFTER DELETE ON fines
	FOR EACH ROW
	EXECUTE PROCEDURE ins_paid();

DELETE FROM fines
WHERE fine_id = 5001

SELECT * FROM fines WHERE fine_id >= 5000
SELECT * FROM paid_fines