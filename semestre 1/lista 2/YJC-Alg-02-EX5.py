moeda = int(input("Digite o valor inserido:"))
m50 = moeda//50
m25 = (moeda%50)//25
m10 = ((moeda%50)%25)//10
m5 = (((moeda%50)%25)%10)//5
m1 = (((moeda%50)%25)%10)%5
print (f"O valor recebido será de {m50} de moedas de 50 centavos")
print (f"O valor recebido será de {m25} de moedas de 25 centavos")
print (f"O valor recebido será de {m10} de moedas de 10 centavos")
print (f"O valor recebido será de {m5} de moedas de 5 centavos")
print (f"O valor recebido será de {m1} de moedas de 1 centavo")