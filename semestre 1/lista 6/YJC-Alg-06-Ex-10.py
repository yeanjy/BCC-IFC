def formatarlista(lista):
    frase = ""
    for list in lista:
        if list in lista[-1]:
            frase += " e " + list
        elif list in lista[-2]:
            frase += list
        else:
            frase += list + ", "
    return frase

def main():
    lista = ["A", "B", "C", "D", "E"]
    a = formatarlista(lista)
    print(a)
main()