pi = 3
sinal = 1
for n in range(2, 33, 2):
    numerador = 4
    d = n*(n+1)*(n+2)*sinal
    apro = numerador/d
    pi += apro
    sinal = sinal*-1
print (pi)