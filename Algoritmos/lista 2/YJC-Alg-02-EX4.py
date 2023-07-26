n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))
menor = min(n1, n2, n3)
maior = max(n1, n2, n3)
meio  = n1+n2+n3-menor-maior
print (menor, meio, maior)