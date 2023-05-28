preços = [4.95, 9.95, 14.95, 19.95, 24.95]
desconto = 0.4

print ("Preço original\tPreço com desconto")

for preços in preços:
    preçod = preços*desconto
    print (f"R$ {preços:.2f}".ljust(20), f"R$ {preçod:.2f}")
