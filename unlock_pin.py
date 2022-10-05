#!/usr/bin/env python3

self_description = """
script to unlock a digital energy meter
"""
### Test Skript zum freischalten / deaktivieren der PIN

# https://ubuntu.com/tutorials/gpio-on-raspberry-pi#3-basic-gpio-example
#  Blink an LED with the LGPIO library
#   install with ''sudo apt install python3-lgpio''
#  Uses lgpio library, compatible with kernel 5.11
#  Author: Wolfgang Geyer

import time
import logging
import lgpio
from create_pulse_pattern import *
from create_pin_list import * 

__version__ = "0.0.1"
__version_date__ = "2022-10-5"
__description__ = "Energy_Meter_PIN_Unlock"
__license__ = "MIT"

#settings for the device
start_PINint=38
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
# open the gpio chip and set the LED pin as output
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED)


########
#create a logger
logger = logging.getLogger('PIN')
#set logging level
logger.setLevel(logging.DEBUG)

logfilename='PIN_unlock.log' #new file for each run
handler = logging.FileHandler(logfilename)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# stop propagting to root logger
logger.propagate = False


try:
    
    print('PIN Unlock started at: '+ time.ctime())
    logger.debug('PIN Unlock started')
    
    PINlist=PINlistgenerator(start_PINint,end_PINint)
    #PINlist = ["0101","1234","4321", "1021"]
    print('Starting sequence with '+ str(len(PINlist))+' PIN-entries')
    #print(PINlist)
    logger.debug("first PIN: '%s'" % str(PINlist[0]))
    logger.debug("last PIN: '%s'" % str(PINlist[len(PINlist)-1]))
    logger.debug("Starting sequence with a total of '%s' PIN-entries" % str(len(PINlist)) )

    i=1
    #while True:
    while (i<=len(PINlist)):
        
        for PINstring in PINlist:
            datetime_start=time.time()
            
            #print('-- Initialisiere die PIN Eingabe - '+ str(pulse_time_init)+' Sekunden Lichtpuls')
            # Turn the GPIO pin on
            lgpio.gpio_write(h, LED, 1)
            time.sleep(pulse_time_init)
            lgpio.gpio_write(h, LED, 0)
            time.sleep(waiting_time_init)
            print('Pulse pattern for entry nr. '+str(i)+' is created : PIN number '+ PINstring)
            PIN2pulse(PINstring,h,LED,pulse_time_short,waiting_time_short,waiting_time_long)

            #print ('EINGABE der PIN  '+ PINstring + ' BEENDET-------')
            time.sleep(waitingtimenextPIN) #next PIN
            #print ('Wait '+ str(waitingtimenextPIN) +' sec until next PIN-------')       
            #print('')
            datetime_diff = (time.time() - datetime_start)
            #logger.debug("time last PIN: '%s' ms" % str(datetime_diff * 10**3))
            logger.debug("attempt nr: '%s' PIN: '%s' time last PIN: '%s' sec" % (str(i),PINstring,str(int(datetime_diff * 10**3)/1000)))

            i += 1
    print ('Programm beendet - alle PINs eingegeben-------')
    logger.debug("Program finished - all PIN patterns created")
    
except KeyboardInterrupt as e:
    lgpio.gpio_write(h, LED, 0)
    lgpio.gpiochip_close(h)
    logging.error("user Interrupt '%s'" % str(e))
    exit(1)
    
except Exception as e:
    logging.error(str(e))