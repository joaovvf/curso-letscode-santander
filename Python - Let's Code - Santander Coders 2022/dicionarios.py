# criando dicionario

dicionario = {}
dicionario = {}
dicionario = { 'nome': 'João', 'idade': 21, 'altura': 1.70 }
print(dicionario) 
print(dicionario['idade'])

# adicionando elementos em um dicionario

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2
print(dicionario)

# iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

#testando a existencia de uma chave

print('peso' in dicionario)
print('altura' in dicionario)

