from input import *
from create_pin_list import *


try:
    mode=selectMode()

    if mode=="a":
        PINList=PINlistgenerator()
    if mode=="m":
        PIN=inputPIN()
        PINList=[PIN]
    ## Testing    
    #PINlist = ["4321", "1021"]

except KeyboardInterrupt:
    print('KeyboardInterrupt')
