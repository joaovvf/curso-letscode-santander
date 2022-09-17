# criar função

def saudacao():
    print('Seja bem vindo(a)!')
    print('Olá, é um prazer te conhecer!')

saudacao()


#funcao com parametetros

def saudacao(nome, curso):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso {curso}!')

saudacao('João', 'Santander')

#funcao com parametros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso {curso}!')

saudacao('João')

# funcao com retorno

def soma(num1, num2):
    return num1 + num2

print('Resulta da soma é: ', soma(10,2))


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

print(calculadora(4, 3, '-'))