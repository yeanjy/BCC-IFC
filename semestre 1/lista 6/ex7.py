def divisores(numero):
    lista = []
    a = numero
    while a > 0:
        if numero % a == 0:
            lista.append(numero // a)
        a = a - 1
    del lista[-1]
    return lista

def perfectnumber(numero):
    divisor = divisores(numero)
    novonumero = 0
    for div in divisor:
        novonumero += div
    if numero == novonumero:
        return True
    else:
        return False

numero = int(input("Digite: "))
divisores_numero = divisores(numero)
numeroperfeito = perfectnumber(numero)
print(divisores_numero)
print(numeroperfeito)
