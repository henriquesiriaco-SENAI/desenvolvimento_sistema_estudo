from dataclasses import dataclass
import os
os.system("CLS")

@dataclass
class Clientes:
    nome : str
    idade: int
    altura : float

QUANTIDADE_CLIENTES = 2

lista_cliente = []

for i in range(QUANTIDADE_CLIENTES):
    novo_cliente = Clientes(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite a sua idade:")),
        altura = float(input("Digite sua Altura: "))
    )
    lista_cliente.append(novo_cliente)

    arquivo = "dados_client.csv"
    with open(arquivo, 'a') as arquivo_cliente:
        for cliente in lista_cliente:
            arquivo_cliente.write(f'{cliente.nome}, {cliente.idade}, {cliente.altura}\n')

    print("Cliente salvo com sucesso! \n")