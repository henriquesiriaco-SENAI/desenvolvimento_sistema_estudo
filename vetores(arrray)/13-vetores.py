import os
os.system("cls")

vetor_numero = []
QUANTIDADE_NUMERO = 5

for i in range (QUANTIDADE_NUMERO):
    numero = float(input(f"Digite {i + 1}° Número "))
    if numero < 0:
        numero = 0
    vetor_numero.append(numero)


for M, numero in enumerate (vetor_numero, start=1):
    print(f"{M}° Número: {numero}")