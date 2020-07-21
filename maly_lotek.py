#LOSOWANIE LICZB OD 1 DO 10 Z MOŻLIWOŚCIU ZGADNIENIA LICZBY PRZEZ UŻYTKOWNIKA

import random

liczba = random.randint(1, 10)
#print("Wyłosowana liczba to: ", liczba)
for i in range(3):
    print("Próba", i + 1)
    odp = input("Jaką liczbę mam na myśli? ")
    if liczba == int(odp):
        print("Zgadłeś!!!")
    elif i == 2:
        print("Miałam na myśli liczbę: ", liczba)
    else:
        print("Spróbuj jeszcze")
        print()

