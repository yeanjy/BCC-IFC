def main ():
    cat1 = float(input("Digite o cateto 1 do traingulo:"))
    cat2 = float(input("Digite o cateto 2 do triangulo"))
    return (cat1**2 + cat2**2)

def pitagoras():
    hip = main()**0.5
    return hip

print ("A hipotenusa é", pitagoras())