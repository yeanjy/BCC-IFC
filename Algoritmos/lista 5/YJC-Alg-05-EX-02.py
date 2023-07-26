def valor(km):
    valorcorrido = 4 + (1000/140*0.25)*km
    return valorcorrido

km = float(input("Digite a distancia percorrida em km: "))
print ("O valor da sua corrida é de", valor(km))