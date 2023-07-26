def raizquadrada(n, estimativa):
    if abs(estimativa**2 - n) < 10**-12:
        return estimativa
    return raizquadrada(n, (estimativa + (n / estimativa)) / 2)

n = int(input("Digite: "))
print(raizquadrada(n, 1))
