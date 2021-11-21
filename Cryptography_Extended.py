# LZ nr indeksu: 76103

# KODOWANIE DLUGOSCI SERII - ROZBUDOWANE (Ocena 5.0)

# STEPS :
# Read string from user
# Converting from string of chars to ASCII string  
# Determining max value from string , ex max = 700
# Checking how meny bits needed to cover max int value
# kodowanie calego lancucha na postac binary w zaleznosci od tego ile bitow potrzeba by wyrazic liczbe
# Converting by counting 0 or 1 (bits)
# Coverting bits string to chars string 


# change string to ASCII values string
def toAsciiIntString(string):
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


# Change int value to binary value depending on how many bits is needed
# intChar : char given by int (ASCII)
# bitsQuantity : quantity of bits to expressed int(Char) value
def intToBits(intChar, bitsQuantity):
    binary = []
    binaryString = ""
    bitCounter = 0
    bitCounter_Counter = bitsQuantity

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
# asciiString : string with ASCII signs
# bitsQuantity : quantity of bits to expressed int(Char) value
def toBinaryString(asciiString, bitsQuantity):
    stringBits = ""
    intChar = ""
    for i in asciiString:
        intChar += i 
        if(i == " "):
            bitsValue = intToBits(int(intChar), bitsQuantity)
            stringBits += bitsValue + " "
            intChar = ""
    return stringBits


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


# MAIN PROGRAM

bitsNeeded = 0 # Value for calculation of bits needed to cover max int value

# Read string from user
string = input("Type string to encryption: ")

# Coverting from string of chars to ASCII string  
asciiIntString = toAsciiIntString(string)
print(f"ASCII reflected by int: {asciiIntString}")

# Determining max value from string , ex max = 700
maxValue = extractMaxValueFromString(asciiIntString)
print(f"Max value in ascii int string: {maxValue}")

# Checking how meny bits needed to cover max int value
bitsQuantity = calculateBitsNeededToDescribeValue(maxValue)
print(f"Bits needed to cover max value: {bitsQuantity}")

# kodowanie calego lancucha na postac binary w zaleznosci od tego ile bitow potrzeba by wyrazic liczbe
binaryString = toBinaryString(asciiIntString, bitsQuantity)
print(f"{bitsQuantity} bits string: ", binaryString)

# Converting by counting 0 or 1 (bits)
valuesString = bitsToHiddenCode(binaryString)
print(f"coded to bits string: {valuesString}")

# Coverting hidden code to chars 
charsString = hiddenToChars(valuesString)
print(f"Bits string converted to chars : {charsString}")