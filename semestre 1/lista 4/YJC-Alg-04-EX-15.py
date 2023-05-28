decimal = int(input("Digite um número decimal: "))
result = ""

while decimal > 0:
    r = decimal % 2
    result = str(r) + result
    decimal //= 2

print("O número binário correspondente é:", result)
