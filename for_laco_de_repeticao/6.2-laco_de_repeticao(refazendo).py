import os
os.system

soma = 0

print("ACUMULANDO VARIAVEL")

for i in range(3):
    soma += int(input('Digite um número para somar: '))

print(f'o valor final da variavel soma: {soma}')