import random

contador = 1
numeros = []
while contador <= 10:
    numeros += [random.randrange(1, 10)]
    contador += 1

print(f"A lista de números geradas é {numeros}")
print(f"1. Os primeiros 4 números: ", end='')
for i in range(0, 4):
    print(numeros[i], end=' ')
print("\n")
print(f"2. Os últimos 5 números: ", end='')
for i in range(len(numeros) - 5, len(numeros)):
    print(numeros[i], end=' ')
print("\n")
print(f"3. Os números nas posições pares: ", end='')
for i in range(0, len(numeros), 2):
    print(numeros[i], end=' ')
print("\n")
print(f"4. Os números nas posições ímpares: ", end='')
for i in range(1, len(numeros), 2):
    print(numeros[i], end=' ')
print("\n")
numeros.sort(reverse=True)
print(f"5. A lista de números inversa: {numeros}\n")
print(f"6. Os 5 primeiros números: ", end='')
for i in range(0, 5):
    print(numeros[i], end=' ')
print("\n")
print(f"7. Os 5 últimos números: ", end='')
for i in range(len(numeros) - 5, len(numeros)):
    print(numeros[i], end=' ')




