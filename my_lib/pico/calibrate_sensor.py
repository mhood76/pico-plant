# Moisture Sensor Calibration
import machine
import time
import os
import os
import json


def check_log_dir():
    '''
    Verify that the directory log exists
    If it does not exist create a directory
    '''
    try:
        os.stat('log')
    except:
        os.mkdir('log')
        
def check_file(path):
    '''
    Verify that the a file at path exists
    Return True is it does
    Return False if it does not
    '''
    try:
        with open(path, 'r') as file:
            return True
    except:
        return False
    
def update_json(path, result):
    '''
    Load data from current log file
    Update with current results and store
    '''
    with open(path, 'r') as file:
        history = json.load(file)
        history.update(result)
        
    with open(path, 'w') as file:
        json.dump(history, file)
    
def log_json(result):
    '''
    Check the the file and path to file exists
    Create new file if it does not exist
    Update with new results if file exists
    '''
    check_log_dir()
    path = '/log/sensor-cal.json'

    if not check_file(path):
        json_result = json.dumps(result, separators= None)
        with open(path, 'w') as f:
            f.write(json_result)
    else:
        update_json(path, result)

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
