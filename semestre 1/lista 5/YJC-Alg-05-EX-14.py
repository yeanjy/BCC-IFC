def datamagica(dia, mes, ano):
    if mes < 1 or mes > 12:
        return ""
    
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia > 31:
            return False
    
    if mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    
    if mes in [4, 6, 9, 11]:
        if dia > 30:
            return False
    
    doisultimosdigitos = ano%100
    magicdata = dia*mes
    if magicdata == doisultimosdigitos:
        return True
    else:
        return False

dia = int(input("Digite o número do dia: "))   
mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o ano: "))

resultado = datamagica(dia, mes, ano)
print(resultado)

def main():
    for ano in range(1900, 2000):
        for mes in range(1, 13):
            for dia in range(1, 32):
                if datamagica(dia, mes, ano):
                    print(f"{dia}/{mes}/{ano}") 
main()