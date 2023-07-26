def listaordenada(lista):
    if not lista:
        return "Lista Vazia"
    elif len(lista) == 1:
        return "Lista de um elemento"
    elif lista == sorted(lista) or lista == sorted(lista, reverse=True):
        return True
    else:
        return False

lista = []
while True:
    numero = input("Digite o numero, aperte enter para encerrar: ")
    if numero == "":
        break
    numero = float(numero)
    lista.append(numero)

resultado = listaordenada(lista)
print(resultado)
