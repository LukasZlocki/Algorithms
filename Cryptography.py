# Lab3 Zadanie 2


# Story :
# Ocena 5.0 
#
# Ocena 4.0
# DONE - Ciagi 2 1 4 1 1 1 5 1 zamienic na znaki - uwaga znaki niewidoczne i wyjatki
# Wyjateki -> Zabezpieczyc i rozbic liczby > 255 w ciagu
#
# Ocena 3.0
# DONE - Odczytac string do zamiany
# DONE - String na ciag liczb ASCII ze spacjami
# DONE - Kazda z liczb zamieniamy na wartosc 8bit binarna i zapisujemy do ciagu ze spacjami 
# DONE - Ciag 8bit zamieniamy na informcje o kolejnych dlugosciach ciagow znakow (0 lub 1) np 2 1 3 1 1 1 5 1 1 1 4 1 2 1 1 1 1 1 1 (bez spacji)





string = "!AB*"


# change string to ASCII values string
def toAsciiString(string):
    stringASCII =""
    for e in string:
        stringASCII += str(ord(e)) + " " 
    return stringASCII


# Change int value to 8bits value
def intTo8Bits(intChar):
    binary = []
    binaryString = ""
    bitCounter = 0
    bitCounter_Counter = 8

    while (intChar > 0):
        d = intChar % 2
        binary.append(d)
        intChar = intChar // 2
        bitCounter += 1  # for bit adder purpose  
    
    # adding bits in order to sustain 8bit digit
    bitLoop = 0
    bitLoop = bitCounter_Counter - bitCounter 
    while(bitLoop != 0):
        binaryString += "0"
        bitLoop -= 1

    binary.reverse() # revers list with calculations
    # Final assembly of bit string
    for e in binary:
        binaryString += str(e)   
    return binaryString


# Convert string with ints to string with 8bits digits which represents given int string
def toBinaryString(asciiString):
    string8Bit = ""
    intChar = ""
    for i in asciiString:
        intChar += i 
        if(i == " "):
            bitValue = intTo8Bits(int(intChar))
            string8Bit += bitValue + " "
            intChar = ""
    return string8Bit


# convert bits string to string of signs basis on counting 1/0  
def bitsToHiddenCode(bitsString):
    hiddenCode = ""
    sign = "0"
    counter = 0
    for e in bitsString:       
        if e != sign and e != " ":
            hiddenCode += str(counter) + " "
            sign = e
            counter = 1
        elif e == sign and e != " ":
            counter += 1
        if e == " ":
            hiddenCode += str(counter) + " "
            counter = 0
            sign = "0"
    return hiddenCode


# splits values > 255 to string which enables to convert it to char string.  example: 700 -> 255 0 255 0 190
def splitValue(value):
    splitedString = value
    if value > 255:
        MAX_VALUE = 255
        splitedString = "255"
        c = 0
        while(value >= MAX_VALUE):
            value = value - MAX_VALUE
            splitedString += " 0 " + str(value)
    return str(splitedString)


# Check valueString to find values > 255, if value > 255 find splitValue method is run to split value
def checkValueString(valuesString):
    checkedValueString = ""
    partialString = ""
    for e in valuesString:
        if  e != " ":
            partialString += e
        if e == " ":
            partialString = splitValue(int(partialString))
            checkedValueString += partialString + " " 
            partialString = "" # set to base                  
    return checkedValueString


# Convert hidden code to chars 
def hiddenToChars(hiddenString):
    hiddenChars = ""
    for e in hiddenString:
        if (e != " "):
            hiddenChars += str(chr(int(e))) + " "
    return hiddenChars


# Read string from user
string = input("Podaj string do zamiany: ")

# Coverting from string of chars to ASCII string  
asciiString = toAsciiString(string)
print(f"ASCII: {asciiString}")

# Converting from ASCII string to 8bits 
bitString = toBinaryString(asciiString)
print(f"8bits: {bitString}")

# Converting from 8bits string to string of values basis on counting 0 or 1 (bits)
valuesString = bitsToHiddenCode(bitString)
print(f"Hidden code: {valuesString}")

# Checking valueString to find values > 255, split such a values and separating them by 0,  example: 700 -> 255 0 255 0 190
valuesAfterCheckValueString= checkValueString(valuesString)
print(f"Hidden code check if > 255. If needed spliting values > 255. result: {valuesAfterCheckValueString}")

# Coverting hidden code to chars 
charsString = hiddenToChars(valuesString)
print(f"Hidden code converted to chars : {charsString}")

# Summary
print("")
print("SUMMARY:")
print("String to coversion:", string)
print("String after conversion: ", charsString)


# TESTS
print("")
print("")
print("String test with values > 255")
# Check valuesString text
probe = "2 3 4 8 500 1 8 700 "
res = checkValueString(probe)
print(f"Probe string: {probe}")
print("result: ", res)

# Check valuesString text
probe = "2 3 4 8 500 1 8 700 "
res = checkValueString(probe)
print(f"Probe string: {probe}")
print("result: ", res)

