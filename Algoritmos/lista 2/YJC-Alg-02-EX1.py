d = int (input("Digite o número de dias:"))
h = int (input("Digite o número de horas:"))
m= int (input("Digite o número de minutos:"))
s = int (input("Digite o número de segundos:"))
ds = d*24*3600
hs = h*3600
ms = m*60
s2 = ds + hs + ms + s

print ("O toral de segundos é de", s2)