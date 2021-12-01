# LZ 76103
# Compression Huffman

table = [0 for element in range(127)]


def give_me_int_base_on_char(char):
    int_char = 0
    int_char = ord(char)
    return int_char


def update_table(possition):
    table[position] = 1





# Main program

string = "AABBABBC" # string to compress

print("String to compress:")
print(string)

for el in string:
    position = give_me_int_base_on_char(el)
    update_table(position)

print("Table with letters")
print(table)