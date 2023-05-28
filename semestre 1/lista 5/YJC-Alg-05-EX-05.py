def numero_ordinal(numero):
    if numero < 1 or numero > 12:
        return ""  

    ordinais = ["primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto",
                "sétimo", "oitavo", "nono", "décimo", "décimo primeiro", "décimo segundo"]

    return ordinais[numero - 1]  

escolha = int(input("Digite um numero de 1 a 12: "))
if escolha in range(1, 13):
    resultado = numero_ordinal(escolha)
    print(f"{escolha} -> {resultado}")
else:
    print("Numero invalido")
