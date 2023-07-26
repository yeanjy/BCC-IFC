ano = int(input("Digite um ano: "))

if ano%4 == 0:
    print("É um ano bissexto")
elif ano%100 == 0:
    print("Não é um ano bissexto")
elif ano%400 == 0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")