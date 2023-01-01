import os
import json


def check_log_dir():
    '''
    Verify that the directory `log` exists
    Create if it does not exist
    '''
    try:
        os.stat('log')
    except:
        os.mkdir('log')
        
def check_file(path):
    '''
    Verify file at path exists
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
        merged = history | result
        
    with open(path, 'w') as file:
        json.dump(merged, file)
        
def new_json(path, result):
    '''
    Writes json results to new file
    '''
    json_result = json.dumps(result, separators= None)
    with open(path, 'w') as f:
        f.write(json_result)
    
def log_local(result, what):
    '''
    Check the the file and path to file exists
    Create new file if it does not exist
    Update with new results if file exists
    
    var: what, identifies if the results are from
    calibration of a moisture measurement
    accpeable values are `cal` and `mea`
    '''
    check_log_dir()
    
    if what == 'cal':
        path = '/log/sensor_cal.json'
    elif what == 'mea':
        path = '/log/measure_log.json'  
    else:
        print(f'{what} is not a valid selection, choose `cal`, or `mea`')
        return
        
    if not check_file(path):
        new_json(path, result)
    else:
        update_json(path, result)
            
def log_remote():
    print("Function is not complete")