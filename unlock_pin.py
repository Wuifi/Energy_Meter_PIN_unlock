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
import config

__version__ = "0.0.2"
__version_date__ = "2022-10-6"
__description__ = "Energy_Meter_PIN_Unlock"
__license__ = "MIT"

#handover variables from config.py file
start_PINint = config.start_PINint
end_PINint =   config.end_PINint

pulse_time_init =   config.pulse_time_init
waiting_time_init = config.waiting_time_init

pulse_time_short =   config.pulse_time_short
waiting_time_short = config.waiting_time_short
#pulse_time_long =    config.pulse_time_long #wird für die PIN nicht gebraucht

waiting_time_long=config.waiting_time_long 

waitingtimenextPIN=config.waitingtimenextPIN 

LED = config.LED
#####

try:
    # open the gpio chip and set the LED pin as output
    h = lgpio.gpiochip_open(0)
    lgpio.gpio_claim_output(h, LED)

    ########
    #create a logger
    logger = logging.getLogger('PIN')
    #set logging level
    logger.setLevel(logging.DEBUG)

    logfilename='PIN_unlock.log' #each run will be attached to the existing log-file
    handler = logging.FileHandler(logfilename)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # stop propagting to root logger
    logger.propagate = False
 
    print('PIN Unlock started at: '+ time.ctime())
    logger.debug('PIN Unlock started')
    
    PINlist=PINlistgenerator(start_PINint,end_PINint)
    #PINlist = ["0101","1234","4321", "1021"]
    print('Starting sequence with '+ str(len(PINlist))+' PIN-entries')
    #print(PINlist)
    logger.debug("PIN Unlock started, first PIN is: '%s'" % str(PINlist[0]))
    logger.debug("PIN Unlock started, last PIN is: '%s'" % str(PINlist[len(PINlist)-1]))
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