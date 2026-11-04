import os


elenco = []

while True:
    os.system("cls")
    print('''
===== Jogadores NBSENAI ====
1 - Cadastra jogador
2 - Lista de Jogador
3 - Atualizar jogador
4 - Excluir jogador
0 - Sair''')
    opcao = int(input("Qual opção você deseja? "))

    match opcao:
        case "1":
            print("\n---- CADASTRAR ----")
            nome = input("Nome: ").strip()
            posicao = input("Posição: ").strip()
            camisa = int(input("Camisa: "))
            
            if nome == "" or posicao == "":
                print("Erro: Nome e posição não podem ficar em branco.")
            elif camisa <= 0:
                print("Erro: A camisa deve ser maior que zero.")
            else:
                # Verifica se a camisa já está a ser usada
                camisa_em_uso = False
                for jogador in elenco:
                    if jogador["camisa"] == camisa:
                        camisa_em_uso = True
                        break
                
                if camisa_em_uso:
                    print("Erro: Esta camisa já pertence a outro jogador.")
                else:
                    elenco.append({"nome": nome, "posicao": posicao, "camisa": camisa})
                    print("Jogador cadastrado!")

        case "2":
            print("\n---- ELENCO ----")
            if len(elenco) == 0:
                print("O elenco está vazio.")
            else:
                for i in range(len(elenco)):
                    jogador = elenco[i]
                    print(f"{i + 1}. {jogador['nome']} | {jogador['posicao']} | #{jogador['camisa']}")

        case "3":
            print("\n---- ATUALIZAR ----")
            if len(elenco) == 0:
                print("O elenco está vazio.")
            else:
                indice = int(input("Indique o número do jogador na lista: ")) - 1
                
                if 0 <= indice < len(elenco):
                    novo_nome = input("Novo nome: ").strip()
                    nova_posicao = input("Nova posição: ").strip()
                    nova_camisa = int(input("Nova camisa: "))
                    
                    elenco[indice] = {"nome": novo_nome, "posicao": nova_posicao, "camisa": nova_camisa}
                    print("Jogador atualizado com sucesso!")
                else:
                    print("Número inválido.")

        case "4":
            print("\n---- EXCLUIR ----")
            if len(elenco) == 0:
                print("O elenco está vazio.")
            else:
                indice = int(input("Indique o número do jogador na lista para remover: ")) - 1
                
                if 0 <= indice < len(elenco):
                    removido = elenco.pop(indice)
                    print(f"Jogador {removido['nome']} removido!")
                else:
                    print("Número inválido.")

        case "0":
            print("A sair do programa...")
            break
            
        case _:
            print("Opção inválida! Tente novamente.")