import os
os.system("cls")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        notas = int(input(f"Digite sua nota {i+1}° entre 0 e 10: "))
        if notas < 0 or notas > 10:
            print("Números errados \n tente novamente! \n ")
            input("pressione para continutar...")
            os.system("cls")
        elif notas >= 0 or notas <= 10:
            soma += notas
            break

media = soma / QUANTIDADE_NOTAS
if media >= 7:
    print(f"Aprovado, sua media: {media}")
elif media > 5 or media < 6.9:
    print(f"Recuperação, sua media: {media}")
elif media <= 5:
    print(f"Reprovado, sua media: {media}")



