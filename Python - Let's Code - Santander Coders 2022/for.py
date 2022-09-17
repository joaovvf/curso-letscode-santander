
"""#DE 0 A 9
for i in range(10):
    print(i)

print("#" * 10)
#DE 1 A 5
for i in range(1, 6):
    print(i)
print("#" * 10)

#DE 0 A 10 DE 2 EM 2
for i in range(0, 11, 2):
    print(i)
print("#" * 10)"""

from xml.dom.minidom import Notation


soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a nota do aluno{i} '))

    soma = soma + nota 

print(soma / 3)
