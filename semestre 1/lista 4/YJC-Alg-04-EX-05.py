criança = 14
adulto = 23
idoso = 18
bebe = 0
total = 0

while True:
    idade = input("Digite a idade do visitante(Tecle enter para encerrar): ")
    if idade == "":
        break
    idade = int(idade)
    if idade in list(range(3, 13)):
        total += criança
    elif idade in list(range(13, 65)):
        total += adulto
    elif idade in list(range(0, 3)):
        total += bebe
    else: 
        total += idoso
print (f"O total da passage é R${total:.2f}")