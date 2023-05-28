x = float(input("Digite um número para calcular a raiz quadrada: "))
raiz = x / 2

while abs(raiz * raiz - x) > 10**-12:
    raiz = (raiz + x/raiz) / 2

print(f"A raiz quadrada de {x} é {raiz}")