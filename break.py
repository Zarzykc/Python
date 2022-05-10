#break

"""wynik = 0

for i in range(3):
    x = int(input("Podaj liczbę dodatnią: "))
    if (x > 0):
        wynik += x
    else:
        print("Dodatnia!")
        continue
    print("Aktualny wynik dodawania to: ", wynik)
    """



"""for i in range(10):
    if (i % 2 == 0):
        print(i)
    
for j in range(15):
    if (j % 2 == 1):
        print(j)    
"""

a = int(input("1 liczba to: "))
b = int(input("2 liczba to: "))

wynik = 0

if (a >= 0 and b < 10):
    print(a + b)   
elif (a < 0 and b < 0):
    print(a + b)
    
