# Lab3 Zadanie 2 wersja na 5 !!

# KODOWANIE DLUGOSCI SERII - ROZBUDOWANE (5.0)
# ToDo:
# wrtosc ciagu 1, 2 ,3 700, 20, 30 , 500 zapisac dynamicznie w zaleznosci od max artosci ciagu : np 700 zapiszemy na 10 bitach
#           DONE - okreslic jaka max wartosc ma ciag 
#           DONE - wyznaczyc na ilu bitach nalezy to zapisac
#           - usunac funkcje rozbijania wartosci tak, by przypadkiem nie rozbic > 255
#           - przerobic funkcje gdzie generowany jest ciag wartosci by jej parametrem byl string oraz juz wyznaczona wartosc bitowego zapisu.




string = "!AB*"


# change string to ASCII values string
def toAsciiString(string):
    stringASCII =""
    for e in string:
        stringASCII += str(ord(e)) + " " 
    return stringASCII


# Calculate bits needed to describe value in binary system
def calculateBitsNeededToDescribeValue(value):
    bits = 1
    counter = 1
    bitsSum = 0
    while(bitsSum < value):
        counter *= 2 
        bitsSum += counter 
        bits += 1

    return bits

# Extract max value from string
def extractMaxValueFromString(stringAscii):
    char = ""
    maxValue = 0
    value = 0
    for i in stringAscii:
        char += i 
        if(i == " "):
            # Tutaj wyznaczyc ile bitow jest potrzebne
            value = int(char)
            if(value > maxValue):
                maxValue = value
            char = ""
    return maxValue


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



# TESTY NOWEJ FUNKCJONALNOSCI:

# Test sprawdzania ile bitow jest potrzebnych do opisania max wartosci w stringu
bitString = "1 2 3 700 5 20"
maxValue = extractMaxValueFromString(bitString)
print(maxValue)

bits = calculateBitsNeededToDescribeValue(700)
print(bits)

"""
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

"""