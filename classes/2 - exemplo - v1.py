from dataclasses import dataclass
import os
os.system("cls")

#CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE
#DADOS: NOME,TELEFONE E EMAIL

@dataclass
class Cliente:
    nome : str
    telefone : str
    email : str

lista_cliente = []


dados_cliente = Cliente(
        nome = input("Digite o nome do cliente: "),
        telefone = int(input("Digite o número do Cliente:")),
        email = input("Digite o email do cliente: ")
    )
lista_cliente.append(dados_cliente)

print("\n === EXIBINDO DADOS ===")
for client in lista_cliente:
    print(f"Nome: {client.nome}")
    print(f"Telefone: {client.telefone}")
    print(f"Email: {client.email}")
    print("="* 15)