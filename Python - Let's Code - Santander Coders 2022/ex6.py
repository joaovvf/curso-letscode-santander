numeros = list()
numero = 1
while numero != 0:
    numero = int(input('Digite um número(0 para parar): '))
    numeros.append(numero)

print(f"A soma dos números é: {sum(numeros)}")
