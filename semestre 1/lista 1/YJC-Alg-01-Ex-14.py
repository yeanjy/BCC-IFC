l1= float (input("Digite o lado 1 do triângulo em metros"))
l2= float (input("Digite o lado 2 do triângulo em metros"))
l3= float (input("Digite o lado 3 do triângulo em metros"))
l = (l1+l2+l3)/2

import math
area = math.pow(l*(l-l1)*(l-l2)*(l-l3), 1/2)
print ("A área do triângulo é", area, "m²")