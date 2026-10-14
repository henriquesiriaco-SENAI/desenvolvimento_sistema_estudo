import os
os.system("cls")

import os
os.system("cls")

pares = 0
impares = 0

print("= INSERINDO NÚMEROS NO VETOR =")
vetor_notas = []
QUANTIDADE_NOTAS = 6

for i in range(QUANTIDADE_NOTAS):
    nota = int(input(f"Sua {i + 1}°  notas: "))
    vetor_notas.append(nota)
    if nota % 2 == 0:
        pares += 1
    else:
        impares += 1

print ("\n= EXIBINDO NOTAS DO VETOR =")
for notinhasbonitinhas, nota in enumerate (vetor_notas,start=1): #forEach
    print(f"{notinhasbonitinhas}°: {nota}")



print(f'\n Quantidade de pares: {pares}')
print(f'\n Quanntidade de impares: {impares}')


