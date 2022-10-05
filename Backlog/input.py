# selektion des Modes

    
def selectMode():
    mode = input("Bitte wählen: \"m\" für manuelle PIN Eingabe, \"a\" für automatische PINs aus Liste:")
    print(mode)
    return(mode)

def inputPIN():
    PIN = input("PIN eingeben:")
    print(PIN)    
    return(PIN)