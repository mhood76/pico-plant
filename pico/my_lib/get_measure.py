from machine import Pin, ADC
import utime


def blink(cycle, freq):
    '''
    Toggles LED at passed frequency and cycle #
    to indicate that a measuremnt is starting
    '''
    led = Pin('LED', Pin.OUT)
    
    if led.value() == True:
        led.value(0)
        utime.sleep(1)
        
    for x in range(0, cycle):
        led.value(1)
        utime.sleep(freq)
        led.value(0)
        utime.sleep(freq)
        
    utime.sleep(0.5) # pause
        
def get_moisture(gpio):
    '''
    Take a measure of soil moisture 5 times
    Return average measure
    '''
    valid_gpio = (28, 27, 26)
    if not(gpio in valid_gpio):
        print(f"GPIO {gpio} is not supported. Use GPIO 26, 27, or 28.")
        return
        
    value = int()
    lp, loop = 5, 5
    
    blink(3, 0.25) # measurement is starting
    while lp != 0:
        blink(1, 1) # measurement is running
        moisture = ADC(gpio).read_u16()
        lp += -1
        value += moisture
        
    blink(2,0.25) # measurement is complete
    return round(value/loop), gpio, utime.time()
