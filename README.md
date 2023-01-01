## House Plant Sustainment System

### Mission Statement
To fulfill watering needs of house plants. By leveraging automation tech stack. Using Python, Raspberry Pi, Sensors, and Water Pumps.  

### System Architecture

#### Conceptual Operations
![Alt text](ref/system-diagram.svg)

### Useful Tutorials
1. [Using ADC on Pico](https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/#ADC_in_Raspberry_Pi_Pico)

### Usage
Need to have a file named `database.ini` in the `/lib` diectory with the details of the database used to store date
```
[postgresql]
host=       ###.###.#.###
database=   ######
user=       ######
password=   ######
```