n = int(input("Digite um numero inteiro: "))
while n < 2:
    print ("ERRO. Digite um numero maior ou igual a 2")
    n = int(input("Digite um numero inteiro: "))
fator = 2
while fator <= n:
    if n%fator== 0:
        print (fator)
        n//= fator
    else: 
        fator += 1