import psycopg2
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def store_measure(sensor_uid, process_step, measure_value):
    # Open connection to postgres db
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Define query
        query = f"""
                INSERT INTO plant.public.testSensorMeasurements 
                (sensor_uid, process_step, measure_value, 
                measured_on)
                VALUES 
                ({sensor_uid}, {process_step}, {measure_value}, 
                CURRENT_TIMESTAMP)
                """
        # Execute insert query 
        cur.execute(query)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
    # Close connection to postgres db
    finally:
        if conn:
            cur.close()
            conn.close()
            
store_measurement('002', 'Button', 65748)