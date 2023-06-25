def DecBinRecursivo(q):
    result = ""
    if q < 0:
        return "ERROR, numero negativo"
    elif q == 0:
        return result
    else:
        r = q%2
        result = str(r) + result
        q = q//2
        return DecBinRecursivo(q) + result
    
q = int(input("Digite:"))
print(DecBinRecursivo(q))