
import random

CAPACIDADE = 5  # capacidade da mochila

ITENS = [
    (6,1),
    (3,2),
    (8,3),
    (9,4)
]

NUM_ITENS = len(ITENS)

POPULACAO_TAM = 30
GERACOES = 20
TAXA_MUTACAO = 0.05
TAXA_CRUZAMENTO = 0.8
TORNEIO_TAM = 3

def gerar_individuo():
    return [random.randint(0, 1) for _ in range(NUM_ITENS)]

def fitness(individuo):
    valor_total = 0
    peso_total = 0
    for i in range(NUM_ITENS):
        if individuo[i] == 1:
            valor_total += ITENS[i][0]
            peso_total += ITENS[i][1]
    if peso_total > CAPACIDADE:
        return 0
    return valor_total

def selecao(populacao):
    melhores = random.sample(populacao, TORNEIO_TAM)
    return max(melhores, key=fitness)

def cruzamento(pai1, pai2):
    ponto = random.randint(1, NUM_ITENS - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutacao(individuo):
    for i in range(NUM_ITENS):
        if random.random() < TAXA_MUTACAO:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico():
    populacao = [gerar_individuo() for _ in range(POPULACAO_TAM)]
    melhor_individuo = None
    melhor_fitness = 0

    for geracao in range(GERACOES):
        nova_populacao = []

        while len(nova_populacao) < POPULACAO_TAM:
            pai1 = selecao(populacao)
            pai2 = selecao(populacao)
            filho1, filho2 = cruzamento(pai1, pai2)
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao[:POPULACAO_TAM]

        melhor_na_geracao = max(populacao, key=fitness)
        f = fitness(melhor_na_geracao)
        if f > melhor_fitness:
            melhor_fitness = f
            melhor_individuo = melhor_na_geracao

        print(f"Geração {geracao + 1}: Melhor valor = {melhor_fitness}")

    print("\nMelhor solução encontrada:")
    print(f"Itens selecionados: {melhor_individuo}")
    print(f"Valor total: {melhor_fitness}")
    print(f"Peso total: {sum(ITENS[i][1] for i in range(NUM_ITENS) if melhor_individuo[i] == 1)}")

if __name__ == "__main__":
    algoritmo_genetico()
