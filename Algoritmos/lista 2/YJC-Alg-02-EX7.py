n = int(input("Digite um número inteiro de 3 algarismo:"))
c = n//100
d = (n%100)//10
u = ((n%100)%10)

print (f"A centana do número é {c}")
print (f"A dezena do número é {d}")
print (f"A unidade do número é {u}")