# Moisture Sensor Calibration
from lib.plant import *


def calibrate(loop):
    dry = int()
    wet = int()
    
    if input("Select 'ENTER' when the sensor is dry.") == '':
        print("Dry calibration in progress...")
        dry = get_moisture(loop)
    if input("Select 'ENTER' when the sensor is wet.") == '':
        print("Wet calibration in progress...")
        wet = get_moisture(loop) 
    return round(dry), round(wet)


sensor_id = input("Enter sensor ID: ")
d, w = calibrate(10)
result = { sensor_id : {"dry": d, "wet": w } }
log_json(result)

print(f'Final calibration value for dry state of sensor {sensor_id}: {d}')
print(f'Final calibration value for wet state of sensor {sensor_id}: {w}')
