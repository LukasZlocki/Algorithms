# LZ 76103
# Compression Huffman

import math

table = [0 for element in range(127)]


def give_me_int_base_on_char(char):
    int_char = 0
    int_char = ord(char)
    return int_char


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


# Main program

L = 0   # signs quantity
X = 0   # different signs
N = 0   # bits numbers needed to create mask of signs

string = "AABBABBC" # string to compress

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

#Step 4: Dictionary as char
char = chr(X)
print(f"char based on different signs quantity : {char}")