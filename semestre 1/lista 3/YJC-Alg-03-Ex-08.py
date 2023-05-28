nota = input("Digite uma nota musical: ").lower()
letra = nota[0]
número = int(nota[1])
c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392
a4 = 440
b4 = 493.88

if letra in "c":
    if número in [0, 1, 2 ,3 , 4, 5, 6, 7, 8]:
        notac = c4/2**(4-número)
        print(f"A frquência da nota é {notac}")
elif letra in "d":
    if número in [0, 1 ,2 ,3 , 4, 5, 6, 7, 8]:
        notad = d4/2**(4-número)
        print(f"A frquência da nota é {notad}")
elif letra in "e":
    if número in [0, 1 ,2 ,3 , 4, 5, 6, 7, 8]:
        notae = e4/2**(4-número)
        print(f"A frquência da nota é {notae}")
elif letra in "f":
    if número in [0, 1 ,2 ,3 , 4, 5, 6, 7, 8]:
        notaf = f4/2**(4-número)
        print(f"A frquência da nota é {notaf}")
elif letra in "g":
    if número in [0, 1 ,2 ,3 , 4, 5, 6, 7, 8]:
        notag = g4/2**(4-número)
        print(f"A frquência da nota é {notag}")
elif letra in "a":
    if número in [0, 1 ,2 ,3 , 4, 5, 6, 7, 8]:
        notaa = a4/2**(4-número)
        print(f"A frquência da nota é {notaa}")
elif letra in "b":
    if número in [0, 1 ,2 ,3 , 4, 5, 6, 7, 8]:
        notab = b4/2**(4-número)
        print(f"A frquência da nota é {notab}")
else:
    print("Digite uma nota válida")