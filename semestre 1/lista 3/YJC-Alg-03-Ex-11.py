from math import *
a = float(input("Dgite o a da equação: "))
b = float(input("Dgite o b da equação: "))
c = float(input("Dgite o c da equação: "))

delta = b**2 - 4*a*c

if delta == 0 :
    print("Possui 1 raiz real")
    raiz = -b / (2*a)
    print (f"A raíz é {raiz}")
elif delta < 0 :
    print("Não possui raízes reais")
else:
    print("Possui dois raízes reais")
    raiz1 = (-b + sqrt(delta)) / 2*a
    raiz2 = (-b - sqrt(delta)) / 2*a
    print (f"As raízes são {raiz1} e {raiz2}")
