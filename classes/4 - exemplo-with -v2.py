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

arquivo = "dados_client.csv"
with open(arquivo, 'r') as arquivo_clientes:
    for linha in arquivo_clientes:
        nome, idade, altura = linha.strip().split(',')
        lista_cliente.append(Clientes(
            nome=nome,
            idade=int(idade),
            altura=float(altura)
        ))

print("Cliente salvo com sucesso! \n")
for cliente in lista_cliente:
    print(f"nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Altura: {cliente.altura}")
    print("="*15)