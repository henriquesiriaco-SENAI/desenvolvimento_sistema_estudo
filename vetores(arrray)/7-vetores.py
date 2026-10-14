import os
os.system("cls")



print("= INSERINDO NÚMEROS NO VETOR =")
vetor_notas = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Sua {i + 1}°  notas: "))
    vetor_notas.append(nota)

soma = sum(vetor_notas)
media = soma / QUANTIDADE_NOTAS

print ("\n= EXIBINDO NOTAS DO VETOR =")
for notinhasbonitinhas, nota in enumerate (vetor_notas,start=1): #forEach
    print(f"{notinhasbonitinhas}°: {nota}")

print(f"Soma: {soma}")
print(f"Méida: {media}")