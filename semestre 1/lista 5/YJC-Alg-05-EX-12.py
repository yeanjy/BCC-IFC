def verificarsenha(senha):
    if len(senha)<8:
        return False
    if not any(x.isupper() for x in senha):
        return False
    if not any(x.islower() for x in senha):
        return False
    
    return True

intsenha = input("Digite a sua senha: ")
vsenha = verificarsenha(intsenha)
print (vsenha)