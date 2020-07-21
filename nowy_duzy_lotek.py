#DUŻY LOTEK ZRIOBIONY ZA POMOCĄ ZBIORU

import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę "))

print("Wytypuj %s z %s liczb." %(ileliczb, maksliczba))

typy = set()
i = 0
while i < ileliczb:
    typ = input("Podaj liczbę %s " %(i + 1))
    if typ not in typy:
        typy.add(typ)
        i += 1
print("Pokaż wylosowane liczby: ", typy)