import os
os.system('cls')

# inicia a variável soma com zero.
# para evitar dar erro quando acumular os valores
# na variavel soma
soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite {i + 1}°, ente 0 e 10: '))
        if nota >= 0 and nota <= 10:
            soma += nota
            break
        else:
            print()
            print('Númnero errado, tente novamente!')

media = soma / QUANTIDADE_NOTAS

print(f'Média: {media}')
print('=== fim ===')