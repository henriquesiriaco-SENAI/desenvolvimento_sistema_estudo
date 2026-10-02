import os
import time
os.system('cls')

contador = 0

while True:
    time.sleep(0.1)
    print('oi')
    print('SENAI')
    print(f'número: {contador}')
    print("...")
    contador += 1
    if contador == 100:
        break