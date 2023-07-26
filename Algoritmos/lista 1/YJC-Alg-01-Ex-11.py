from math import *
t1 = radians (float (input("Digite a latitude do primeiro ponto")))
g1 = radians(float (input("Digite a longitude do primeiro ponto")))
t2 = radians (float (input("Digite a latitude do segundo ponto")))
g2 = radians (float (input("Digite a longitude do segundo ponto")))

distancia = 6371.01*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
print ("A distância entre esses dois pontos é de", distancia, "km")