# Energy Meter PIN Unlock

script to unlock a digital energy meter.\
**It shall only be used for meters not registered or administrated by your "Messstellenbetreiber"!**

It runs on a Raspberry Pi 4 with Ubuntu 22.04. Server installed. \
For RaspberryOS, the library for GPIO shall be exchanged to gpiozero.

A LED flashlight controlled via Raspberry Pi GPIO is required. THe hardware is a simple (preferably white LED (--|>|--) with a suitable resistor (---====--- in my case 180Ohm) in series:  
GPIO °---|>|----====----°GND 


# Requirements
* python3.10 or newer
* lgpio (```sudo apt install python3-lgpio```)


# License
>You can check out the full license [here](LICENSE.txt)

This project is licensed under the terms of the **MIT** license.
