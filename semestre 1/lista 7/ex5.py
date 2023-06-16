def caracteresunico(a, b):
    if len(a) != len(b):
        return False
    
    a1 = sorted(list(a))
    b1 = sorted(list(b))
    return True if a1==b1 else False

frase = input("Digite: ").upper()
frase2 = input("Digite: ").upper()
resultado = caracteresunico(frase, frase2)
print(resultado)
