n = int (input("Digite um número inteiro de 4 digitos:"))
m = n//1000
c = (n%1000)//100
d = ((n%1000)%100)//10
u = ((n%1000)%100)%10
soma = m + c + d + u
print (f"A soma é de {soma}")
