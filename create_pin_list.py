#!/usr/bin/env python3
# ### Skript zum generieren einer PIN-Liste

#PINlist = ["4321", "1021"]

import numpy as np

def PINlistgenerator(start,end):
    
    print('Generating PIN List')
    PINs=np.linspace(start,end,(end-start)).astype('int')
    # Converting numpy to list
    PINs = list(PINs)
    PINlist=[]
    for PIN in PINs:
        if len(str(PIN))<=3:
            while len(str(PIN))<4:
                PIN='0'+str(PIN)
        #PINlist.append(str(PIN))
        PINlist += [str(PIN)]
    return(PINlist)