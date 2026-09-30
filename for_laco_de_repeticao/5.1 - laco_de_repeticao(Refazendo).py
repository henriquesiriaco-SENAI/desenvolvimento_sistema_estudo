import os
import time
os.system('cls')

numero = int(input('Digite 1° número: '))

for i in range(numero, 0 ,-1):
    print(f'Contagem Regressiva ate a detonação {i}')
    time.sleep(1)
print('KABOOOM')