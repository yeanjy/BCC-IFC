posição = input("Insira uma posição no tabuleiro do xadrez: ").lower()
letra = posição[0] 
numero = int(posição[1])

if letra in "BDFH":
    pc = "branco"
    if numero in [1, 3, 5, 7]:
        print (f"A {posição} é branco")
    else:
        print(f"A {posição} é preto")
else:
    pc = "preto"
    if numero in [2, 4, 6, 8]:
        print (f"A {posição} é branco")
    else:
        print(f"A {posição} é preto")
