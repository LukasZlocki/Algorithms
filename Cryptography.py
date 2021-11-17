# Lab3 Zadanie 2


# Story :
# Ocena 5.0 
#
# Ocena 4.0
# DONE - Ciagi 2 1 4 1 1 1 5 1 zamienic na znaki - uwaga znaki niewidoczne i wyjatki
# Wyjateki -> Zabezpieczyc i rozbic  
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


# splits values > 255 to string which enables to convert it to char string
def splitValue(value):
    MAX_VALUE = 255
    splitedString = "255"
    c = 0
    while(value >= MAX_VALUE):
        value = value - MAX_VALUE
        splitedString += " 0 " + str(value)
    return splitedString


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


# Convert hidden code to chars 
def hiddenToChars(hiddenString):
    hiddenChars = ""
    for e in hiddenString:
        if (e != " "):
            hiddenChars += str(chr(int(e))) + " "
    return hiddenChars


# Read string from user
#string = input("Podaj string do zamiany: ")

# Covertion from string of chars to ASCII string 
asciiString = toAsciiString(string)
print(f"ASCII: {asciiString}")

# Convertion from ASCII string to 8bits 
bitString = toBinaryString(asciiString)
print(f"8bits: {bitString}")

# Conversion from 8bits string to string of signs basis on counting 0 or 1 (bits)
signsString = bitsToHiddenCode(bitString)
print(f"Hidden code: {signsString}")

# Covert hidden code to chars 
charsString = hiddenToChars(signsString)
print(f"Hidden converted to chars : {charsString}")

#SplitIt test
c = splitValue(700)
print(c)


"""
# --- TESTY ---
# T E S T Y - tablica z digitami
def test_generowanej_tablicy_z_digitami():
    assert digit_generator(5) == ['0', '1', '2', '3', '4']
    assert digit_generator(13) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']

test_generowanej_tablicy_z_digitami()
"""