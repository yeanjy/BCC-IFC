def mediana(n1, n2, n3):
    maxn = max(n1, n2, n3)
    minn = min(n1, n2, n3)
    mediana = n1 + n2 + n3 - maxn - minn
    return mediana

n1 = int(input("Insira o numero 1: "))
n2 = int(input("Insira o numero 2: "))
n3 = int(input("Insira o numero 3: "))
print ("A mediana eh", mediana(n1, n2, n3))