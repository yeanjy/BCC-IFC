def corrigirtxt(texto):
    textocorrigido = ""
    pmaiusculo = True

    for caractere in texto:
        if pmaiusculo and caractere.isalpha():
            textocorrigido += caractere.upper()
            pmaiusculo = False
        else:
            textocorrigido += caractere
        if caractere in [".", "?", "!"]:
            pmaiusculo = True
    return textocorrigido

entrada = input("Digite uma frase: ")
saida = corrigirtxt(entrada)
print (saida)