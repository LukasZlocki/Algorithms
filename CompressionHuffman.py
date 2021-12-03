# LZ 76103
# Compression Huffman

import math

table = [0 for element in range(127)]


def read_string_to_compress():
    file = open("string2Compress.txt","r").readlines()
    string = ""
    for element in file:
        string += element
    return string


def write_string_compressed(string_compressed):
    with open("stringCompressed.txt", 'w') as file:
        file.write(string_compressed)


def save_dictionary(char):
    with open("dictionary.txt", 'w') as file:
            file.write(char)

def give_me_int_base_on_char(char):
    int_char = ord(char)
    return int_char

def give_me_char_base_on_int(int):
    char = chr(int)
    return char


def update_table(possition):
    table[position] = 1


def give_me_table_sum(table):
    sum = 0
    for e in table:
        sum += e
    return sum


def calculating_N_bits_to_create_mask(int_signs_quantity):
    n = math.ceil(math.log(int_signs_quantity,2))
    return n


def calculating_R_rest_bits(l, n):
    r = (8 - (l * n +3) %8) %8
    return r


# intChar - char express by int number
# N - bits numbers needed to create mask of signs
# Dec2Bin
def dec_to_bin(intChar, N):
    binary = ""
    bitCounter = 0
    bitCounter_Counter = N
    while (intChar > 0):
        d = intChar % 2
        binary += str(d)
        intChar = intChar // 2
        bitCounter += 1  # for bit adder purpose
    # adding bits in order to sustain N bit digit
    bitLoop = 0
    bitLoop = bitCounter_Counter - bitCounter 
    while(bitLoop != 0):
        binary += "0"
        bitLoop -= 1
    binary = binary[::-1]   # binary string reverse
    return binary


# Bin2Dec
def bin_to_dec(bin):
    dec = 0
    potega = 0
    for el in bin[::-1]:
        if (int(el) == 1 ):
            dec += 2**potega
        potega += 1
    return dec
 
 
# ******************************************************************************************
# Main program

L = 0   # signs quantity
X = 0   # different signs
N = 0   # bits numbers needed to create mask of signs
R = 0   # rest result

temporary_string = ""
output_string = ""

string = read_string_to_compress()
print(f"String to compress: {string}")

# Step 1: Calculations signs quantity
for el in string:
    L += 1
    position = give_me_int_base_on_char(el)
    update_table(position)
print(f"Calculated signs quantity L: {L}")

# Step 2: different signs calculation
X = give_me_table_sum(table)
print(f"Calculated different signs X: {X}")

# Step 3: calculating bits for mask creation
N = calculating_N_bits_to_create_mask(give_me_table_sum(table))
print(f"Calculated bits needed to create mask N: {N}")

# Step 4: Dictionary as char
char = chr(X)
save_dictionary(char)
print(f"char based on different signs quantity : {char}")

# Step 5: creating dictionary
counter = 0
char_counter = 0
mappa = {}
for element in table:
    if element == 1 :
        char = chr(counter)
        binary = dec_to_bin(char_counter, N)
        mappa[char] = binary
        # map = dict(chr : binary) # Maping char to its binary substitution
        char_counter += 1
    counter += 1
print(f"Dictionary: {mappa}")

# Step 6: Rest R calculation
R = calculating_R_rest_bits(L, N)
print(f"Calculating rest of bits R: {R}")

# Step 7: write to temporary string first 3 bits with R value
temporary_string = dec_to_bin(R, 3)

# Step 8 / 9 : creating 8 bits string and adding string letters to temporary string base on calculated mask
batch_string = temporary_string # add R value to begining of string
bit8_string = ""    # first 8bits
bit_rest_string = ""    # next bits after 8th bit 
batch_string_length = 0    # batch length
for element in string:  # "AABBABBC" AAB / BABB / C
    batch_string += mappa[element]
    batch_string_length = len(batch_string)
    if ( batch_string_length >= 8):
        bit_8_string = batch_string[:8]  # first 8bits
        rest = batch_string[8:]  # next bits after 8th bit 

        bit_rest_string += rest  # dodajemy ostatni bit nadprogramowy
        bit8_string += bit_8_string + " "  # dodajemy 8bitow do stringu glownego

        a = ""  # reset
        # batch_string = "" + bit_rest_string    # add rest bit and start counting
        batch_string = rest # adding rest bit to new calculation

if (batch_string_length < 8):   # adding rest bits if last batch of string len < 8
    bit_8_string = batch_string[:8]  # first 8bits
    bit_rest_string += "0"
    bit8_string += bit_8_string
    # Adding additional R bits to the end of bits string
    for el in range(R):
        bit8_string += "1"
    bit8_string += " "  # final separation sign 

print(f"string 8 bits before compression: {bit8_string}")
ascii_string = ""
string = ""
for e in bit8_string:
    if (e == " "):
        dec = bin_to_dec(string)
        ascii_string += str(dec) + " "
        string = ""
    if e != " ": 
        string += e 
print(f"8bits to int ASCII signs: {ascii_string}")

print("Transfering to final package version...")

string_coded_assembled = "" # final string assembly
for e in mappa:
    string_coded_assembled += str(e)
string = ""
for e in bit8_string:
    if (e == " "):
        dec = bin_to_dec(string)
        char = chr(dec)
        string_coded_assembled += char
        string = ""
    if e != " ": 
        string += e 

print(f"Final package: {string_coded_assembled}")
write_string_compressed(string_coded_assembled)

