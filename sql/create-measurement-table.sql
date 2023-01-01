CREATE TABLE plant.public.testSensorMeasurements (
	mid				SERIAL		PRIMARY KEY,
	sensor_uid		CHAR(5)		NOT NULL, 
	process_step	VARCHAR(50)	NOT NULL,
	measure_value	INTEGER		NOT NULL,
	measured_on		TIMESTAMP	NOT NULL
);