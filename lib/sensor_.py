# Moisture Sensor Calibration
import machine
import time
import os
from calibration import *


def read_moisture(lp):
    value = int()
    while lp != 0:
        print(f'Count till complete: {lp:02}', end = '\r')
        moisture = machine.ADC(28).read_u16()
        lp += -1
        value += moisture
        time.sleep(sleep)
    return value

def calibrate():
    dry = int()
    wet = int()
    
    if input("Select 'ENTER' when the sensor is dry.") == '':
        print("Dry calibration in progress...")
        dry = read_moisture(loop)
    if input("Select 'ENTER' when the sensor is wet.") == '':
        print("Wet calibration in progress...")
        wet = read_moisture(loop) 
    return round(dry/loop), round(wet/loop)


loop = 60
sleep = 1

sensor_id = input("Enter sensor ID: ")
d, w = calibrate()
result = { sensor_id : {"dry": d, "wet": w } }
log_json(result)

print(f'Final calibration value for dry state of sensor {sensor_id}: {d}')
print(f'Final calibration value for wet state of sensor {sensor_id}: {w}')
