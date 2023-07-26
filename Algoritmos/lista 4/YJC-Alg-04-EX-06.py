while True:
    bits = input("Digite os bits para verificar a paridade (tecle enter para sair): ")
    contador = bits.count("1")

    if bits == "":
        break

    if len(bits) != 8 or not all(c in "01" for c in bits) :
        print ("Erro, digite somente 1 e 0 com no maximo de 8 digitos.")
        continue
    
    if contador % 2 != 0:
        print("Bit de paridade 0")
    else:
        print("Bit de paridade 1")