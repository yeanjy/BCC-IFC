import random
jogadas = 10

def simular():
    sequencia = ""
    lancamentos = 0
    while True:
        resultado = random.choice(["A", "O"])
        sequencia += resultado[0].upper()
        lancamentos += 1
        if len (sequencia) >= 3 and sequencia[-3] == sequencia[-2] == sequencia[-1]:
            break
    print (f"{' '.join(sequencia)} - {lancamentos} lancamentos")
    return lancamentos

resultados = [simular() for _ in range(jogadas)]
media = sum(resultados) / jogadas
print(f"Média de {media:.2f} lançamentos")