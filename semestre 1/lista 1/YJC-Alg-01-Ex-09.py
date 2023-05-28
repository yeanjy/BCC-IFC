valor = float (input("Digite o valor do investimento inicial"))
juros1 = float (valor*(1.12)**1)
juros2 = float (valor*(1.12)**2)
juros3 = float (valor*(1.12)**3)

print ("O valor após 1 ano seria de {:.2f}".format(juros1))
print ("O valor após 2 anos seria de {:.2f}".format(juros2))
print ("O valor após 3 anos seria de {:.2f}".format(juros3))