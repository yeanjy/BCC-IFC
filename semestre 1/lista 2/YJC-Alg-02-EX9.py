data = int(input("Insira uma data:"))
d = data//10000
m = (data%10000)//100
a = data%100

print (f"A data inversa é {a:02d}{m:02d}{d:02d}")