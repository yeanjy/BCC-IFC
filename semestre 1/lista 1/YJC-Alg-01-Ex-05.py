Vasilhames_menor = int (input("Digite a quantidade de vasilhames com menos de 1 litro"))
Vasilhames_maior = int (input("Digite a quantidade de vasilhames com mais de 1 litro"))
Valor_total = float ((Vasilhames_maior*0.25) + (Vasilhames_menor*0.1))
print ("O valor total de reciclado foi de R$ {: .2f}".format(Valor_total))