## House Plant Sustainment System

### Mission Statement
To fulfill watering needs of house plants. By leveraging automation. Using Python, Raspberry Pi, Sensors, and Water Pumps.  

### System Architecture

#### Conceptual Operations
![Alt text](doc/system-diagram.svg)

### Operations
Need to have a file named `database.ini` in the `/lib` diectory with the details of the database used to store date
```
[postgresql]
host=       ###.###.#.###
database=   ######
user=       ######
password=   ######
```

### Useful Tutorials
1. [ADC on Pico W](https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/#ADC_in_Raspberry_Pi_Pico)
2. [MQTT on Pico W](https://peppe8o.com/mqtt-and-raspberry-pi-pico-w-start-with-mosquitto-micropython/)