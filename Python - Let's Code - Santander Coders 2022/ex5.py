pontos = 0
perguntas = ["Mora perto da vítima?", "Já trabalhou com a vítima?", "Telefonou para a vítima?", 
"Esteve no local do crime?", "Devia para a vítima?"]
for i in perguntas:
    print(i)
    resposta = str(input("sim ou nao? "))
    if resposta == "sim":
        pontos += 1
    if resposta == "nao":
        pontos += 0
if pontos == 5:
    print("Assassino!")
elif pontos >= 3 and pontos < 5:
    print("Cumplíce!")
elif pontos == 2:
    print("Suspeito.")
else:
    print("Liberado.")
