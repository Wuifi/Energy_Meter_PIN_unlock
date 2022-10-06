#!/usr/bin/env python3

#settings for the device
start_PINint=0
end_PINint=9999

pulse_time_init=0.5
waiting_time_init=3.5

pulse_time_short=0.1
waiting_time_short=0.4 # time between two pulses to increase the digits

#pulse_time_long=6 #wird für die PIN nicht gebraucht
waiting_time_long=3 # time between two different digits 

#(after this time without any short pulse, the device goes to the next digit)
waitingtimenextPIN=5 #120sec time between two different attempts 
#(after this time without any short pulse, the device goes back to the default display)

#Die optische Taste hat zwei Aktionen:
# Kurzes Drücken oder Blinken mit einer Taschenlampe (kürzer als 2 Sekunden)
# Langes Drücken oder Blinken mit einer Taschenlampe (länger als 5 Sekunden)

## settings for the HW-Interface to the LED-flashlight
LED = 24