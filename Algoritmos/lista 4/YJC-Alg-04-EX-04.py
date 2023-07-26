from math import *
perimetro = 0

x1 = float(input("Digite a cordenada x de um ponto:"))
y1 = float(input("Digite a cordenada y de um ponto:"))

while True:
    x2 = input("Digite a cordenada x de um ponto (enter para sair):")
    if x2 == "":
        break
    y2 = float(input("Digite a cordenada y de um ponto:"))
    x2 = float(x2)
    d = sqrt((y2-y1)**2+(x2-x1)**2)
    perimetro += d 
    x1 = x2
    y1 = y2 
print(f"O perímetro deste polígono é igual a {perimetro}")