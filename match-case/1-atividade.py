import os

lista_produtos = []
produtao = []

while True:
    os.system("CLS")

    print('''
===== Mercadinho senai=====
1 - cadastra produto
2 - lista de todos os produtos
3 - atualizar produto
4 - remover produto
5 - buscar produto
0 - sair''')

    opcao = int(input("Escolha uma opição"))
    match opcao:
        case 1:
                #create (inserir)
                print("==== cadastra produto ===")
                nome_produto = input("Digite o nome do produto: ").strip().upper()
                produtinho = input("digite seu produto").strip().upper()
                if nome_produto == " ":
                    print("o nome do produto deve ser inserido.")
                elif nome_produto in lista_produtos:
                    print("produto já cadastrado")
                else:
                    lista_produtos.append(nome_produto)
                    produtao.append(produtinho)
        case 2:
            # read(Ler/buscar)
            print("=== produto no estoque ===")
            if len(lista_produtos) == 0:
                print('\n estoque vazio.')
            for produto in lista_produtos:
                print(f'- {produto}')

        case 3:
            #atualizar(update)
            print("=== ATUALIZAR PRODUTO ====")
            nome = input("Qual produto deseja atualizar?")
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input("Novo nome: ")
                lista_produtos[posicao] = novo
                print("Produto alterado com sucesso")
            else:
                print("Produto não encontrado")

        case 4:
            #remove/delete (remover)
            print("\n=== Remover Produto ====")
            nome = input("Qual produto deseja Remover?")
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print("Produto removido com sucesso")
            else:
                print("Produto não encontrado")

        case 5:
            #Read (Ler / Consultar / Buscar)
            print("\n ==== ENCONTRAR PRODUTO ==")
            nome = input("Qualç produto deseja buscar?")
            if nome in lista_produtos:
                print("Produto encontrado!")
            else:
                print("Este protudo não estã no estoque")
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida! \n tente novamente...")
    input("Pressione uma tecla para continuar...")