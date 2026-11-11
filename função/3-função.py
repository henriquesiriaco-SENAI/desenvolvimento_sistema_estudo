import os
os.system("cls")

lista_produtos = []

def solicitar_dados():
    for i in range(3):
        produto = input("Digite o nome do produto")
        lista_produtos.append(produto)


def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f'f{i + 1} - {lista_produtos[i]}')


print("= solicitando dados =")
solicitar_dados()

print("\n exibindo dados")
mostrar_dados(lista_produtos)