# LZ 76103
# Compression Huffman

import math

table = [0 for element in range(127)]


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

string = "AABBABBC" # string to compress
temporary_string = ""
output_string = ""

print(f"String to compress: {string}")

# Step 1: Calculations signs quantity
for el in string:
    L += 1
    position = give_me_int_base_on_char(el)
    update_table(position)
print(f"Calculated signs quantity L: {L}")

# Step 2: different signs calculation
X = give_me_table_sum(table)
print(f"calculated different signs X: {X}")

# Step 3: calculating bits for mask creation
N = calculating_N_bits_to_create_mask(give_me_table_sum(table))
print(f"Calculated bits needed to create mask N: {N}")

# Step 4: Dictionary as char
char = chr(X)
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
print(F"Temporary string: {temporary_string}")    

# Step 8: adding string letters to temporary string base on calculated mask
batch_string = temporary_string # add R value to begining of string
bit8_string = ""    # first 8bits
bit_rest_string = ""    # next bits after 8th bit 
for element in string:
    batch_string += mappa[element]
    a = len(batch_string)
    if ( a >= 8):
        bit8_string = batch_string[:8]  # first 8bits
        bit8_dec = bin_to_dec(bit8_dec)
        char = give_me_char_base_on_int(bit8_dec)
        batch_string += char
        bit_rest_string = batch_string[8:]  # next bits after 8th bit 

    bit8_string = ""    # reset
    bit_rest_string = ""    # reset
    batch_string = ""   # reset

