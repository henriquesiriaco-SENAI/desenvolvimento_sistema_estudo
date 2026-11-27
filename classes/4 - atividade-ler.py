from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Clientes:
    nome : str
    email : str
    telefone : str
    endereco : str

QUANTIDADE_CLIENTES = 2

lista_clientes = []

arquivo = "fornecedor.csv"
with open(arquivo, 'r') as arquivo_cliente:
    for linha in arquivo_cliente:
        nome, email, telefone , endereco = linha.strip().split(",")
        lista_clientes.append(Clientes(
            nome = nome,
            email = email,
            telefone = telefone,
            endereco = endereco
        ))

for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Email: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Endereço: {cliente.endereco}")
    print("="*15)
