def diames(mes, ano):
    if mes < 1 or mes > 12:
        return ""
    
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return "Possui 31 dias"
    
    if mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            return "Possui 29 dias"
        else:
            return "Possui 28 dias"
    
    return "Possui 30 dias"

mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o ano: "))

resultado = diames(mes, ano)
print(resultado)
