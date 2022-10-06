# Energy Meter PIN Unlock

script to unlock a digital energy meter.\
**It shall only be used for meters not registered or administrated by your "Messstellenbetreiber"!**

It runs on a Raspberry Pi 4 with Ubuntu 22.04. Server installed. \





## Requirements
* python3.10 or newer
* lgpio (```sudo apt install python3-lgpio```)\
For RaspberryOS, the library for GPIO shall be exchanged to gpiozero.

### HW Interface
A LED flashlight controlled via Raspberry Pi GPIO is required. THe hardware is a simple (preferably white LED (--|>|--) with a suitable resistor (---====--- in my case 180Ohm) in series:  
GPIO °---|>|----====----°GND 

## How to use Energy Meter PIN Unlock
One everthing is set up and the flashligth can be controlled via the GPIO, make copy of the ```config-example.py``` file and adjust the PIN range to your needs. Depending on the meter, you might need to adjust the timings as well.

# Backlog / unsolved Issues
- the script can take up to several days. Currently due to the debug print to terminal, the script stops, once ssh or the terminal session is closed\
try  ```python3 unlock_pin.py &``` 

# License
>You can check out the full license [here](LICENSE.txt)

This project is licensed under the terms of the **MIT** license.
