idade = int(input("Digite a idade do seu cachorro:"))
while idade < 0:
    print ("Digite um número positivo")
    idade = int(input("Digite a idade do seu cachorro:"))

if idade <= 2:
    idade2 = idade*10.5
else:
    idade2 = 10.5*2 + (idade-2)*4

print (f"A idade do cachorro convertidade em idade humana é {idade2}")