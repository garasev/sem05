CREATE TABLE IF NOT EXISTS models (
	model_id SERIAL NOT NULL PRIMARY KEY,
	model varchar(9) NOT NULL,
	capacity int NOT NULL,
	country varchar(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS trams (
	tram_id SERIAL NOT NULL PRIMARY KEY,
	plate varchar(6) NOT NULL,
	model_id int NOT NULL REFERENCES models(model_id),
	mileage int NOT NULL,
	readiness varchar(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS drivers (
	driver_id serial NOT NULL PRIMARY KEY,
	name varchar(64) NOT NULL,
	raiting real NOT NULL,
	exp int NOT NULL
);

CREATE TABLE IF NOT EXISTS conductors (
	conductor_id serial NOT NULL PRIMARY KEY,
	name varchar(64) NOT NULL,
	raiting real NOT NULL,
	finer_count int NOT NULL
);

CREATE TABLE IF NOT EXISTS finers (
	finer_id serial NOT NULL PRIMARY KEY,
	name varchar(64) NOT NULL,
	fine_count int NOT NULL
);

CREATE TABLE IF NOT EXISTS schedules (
	route_id SERIAL NOT NULL PRIMARY KEY,
	time varchar(5) NOT NULL,
	tram_id int NOT NULL REFERENCES trams(tram_id),
	driver_id int NOT NULL REFERENCES drivers(driver_id),
	conductor_id int NOT NULL REFERENCES conductors(conductor_id)
);

CREATE TABLE IF NOT EXISTS fines (
	fine_id SERIAL NOT NULL PRIMARY KEY,
	data varchar(11) NOT NULL,
	finer_id int NOT NULL REFERENCES finers(finer_id),
	conductor_id int NOT NULL REFERENCES conductors(conductor_id)
);

ALTER TABLE drivers ADD CONSTRAINT valid_raiting CHECK (raiting >= 0 AND raiting <= 5);
ALTER TABLE drivers ADD CONSTRAINT valid_exp CHECK (exp >= 0);

ALTER TABLE conductors ADD CONSTRAINT valid_raiting CHECK (raiting >= 0 AND raiting <= 5);
ALTER TABLE conductors ADD CONSTRAINT valid_count CHECK (finer_count >= 0);

ALTER TABLE finers ADD CONSTRAINT valid_count CHECK (fine_count >= 0);

ALTER TABLE models ADD CONSTRAINT valid_capacity CHECK (capacity > 0);
ALTER TABLE models ADD CONSTRAINT valid_model CHECK (model LIKE 'model-___');

ALTER TABLE trams ADD CONSTRAINT valid_plate CHECK (plate LIKE '______');
ALTER TABLE trams ADD CONSTRAINT valid_mileage CHECK (mileage >= 0);

ALTER TABLE schedules ADD CONSTRAINT valid_time CHECK (time LIKE '__:__');


COPY models(model, capacity, country) FROM 'D:\git\p0rn\bd\csv\models.csv' WITH (FORMAT csv);
COPY trams(plate, model_id, mileage, readiness) FROM 'D:\git\p0rn\bd\csv\trams.csv' WITH (FORMAT csv);
COPY drivers(name, raiting, exp) FROM 'D:\git\p0rn\bd\csv\drivers.csv' WITH (FORMAT csv);
COPY conductors(name, raiting, finer_count) FROM 'D:\git\p0rn\bd\csv\conductors.csv' WITH (FORMAT csv);
COPY finers(name, fine_count) FROM 'D:\git\p0rn\bd\csv\finers.csv' WITH (FORMAT csv);
COPY schedules(time, tram_id, driver_id, conductor_id) FROM 'D:\git\p0rn\bd\csv\schedules.csv' WITH (FORMAT csv);
COPY fines(conductor_id, finer_id, data) FROM 'D:\git\p0rn\bd\csv\fines.csv' WITH (FORMAT csv);


