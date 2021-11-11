# LZ 76103
# Algorytm zamiany z dowolnego systemu na system dziesietny


digit = [] # tablica do przetrzymywania digitow w zaleznosci od dobranego systemu


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


# Zwraca numer w zaleznosci od podanego digitu w wygenerowanej bazie digitow
def digit_to_number(digit, digits):
    number = 0
    for dig in digits:
        if(digit == dig):
            return number
        number += 1
    return number


# Potegowanie
def potegowanie(podstawa, potega):
    wynik = 1
    for i in range(potega):
        wynik = wynik * podstawa
    return int(wynik)


# generator liczby decymalnej.
def to_Dec(number, base, digits):
    dec = 0
    potega = 0
    for e in reversed(number):
        liczba = digit_to_number(e, digits)
        dec = dec + liczba * potegowanie(base, potega)
        potega += 1
    return dec


# Przyjecie liczby od usera
userNb = input("Podaj liczbe dowolnego systemu (np. 5G): ")
userNb = userNb.upper() # konwersja male / duze litery
userBase = int(input("Podaj baze systemu (np 8 -hexa): "))
print(f"Liczba {userNb} baza-{userBase}")
print("Konwertuje do Dec ...")

# Generuje digity dla podanej przez uzykownika bazy
digits = digit_generator(userBase)

# konwersja z systemu usera do Dec
dec = to_Dec(userNb, userBase, digits)
print(f"Konwesja liczby do Dec : {userNb} baza-{userBase} = {dec} baza-10 ")



# --- TESTY ---
# T E S T Y - tablica z digitami
def test_generowanej_tablicy_z_digitami():
    assert digit_generator(5) == ['0', '1', '2', '3', '4']
    assert digit_generator(13) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']

test_generowanej_tablicy_z_digitami()


# T E S T Y - funkcja zwracajaca numer w zaleznosci od podanego digitu
def test_funkcji_zwracajace_numer():
    assert digit_to_number('C', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']) == 12
    assert digit_to_number('3', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']) == 3

test_funkcji_zwracajace_numer()