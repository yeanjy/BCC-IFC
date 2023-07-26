matrícula = int(input("Digite o número da matrícula:"))
ano = matrícula//10000
semestre = (matrícula%10000)//1000

print (f"O ano da matrícula é {ano:02d}")
print (f"O semestre da matrícula é {semestre:02d}")
