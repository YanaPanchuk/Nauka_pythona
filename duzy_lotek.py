#LOSOWANIE LICZB

import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną liczbę losowania: "))

print("Wyświetl ilość typowanych liczb - %s, a także maksymalną liczbę losowania - %s." %(ileliczb, maksliczba))

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i += 1
print("Wyłosowane liczby to: ", liczby)