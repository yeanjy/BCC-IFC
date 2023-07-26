def hex2int(hexadecimal):
    resultado = ["A", "B", "C", "D", "E", "F"]
    if hexadecimal in resultado:
        return resultado.index(hexadecimal) + 10
    else:
        return "Letra inválida."

hexadecimal = input("Digite uma letra de A a F: ").upper()
print(hex2int(hexadecimal))


def int2hex(numero):
    digitos_hex = '0123456789ABCDEF'
    
    if 0 <= numero <= 15:
        return digitos_hex[numero]
    else:
        return "Número inteiro fora do intervalo 0-15."

numero = int(input("Digite um numero: "))
print (int2hex(numero))