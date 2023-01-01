from machine import Pin, ADC
import utime
import os
import json


# Calibration Functions ###

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


# Standard Functions ###
def blink():
    '''
    Sets LED value to off and then toggles once
    '''
    led = Pin('LED', Pin.OUT)
    led.off()
    led.toggle()
    utime.sleep(0.2)
    led.toggle()
    
def get_moisture(loop):
    value = int()
    lp = loop
    while lp != 0:
        moisture = ADC(28).read_u16()
        lp += -1
        value += moisture
        blink()
        utime.sleep(0.5)
    return value/loop
