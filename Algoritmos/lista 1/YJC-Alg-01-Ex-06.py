Suco = float (input("Digite o valor do suco"))
Prato_principal = float (input("Digite o valor do prato principal"))
Sobremesa = float (input("Digite o valor da sobremesa"))
Valor_total = (Suco + Prato_principal + Sobremesa) + (Suco + Prato_principal + Sobremesa)*0.1
print ("O valor total da sua conta é R$ 10 {:.2f}".format(Valor_total))