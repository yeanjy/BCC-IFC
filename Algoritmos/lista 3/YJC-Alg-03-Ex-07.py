som = int(input("Digite um nível de volume em dB:"))

if som == 40:
    print("Sala silenciosa")
elif som > 40 and som < 70:
    print("Entre sala silenciosa e despertador")
elif som == 70:
    print("Despertador")
elif som >70 and som < 106:
    print("Entre despertador e cortador de grama")
elif som == 106:
    print("Cortador de grama")
elif som > 106 and som < 130:
    print("Entre cortador de grama e britadeira")
elif som == 130:
    print("Britadeira")
elif som < 40 :
    print("Menor que uma sala silenciosa")
else:
    print("Maior que uma britadeira")