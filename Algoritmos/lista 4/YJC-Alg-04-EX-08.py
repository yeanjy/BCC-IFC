escolha = int(input("Digite 1 para codificar ou 2 para descodificar: "))

while escolha not in [1, 2]: 
    print ("Numero invalido") 
    escolha = int(input("Digite 1 para codificar ou 2 para descodificar: "))

if escolha == 1:
    cifra = input("Escreva uma frase que deseja codificar: ")
    deslocamento = int(input("Digite o deslocamento desejado:"))
    menssagemcodificada = ""

    for letra in cifra:
        if letra.isupper():
            nova_letra = chr((ord(letra) - 65 + deslocamento) % 26 + 65)
        elif letra.islower():
            nova_letra = chr((ord(letra) - 97 + deslocamento) % 26 + 97)
        else:
            nova_letra = letra
        menssagemcodificada += nova_letra
    print("Mensagem codificada:", menssagemcodificada)

else: 
    cocifra = input("Escreva uma frase que deseja descodificar: ")
    codeslocamento = int(input("Digite o deslocamento:"))
    mensagemdescodificada = ""

    for coletra in cocifra:
        if coletra.isupper(): 
            novaconovaletra = chr((ord(coletra) - 65 - codeslocamento)%26 + 65)
        elif coletra.islower():
            novaconovaletra = chr((ord(coletra) - 97 - codeslocamento)%26 + 97)
        else:
            novaconovaletra = coletra
        mensagemdescodificada += novaconovaletra

    print ("Mensagem descodificada:", mensagemdescodificada)
