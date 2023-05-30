def divisores(numero):
    lista = []
    a = numero
    while a > 0:
        if numero%a == 0:
            lista.append(numero//a)
        a = a-1
    return lista

def main():
    numero = int(input("Digite:"))
    numero = divisores(numero)
    print(numero)
main()
