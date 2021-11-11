# LZ 76103
# Algorytm zamiany liczby dziesietnej na dowolny system


digits = [] # tablica do przetrzymywania digitow w zaleznosci od dobranego systemu


# Generuje zestaw digitow wg podanej przez usera bazy(radix)
def digit_generator(userSystem):
    digitTab = []
    startChar_0 = 48 # znak startowy 0 - 9
    startChar_A = 65 # znak startowy A - Z
    counter = 0
    i = 0
    while (userSystem != 0):
        if(i >= 0 and i <= 9):
            digitTab.append(chr(startChar_0 + counter))
            counter += 1
        if (i == 9):
            counter = 0 # reset
        if (i > 9 and i <= 33):
            digitTab.append(chr(startChar_A + counter))
            counter += 1

        userSystem -= 1
        i += 1
    return digitTab # zwracamy tablice digitow


# Zwraca litere(lub liczbe) w zaleznosci od podanej wartosci liczbowej
def number_to_digit(number, digits):
    digit = digits[number]
    return digit


def reverse_string(string):
    revers = ""
    for e in reversed(string):
        revers = revers + e
    return revers


def dec_to_user_system(dec, base, digits):
    converted = ""
    moduloRest = 0
    roundValue = 0
    value = dec
    finalResult = ""
    while(moduloRest != 1):
        moduloRest = value % base
        roundValue = round(value// base)
        system = number_to_digit(moduloRest, digits)
        converted = converted + system
        value = roundValue
    finalResult = reverse_string(converted) # Rewers stringa
    return finalResult


decUser = input("Podaj liczbę w zapisie dziesietnym: ")
baseUser = int(input("Podaj baze(radix) systemu docelowego: "))


digits = digit_generator(baseUser)

res = dec_to_user_system(int(decUser), int(baseUser), digits)
print(f"Konwesja liczby: {decUser} baza-10 = {res} baza-{baseUser} ")
