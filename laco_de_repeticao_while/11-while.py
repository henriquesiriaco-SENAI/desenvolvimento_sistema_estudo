import os

while True:
    os.system("cls")
    print('''
==== MENU ====
1 - Adicionar pessoa
2 - Exibir resultado
3 - Sair
''')
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            print("== CADASTRO ==")
            idade = int(input("Digite a sua idade: "))
            sexo = input("Digite o sexo (M/F): ").upper()
            salario = float (input("Digite o salário R$: "))

            soma_salario += salario
            contador_pessoas += 1
            maior_idade = max(idade , maior_idade)
            menor_idade = min(idade , menor_idade)

            if sexo == "F" and salario >= 5000:
                mulheres_5k += 1

                print("pessoa adicionada com sucesso!")
                input("pressione uma tecla para continuar...")
        case 2:
            if contador_pessoas == 0:
                print("\n nenhuma pessoa cadastrada \n")
            else:
                media_salario = soma_salario / contador_pessoas
                
                print("|n ======= RESULTADO DA PESQUISA =======")
                print(f"media de salário do grupo {media_salario}")
                print(f"Maior idade: {maior_idade}")
                print(f"menor idade: {menor_idade} ")
                print(f"Mulhes com salario a partir de R$ 5.000,00 {mulheres_5k}")
                input("pressione para continuar...")
        case 3:
            print("programa encerrado")
            break
        case _:
            print("opção invalida \n")
            input("pressione para continuar")