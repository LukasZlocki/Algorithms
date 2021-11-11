# LZ 76103
# Algorytm znajdywania Palindromow - trudniejszy
# - palindrom minimum 2- znaki
# - jesli istnieje wiecej niz jeden palindrom, podac najdluzszy


# Przykladowe ciagi znakow z palindromami
ciag1 = "CABCBAB" # 1x palindrom
ciag2 = "CABCAB" # 0x palindrom
ciag3 = "ABCABCDEEDCBATT" # 1x palindrom
ciag4 = "EFGGFEZZOOABCDEFGGFED" # 2x palindrom ,
ciag5 = "ABVABCCBAERT" # 1x palindrom ,


# sprawdza czy podany tekst jest palindromem
def czy_palindrom(tekst):
    dl = len(tekst)
    if dl < 1:
        return False
    for i in range(dl // 2):
        if tekst[i] != tekst[dl - i - 1]:
            return False
    return True

# Poszukuje palindromow w zadanym ciagu - jesli znajdzie symetrie to wysyla do weryfikacji do funkcji czy_palindrom
def sprawdz_ciag(ciag):
    j = 0
    i = 0
    isPalindrom = False
    palindrom = ""
    for el1 in ciag:
        j = i
        for el2 in ciag[j:]:
            if (el1 == el2):
                #j += 1
                tekst1 = ciag[i:j+1]
                wynik = czy_palindrom(tekst1)
                if (len(tekst1) > 2 and wynik == True):
                    if(len(palindrom) < len(tekst1)): # przypisujemy najdluzszy palindrom w wyszukanym do tej pory tekscie
                        palindrom = tekst1
                    isPalindrom = True
            j += 1
        i += 1
    if (isPalindrom == False):
        print("Odpowiedź : brak")
    else:
        print("Odpowiedź : ", palindrom)
    return palindrom # zwrot wykrytego palindromu


print("*************")
print(f"Ciag znakow: {ciag1}")
sprawdz_ciag(ciag1)

print("*************")
print(f"Ciag znakow: {ciag2}")
sprawdz_ciag(ciag2)

print("*************")
print(f"Ciag znakow: {ciag3}")
sprawdz_ciag(ciag3)

print("*************")
print(f"Ciag znakow: {ciag4}")
sprawdz_ciag(ciag4)

print("*************")
print(f"Ciag znakow: {ciag5}")
sprawdz_ciag(ciag5)
