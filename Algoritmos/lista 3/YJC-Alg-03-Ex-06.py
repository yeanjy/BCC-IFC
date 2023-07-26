l1 = float(input("Digite o lado 1 do triângulo"))
l2 = float(input("Digite o lado 2 do triângulo"))
l3 = float(input("Digite o lado 3 do triângulo"))

if l1 != l2 != l3:
    print("É um triângulo escaleno")
elif l1==l2==l3:
    print("É um triângulo equilátero")
else:
    print("É um triângulo isóceles")