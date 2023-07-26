s = int(input("Digite o número de tempo em segundos:"))
d = s//86400
h = (s%86400//3600)
m = ((s%86400)%3600)//60
s = (((s%86400)%3600)%60)
print (f"O tempo convertido é {d:02d}:{h:02d}:{m:02d}:{s:02d}")