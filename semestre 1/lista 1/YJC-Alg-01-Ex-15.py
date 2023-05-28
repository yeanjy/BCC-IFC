from math import *
l = float (input("Digite o lado do polígono regular em metros"))
n = int (input("Digite o número de lados"))

area = (n*l**2)/4*tan(pi/n)
print ("A área do poligono é", area, "m2")