plik = open("anagramy.txt","r").readlines()
# print(plik)


'''
def czy_anagram(wyraz1, wyraz2):
    
    dlugosc1 = len(wyraz1)
    dlugosc2 = len(wyraz2)

    # sprawdzenie po dlugosci wyrazenc
    if (dlugosc1 != dlugosc2):
        return False
    else:
        return True
''' 
    
anagrams_counter = 0

for wyraz in plik:
    wyrazsplited = wyraz.split(' ')
    wyraz1 = wyrazsplited[0]
    wyraz2 = wyrazsplited[1].split('\n')

    b_anagram = czy_anagram(wyraz1, wyraz2 )

    if (b_anagram):
        print("To jest anagramm")
        anagrams_counter += 1
    else:
        print("To nie jest anagram")
print("Znaleziono anagramow: ", anagrams_counter)


# anagramow 93

