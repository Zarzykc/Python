import math
wybor = input("+ - dodawanie, - - odejmnowanie, * - mnożenie, / - dzielenie, ** - potęgowanie, % - modulo(reszta z dzielenia)")

a = int(input("Wybierz pierwszą liczbę: "))
b = int(input("Wybierz drugą liczbę: "))

if (wybor == '+'):
    print(a + b)
elif (wybor == "-"):
    print(a - b)
elif (wybor == "*"):
    print(a * b)
elif (wybor == '/'):
    if b == 0:
        print("Nope")
    else:
        print(a / b)
elif (wybor == '**'):
    print(a ** b)
elif (wybor == '%'):
    print(a % b)
else:
    print("Nie wybrano odpowiedniej opcji")
