valor =  float(input("Entrada: "))
if valor >= 0 and valor <= 25:
    print("Saída: [0, 25]")
elif valor > 25 and valor <= 50:
    print("Saída: (25, 50]")
elif valor > 50 and valor <= 75:
    print("Saída: (50, 75]")
elif valor > 75 and valor <= 100:
    print("Saída: (75, 100]")
else:
    print("Fora de intervalo")

