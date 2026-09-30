import os
os.system("cls")

while True:
    numero = int(input('Digite um número ente 1 e 10: '))
    if numero < 1 or numero > 10:
        print() #pular uma linha
        print('número inválido, tente novamente')
    else:
        print() #assim como o \n
        print('O Número está entre 1 e 10')
        #serve para parar o laço de repetição
        break

print(' === FIM ===')