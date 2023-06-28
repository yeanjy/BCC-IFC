def DecBinInterativo(q):
    result = ""
    while q>0:
        r = q%2
        result = str(r) + result
        q= q//2
    return result

q = int(input("Digite:"))
print(DecBinInterativo(q))