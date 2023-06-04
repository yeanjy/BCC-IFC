lista = []

while True:
    numero = (input("Digite o numero, aperte enter para encerrar: "))
    if numero == "":
        break
    numero = float(numero)
    lista.append(numero)

numerosomado = 0
for num in lista:
    numerosomado += num
media = numerosomado/len(lista)
print("A media eh", media)

for number in lista:
    if media > number:
        print(number, "Esta abaixo da media")
    elif media == number:
        print (number, "Esta na media")
    else:
        print(number, "Esta a cima da media")