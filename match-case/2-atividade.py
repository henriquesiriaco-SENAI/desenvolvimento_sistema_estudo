import os
lista_nomes = []
lista_sobrenome = []



while True:
    os.system("CLS")

    print('''
==== CLINICA AURUDINHA ====
1 - Cadastro do paciente
2 - Lista Paciente
3 - Atualizar Paciente
0 - sair''')

    opcao = int(input("Deseja qual opção?: "))

    match opcao:
        case 1:
            nome = input("Escreva o nome do paciente: ").strip().upper()
            sobrenome = input("Escreve o sobrenome do paciente: ").strip().upper()
            if nome == "" or sobrenome == "":
                print("Por favor, insira o nome do paciente corretamente!")
            elif nome in lista_nomes:
                print("Paciente cadastrado com sucesso! nome")
            elif sobrenome in lista_sobrenome:
                print("Paciente cadastrado com sucesso! sobrenome")
            else:
                lista_nomes.append(nome)
                lista_sobrenome.append(sobrenome)
            
        case 2:
            print("\n==== PACIENTES REGISTRADOS ====")
            if len(lista_nomes) == 0:
                print("Nenhum paciente registrado")
            else:
                for i in range(len(lista_nomes)):
                    print(f"{i + 1}. Nome: {lista_nomes[i]} | Sobrenome: {lista_sobrenome[i]}")
        case 3:
            ...
        case 0:
            ("==== FIM DO PROGRAMA ===")
            break
        case _:
            print("Ordem invalidá..... \n tente novamente!")
    input("pressione para tentar novamente...")