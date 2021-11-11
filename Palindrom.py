plik = open("palindromy.txt","r").readlines()
# print(plik)
palindromy_lista = []


def czy_palindrom(palindrom):
    i = 0
    j = len(palindrom)

    for element in palindrom:
        if element != palindrom[j - 2 - i]:
            return False
        i += 1
    return True


palindroms_counter = 0

for wyraz in plik:
    b_palindrom = czy_palindrom(wyraz)
    if (b_palindrom):
        print("To jest palindrom")
        palindroms_counter += 1
        palindromy_lista.append(wyraz)
    else:
        print("To nie jest palindrom")
print("Znaleziono palindromow: ", palindroms_counter)

# Zapis do pliku
SaveFile=open('output_palindromy.txt','w')
for element in palindromy_lista:
    print >> SaveFile, element




# palindromow 187


