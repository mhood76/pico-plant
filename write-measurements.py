import psycopg2
from lib.config import config
import json
from datetime import datetime
import os

def json_db_insert(content):
    # Insert the json record that is captured for a measurement
    sd, mt, dt = content.values()
    dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

    try:
        params = config()
        conn = psycopg2.connect(**params)	
        cur = conn.cursor()

        query =  f"""INSERT INTO plant.pi.test(
	                sensor_id, date, measurement)
	                VALUES ('{sd}', '{dt}', '{mt}')"""
        cur.execute(query)
        conn.commit()
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
    
    finally:
        if conn:
            cur.close()
            conn.close()

def measurement_parse():
    path = 'log/measurements'
    file_names = os.listdir(path)
    print(file_names)

    for file_name in file_names:
        file_path = path+'/'+file_name
        with open(file_path, 'r') as file:
            file_content = json.load(file)
            json_db_insert(file_content)
        os.remove(file_path)

measurement_parse()
