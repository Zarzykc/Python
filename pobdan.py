
Dzialanie = int(input("Wybierz działanie: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie, 5 - potegowanie, 6 - modulo(Reszta z dzielenia) "))

if (Dzialanie >= 1 and Dzialanie <= 6):
        a = int(input("Podaj liczbe 1: "))
        b = int(input("Podaj liczbę 2: "))
else:
        print("Zly wybor")

if (Dzialanie == 1):
    print(a + b)
elif (Dzialanie == 2):
    print(a - b)
elif (Dzialanie == 3):
    print(a * b)
elif (Dzialanie == 4):
    print(a / b)
elif (Dzialanie == 5):
    print(a ** b)
elif (Dzialanie == 6):
    print(a % b)
