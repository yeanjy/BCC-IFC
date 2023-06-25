def valnumericos():
    valor = (input("Digite (tecle enter para parar):"))
    result = 0
    if valor == "":
        return result
    else:
        valor = int(valor)
        result += valor
        return result + valnumericos()

print(valnumericos())