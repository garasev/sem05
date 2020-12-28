CREATE TABLE IF NOT EXISTS employee
(
    id_emp SERIAL PRIMARY KEY,
    name CHARACTER VARYING(64) NOT NULL,
    birthdate DATE NOT NULL,
    department CHARACTER VARYING(64)
);

INSERT INTO employee VALUES (1, 'Гарасев Н.А.', '2000-09-12', 'МГТУ');
INSERT INTO employee VALUES (2, 'Иванов А.А.', '1999-08-10', 'МГТУ');
INSERT INTO employee VALUES (3, 'Куликов Д.А.', '2001-02-08', 'МГТУ');
INSERT INTO employee VALUES (4, 'Петров Б.Б.', '2000-03-20', 'Цитис');
INSERT INTO employee VALUES (5, 'Павлов Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (6, 'Павлов2 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (7, 'Павлов3 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (8, 'Павлов4 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (9, 'Павлов5 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (10, 'Павлов6 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (11, 'Павлов7 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (12, 'Павлов8 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (13, 'Павлов9 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (14, 'Павлов10 Н.А.', '2000-10-03', 'Цитис');
INSERT INTO employee VALUES (15, 'Павлов11 Н.А.', '2000-10-03', 'Цитис');

CREATE TABLE IF NOT EXISTS time_log
(
    id_emp INT NOT NULL REFERENCES employee(id_emp),
    sysdate DATE NOT NULL,
    day_week CHARACTER VARYING(64) NOT NULL,
    systime TIME NOT NULL,
    type INT NOT NULL
);

INSERT INTO time_log VALUES (4, '2020-12-28', 'ПН', '9:05', 1);
INSERT INTO time_log VALUES (2, '2020-12-28', 'ПН', '9:05', 1);

INSERT INTO time_log VALUES (3, '2020-12-28', 'ПН', '9:00', 1);
INSERT INTO time_log VALUES (3, '2020-12-28', 'ПН', '19:00', 2);

INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:00', 1);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:10', 2);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:15', 1);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:20', 2);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:25', 1);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:30', 2);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '9:35', 1);
INSERT INTO time_log VALUES (1, '2020-12-28', 'ПН', '10:00', 2);

INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:00', 1);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:10', 2);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:15', 1);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:20', 2);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:25', 1);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:30', 2);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '9:35', 1);
INSERT INTO time_log VALUES (2, '2020-12-27', 'ПН', '10:00', 2);

CREATE OR REPLACE FUNCTION cnt_emp_task_1()
RETURNS BIGINT AS $$
BEGIN
    RETURN(
        SELECT COUNT(employee.id_emp)
        FROM
        (
            SELECT employee.id_emp, time_log.sysdate, COUNT(time_log.type)
            FROM employee JOIN time_log ON employee.id_emp = time_log.id_emp
            WHERE time_log.type = 2
            GROUP BY employee.id_emp, time_log.sysdate
            HAVING COUNT(time_log.type) > 3
        ) as tmp
        JOIN employee ON employee.id_emp = tmp.id_emp
        WHERE date_part('year', age(current_date, birthdate)) BETWEEN 18 AND 40
    );
END;
$$
LANGUAGE 'plpgsql';

SELECT * FROM cnt_emp_task_1();



