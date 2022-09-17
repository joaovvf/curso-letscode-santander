duracao_da_nota = {
    'W': 1,
    'H': 1/2,
    'Q': 1/4,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
}

composicao = '/HH/QQQQ/XXXTXTEQH/W/HW/'
compassos = composicao.strip('/').split('/')

qt_corretos = 0
incorretos = []

for compasso in compassos:
    duracao_compasso = 0
    for nota in compasso:
        duracao_compasso += duracao_da_nota[nota]
    
    if duracao_compasso == 1:
        qt_corretos += 1
    else:
        incorretos.append(compasso)

print(f'Quantidade de compassos corretos: {qt_corretos}')
print(f'Compassos errados: {incorretos}')
