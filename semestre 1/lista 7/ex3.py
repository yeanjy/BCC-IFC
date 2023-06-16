def buscaREVERSA(dicionario):
    lista = dicionario.keys()
    return lista

dicionario = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo',
    'hobbies': ['leitura', 'fotografia', 'esportes'],
    'cor_favorita': 'azul',
    'animal_estimacao': {
        'nome': 'Max',
        'especie': 'cachorro',
        'idade': 3
    }
}

resposta = buscaREVERSA(dicionario), buscaREVERSA(dicionario['animal_estimacao'])
print(resposta)
