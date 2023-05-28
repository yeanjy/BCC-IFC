soma = 0
contador = 0

nota = float(input("Digite as suas notas(Tecle 0 para sair): "))
if nota == 0:
    print("ERROR. A primeira nota não pode ser 0.")

else:
    while nota!= 0:
        soma += nota
        contador += 1
        nota = float(input("Digite as suas notas(Tecle 0 para sair): "))
    média = soma / contador
    print(f"A sua média é {média}")