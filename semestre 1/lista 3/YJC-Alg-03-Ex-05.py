mês = input("Digite o nome do mês:").lower()

if mês == "fevereiro":
    print ("28 ou 29 dias")
elif mês == "janeiro" or mês == "março" or mês == "maio" or mês == "julho" or mês == "agosto" or mês == "outubro" or mês == "dezembro":
    print ("31 dias")
else:
    print ("30 dias")
