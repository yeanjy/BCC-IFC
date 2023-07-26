l = int(input("Digite o número de lados de um polígono"))

while l < 3 or l > 10:
    print ("Digite um número de 3 a 10")
    l = int(input("Digite o número de lados de um polígono"))

if l == 3:
    print("É um triângulo")
elif l == 4:
    print("É um quadrilátero")
elif l==5:
    print("É um pentágono")
elif l == 6:
    print("É um hexágono")
elif l == 7:
    print("É um heptágono")
elif l == 8:
    print("É um octógono")
elif l == 9:
    print("É um eneágono")
elif l == 10:
    print("É um decágono")