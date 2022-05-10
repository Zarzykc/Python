#zadanie z suma liczb pętla

from cmath import pi


wynik = 0

i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik dodawania 4 liczb to: ", wynik)