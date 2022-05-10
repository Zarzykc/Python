#break

wynik = 0

for i in range(3):
    x = int(input("Podaj liczbę dodatnią: "))
    if (x > 0):
        wynik += x
    else:
        print("Dodatnia!")
        continue
    print("Aktualny wynik dodawania to: ", wynik)