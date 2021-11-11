
def BrutForce(ciag, wyraz):
    wyrazLength = len(wyraz)
    counter = 0
    for element in ciag:
        if(element == wyraz[counter]):
            counter += 1
            if (counter == wyrazLength):
                return True        
        else:
            counter = 0
    return False


ciag = "BAABABAAABAAB"
szukany = "AAB"

Znalezniony = BrutForce(ciag, szukany)
print("Przeszukiwany ciag 1 : ", ciag)
if (Znalezniony == True):
    print("Znaleziono")
else:
    print("NIE znaleziono")



ciag = "XXXXXXXXXXXXXXXXXFFFFGGGGGAARRRRRTTTTT"
szukany = "AAB"

Znalezniony = BrutForce(ciag, szukany)
print("Przeszukiwany ciag 2 : ", ciag)
if (Znalezniony == True):
    print("Znaleziono")
else:
    print("NIE znaleziono")