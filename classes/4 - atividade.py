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

for i in range (QUANTIDADE_CLIENTES):
    novo_cliente =Clientes(
        nome = input("Digite o seu nome: "),
        email = input("Digite o seu E-mail: "),
        telefone = input("Digite o seu telefone: "),
        endereco = input("Digite o seu endereço: ")
        )
    lista_clientes.append(novo_cliente)

    arquivo = "fornecedor.csv"
    with open(arquivo, 'a') as arquivo_cliente:
        for cliente in lista_clientes:
            arquivo_cliente.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}\n")
    print("Cliente salvo com sucesso!\n ")