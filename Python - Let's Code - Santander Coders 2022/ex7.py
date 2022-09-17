import math

x_1 = int(input("X do primeiro ponto: "))
y_1 = int(input("Y do primeiro ponto: "))
x_2 = int(input("X do segundo ponto: "))
y_2 = int(input("Y do segundo ponto: "))

distancia = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
print(f"A distância entre os pontos X({x_1}, {y_1}) e Y({x_2}, {y_2}) é: {distancia}")