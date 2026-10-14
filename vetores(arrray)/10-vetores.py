import os
os.system("cls")




print("= INSERINDO NÚMEROS NO VETOR =")
vetor_numeros = []
QUANTIDADE_NOTAS = 5

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Sua {i + 1}°  notas: "))
    vetor_numeros.append(nota)

menor_nota = min(vetor_numeros)
maior_nota = max(vetor_numeros)


print ("\n= EXIBINDO NOTAS DO VETOR =")
for notinhasbonitinhas, nota in enumerate (vetor_numeros,start=1): #forEach
    print(f"{notinhasbonitinhas}°: {nota}")


print(f"\n Menor Número {menor_nota}")
print(f"\n Maior número {maior_nota}")