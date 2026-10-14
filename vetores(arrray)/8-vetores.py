import os
os.system("cls")

import os
os.system("cls")



print("= INSERINDO NÚMEROS NO VETOR =")
vetor_notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Sua {i + 1}°  notas: "))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADE_NOTAS


print ("\n= EXIBINDO NOTAS DO VETOR =")
for notinhasbonitinhas, nota in enumerate (vetor_notas,start=1): #forEach
    print(f"{notinhasbonitinhas}°: {nota}")

if media >= 7:
    print(f"\n Aprovado, media: {media}")
elif media >= 5:
    print(f"\n Recuperação, media: {media}")
elif media <= 5:
    print (f"\n Recuperação, media:   {media}")
else:
    print("\n opção invalida, tente novamente")
