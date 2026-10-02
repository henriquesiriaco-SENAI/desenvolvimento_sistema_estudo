import os
os.system('cls')

carro = 150
luva = 20
celular = 2.50
paralelepipedo = 999
hakuna_matata = 6767

while True:
    print('''
====== SENAI SHOP ======
1 - CARRO R$ 150
2 - LUVA R$ 20
3 - CELULAR R$ 2,50
4 - PARALELEPIPEDO R$ 999
5 - hakuna matata R$ 6767''')
    numero = input("Escolha o número do produto: ")
    if numero == "1":
        print(f"Opção escolhida, carro R${carro}")
        break
    elif numero == "2":
        print(f"opção escolhida, Luva R${luva}")
        break
    elif numero == "3":
        print(f"opção escolhida, celular R${celular}")
        break
    elif numero == "4":
        print(f"opção escolhida, paralelepipedo R${paralelepipedo}")
        break
    elif numero == "5":
        print(f"opção escolhida, hakuna matata R${hakuna_matata}")
        break
    else:
        print(f"Não vendemos esse produto")
        print("tente novamente")
        input("Pressione para continuar..")
        os.system("cls")
