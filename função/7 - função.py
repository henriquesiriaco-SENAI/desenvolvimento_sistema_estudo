import os
os.system("cls")

notas_armazenadas =[]
QUANTIDADE_NOTAS = 3


def calcular_notas(notas_armazenadas):
    return sum(notas_armazenadas) / len(notas_armazenadas)

def mostrar_resultado(media,notas_armazenadas):
    print("\n === Exiibindo Resultado ===")
    for nota in notas_armazenadas:
        print(f"Nota:{nota}")
    print(f"\nMédia: {media}")

for i in range(QUANTIDADE_NOTAS):
        nota = float(input(f"Digite a sua {i + 1} Nota: "))
        notas_armazenadas.append(nota)

media = calcular_notas(notas_armazenadas)

mostrar_resultado(media, notas_armazenadas)
