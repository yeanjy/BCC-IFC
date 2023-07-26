binario = input("Digite um número binário: ")

decimal = 0
expoente = len(binario) - 1

for digito in binario:
    decimal += int(digito) * 2**expoente
    expoente -= 1

print("O número decimal correspondente é:", decimal)

