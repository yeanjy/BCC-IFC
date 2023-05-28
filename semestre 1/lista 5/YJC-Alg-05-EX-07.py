def canudot(a, b, c):
    cmaior = max(a, b, c)
    if cmaior >= a + b + c -cmaior:
        return ("N pode formar um triangulo")
    else :
        return ("Pode formar um triangulo")
    
a = float(input("Digite o comprimento do canudo 1: "))
b = float(input("Digite o comprimento do canudo 2: "))
c = float(input("Digite o comprimento do canudo 3: "))

print (canudot(a,b,c))