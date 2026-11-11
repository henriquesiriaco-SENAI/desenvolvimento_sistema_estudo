import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Produto:
    nome: str
    preco: float

lista_produtos = []

def solicitar_dados():
    for i in range(3):
        produto = Produto(
        nome = input("Digite o nome do produto"),
        preco = float(input("Digite o preço"))
        )
        lista_produtos.append(produto)


def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f'f{i + 1} - {lista_produtos[i]}')


print("= solicitando dados =")
solicitar_dados()

print("\n exibindo dados")
mostrar_dados(lista_produtos)