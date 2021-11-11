# LZ 76103
# Algorytm Boyera-Moore'a



txt1 = "Z pamietnika mlodej lekarki"
wzorzec1 = "lek"

txt2 = "ilek"
wzorzec2 = "lek"

txt3 = "werthlekoerytytrty"
wzorzec3 = "lek"

txt4 = "l"
wzorzec4 = "lek"


# jak w opisie funkcji
def kalkulacja_przesuniecia_wzorca_jesli_jest_litera_tekstu_we_wzorcu(literaTextu, wzorzec):
    index = len(wzorzec) - 1
    offset = 0
    while(index != -1):
        if (wzorzec[index] == literaTextu):
            return offset # znaleziono litere , zwracamy index pozycji
        else:
            index -= 1
            offset += 1
    return 0 # nie znaleziono litery, nie pozycjonujemy tekstu


# Algorytm Boyera-Moore'a
def BM_Check(tekst, wzorzec):

    wzorzecLength = len(wzorzec)
    tekstLength = len(tekst)

    wzorzecIndex = wzorzecLength - 1 # index ostatniej litery wzorca
    tekstIndex = wzorzecIndex # index ostatniej litery wzorca na badanym tekscie

    skok = wzorzecLength # dlugosc tekstu wzorca

    while tekstIndex < tekstLength:
        if tekst[tekstIndex] == wzorzec[wzorzecIndex]:
            # jesli zgadza sie litera, sprawdza pozostale litery wzorca w tekscie w badanym odcinku tekstu
            i = 0
            wzorzec_counter = wzorzecLength
            while(tekst[(tekstIndex - i)] == wzorzec[(wzorzecIndex - i)]):
                    i += 1
                    wzorzec_counter -= 1
                    if (wzorzec_counter == 0):
                        return True # sprawdzono wszystkie litery, jest pelen wzorzec w tekscie
            tekstIndex = tekstIndex + skok

        else:  # wzorzec nie pasuje przechodzimy dalej do poszukiwan
            # sprawdza czy pomimo ze ostatnia litera sie nie zgadza to czy wystepuja pozostale litery w tekscie i mozna dokonac przesuniecia wzorca
            i = wzorzecLength
            ti = tekstIndex
            offsetWzorca = 0 # jesli 0 to nie znaleziono
            while (i != 0):
                offsetWzorca = kalkulacja_przesuniecia_wzorca_jesli_jest_litera_tekstu_we_wzorcu(tekst[ti], wzorzec) # sprawdza czy jest litera i podaje offset
                if (offsetWzorca != 0):
                    i = 0 # przerywam petle, mam wartosc offsetu -> offsetWzorca
                else:
                    i -= 1
                    ti -= 1
            if (offsetWzorca == 0):
                tekstIndex += skok  # przesuwamy tekst o skok poniewaz nie podjeto centrowania na literze (brak litery)
            else:
                tekstIndex = tekstIndex + offsetWzorca # znaleziono litere centrujemy wzorzec wzgledem tekstu na znalezionej literze
    return False


print(f"Przeszukiwany tekst : {txt1}")
print(f"Wzorzec: {wzorzec1}")
znaleziono = BM_Check(txt1, wzorzec1)
print(f"Znaleziono wzorzec: {znaleziono}")
print("***")

print(f"Przeszukiwany tekst : {txt2}")
print(f"Wzorzec: {wzorzec2}")
znaleziono = BM_Check(txt2, wzorzec2)
print(f"Znaleziono wzorzec: {znaleziono}")
print("***")

print(f"Przeszukiwany tekst : {txt3}")
print(f"Wzorzec: {wzorzec3}")
znaleziono = BM_Check(txt3, wzorzec3)
print(f"Znaleziono wzorzec: {znaleziono}")
print("***")

print(f"Przeszukiwany tekst : {txt4}")
print(f"Wzorzec: {wzorzec4}")
znaleziono = BM_Check(txt4, wzorzec4)
print(f"Znaleziono wzorzec: {znaleziono}")
print("***")



#  T E S T Y - kalkulacja przesuniecia wzorca
def validacja_kalulacji_przesuniecia_wzorca():
    assert kalkulacja_przesuniecia_wzorca_jesli_jest_litera_tekstu_we_wzorcu('l', "lek") == 2 # ---
    assert kalkulacja_przesuniecia_wzorca_jesli_jest_litera_tekstu_we_wzorcu('k', "abcdkeefgh") == 5 # srodek
    assert kalkulacja_przesuniecia_wzorca_jesli_jest_litera_tekstu_we_wzorcu('a', "abcdkeefgh") == 9 # lewy kraniec
    assert kalkulacja_przesuniecia_wzorca_jesli_jest_litera_tekstu_we_wzorcu('h', "abcdkeefgh") == 0 # prawy kraniec

# T E S T Y - caly algorytm Boyera i Moore'a
def validacja_algorytmu_dla_parametrow_tekst1_i_wzorzec1():
    assert BM_Check("ilek", "lek") == True
    assert BM_Check("Z pamietnika mlodej lekarki", "lek") == True
    assert BM_Check("werthlekoerytytrty", "lek") == True
    assert BM_Check("lek", "lek") == True
    assert BM_Check("l", "lek") == False


#  T E S T Y - kalkulacja przesuniecia wzorca
validacja_kalulacji_przesuniecia_wzorca()

# T E S T Y - caly algorytm Boyera i Moore'a
validacja_algorytmu_dla_parametrow_tekst1_i_wzorzec1()