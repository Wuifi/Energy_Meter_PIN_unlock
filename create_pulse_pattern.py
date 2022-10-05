#!/usr/bin/env python3

import time
import lgpio

def PIN2pulse(PINstring,h,LED,pulse_time_short,waiting_time_short,waiting_time_long):
    
            
    ciphernr=1

    for digit in PINstring:
        digit=int(digit) 
        count = 1
        #print('- Ziffer '+ str(ciphernr) + ': Pulsmuster für die Zahl '+str(digit) + ' des PINs '+ PINstring+ ' wird generiert')
        while count <= digit:
            if digit==0:
                break
            # Turn the GPIO pin on
            lgpio.gpio_write(h, LED, 1)
            #print('--'+ str(count) + '. Lichtpuls  - '+ str(pulse_time_short)+' Sekunden ')
            #print('---LED ON')
            time.sleep(pulse_time_short)
            lgpio.gpio_write(h, LED, 0)
            #print('---LED OFF')
            time.sleep(waiting_time_short)
            #print('---Warte '+ str(waiting_time_short) +' Sekunden bis zum nächsten Puls')
            count += 1
        #print ('--Warte '+ str(waiting_time_long) +' Sekunden bis zur Eingabe der nächsten Ziffer-------')
        time.sleep(waiting_time_long)  # next digit
        ciphernr += 1
    return()  
