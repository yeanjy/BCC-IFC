def MDC(a, b):
    if b == 0:
        return a
    else:
        c = a%b
        return MDC(b,c)
    
valor=int(input("Digite:"))
valor2=int(input("Digite:"))
print(MDC(valor,valor2))