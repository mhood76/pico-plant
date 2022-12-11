import machine
import time


def read_moisture():
    return machine.ADC(28).read_u16()

read_moisture()
