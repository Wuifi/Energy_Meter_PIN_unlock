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

## How to use analyze the Energy Meter PIN Unlock
with the Jupyter Notebook ```analysis.ipynb```, the log file is converted into a pandas dataframe and visualized.

# Backlog / unsolved Issues
- the script can take up to several days. Currently all relevant information is logged in ```PIN_unlock.log``` file. To debug and print the output directily to terminal, the script is to be modified. This was implemented as  the script stops, once ssh or the terminal session is closed\

use  ```python3 unlock_pin.py &``` instead\
To figure out the process ID, use the following command:\ 
```ps ax | grep unlock_pin.py```\
and kill the process with\
```kill -9 {{id got after }} &```

not recommended:  ```python3 unlock_pin.py &&``` ==> this blocks the log output as well
# License
>You can check out the full license [here](LICENSE.txt)

This project is licensed under the terms of the **MIT** license.
