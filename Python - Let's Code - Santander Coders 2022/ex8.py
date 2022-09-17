import math

contador = 1
soma = 0 
while contador <= 1000:
    termos = 1/(math.factorial(contador))
    soma += termos
    contador += 1

print(soma)