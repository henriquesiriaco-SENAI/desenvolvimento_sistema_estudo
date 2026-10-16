import os
os.system("cls")

vetor_numero = []
QUANTIDADE_NUMERTOS = 5
negativos = 0
soma = 0


for i in range(QUANTIDADE_NUMERTOS):
    numero = float(input(f"Digite {i + 1}° Número:  "))
    vetor_numero.append(numero)
    if numero > 0:
        soma += numero
    elif numero < 0:
        negativos += 1


print("===== exibindo valores =====")
print(f"Quantidade de numeros negativos: {negativos}")
print(f"Soma dos positivos: {soma}")

