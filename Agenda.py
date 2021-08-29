# Este programa possui funções do Python 3.10
# Poderá não funcionar em versões anteriores do Python
# Nenhum arquivo externo será gerado durante a execução deste programa

info_contato = {}


def menu_programa():  # Menu inicial do programa
    print('*='*30)
    print('Digite uma das Opções a seguir:')
    print('1: Inserir novo cadastro')
    print('2: Consultar nome cadastrado')
    print('3: Remover cadastro')
    print('4: Alterar cadastro')
    print('5: Cadastros salvos')
    print('6: Gerar relatório')
    print('*='*30)
    escolha = int(input('Digite o número correspondente a função desejada: '))
    # Função match/case funciona da mesma forma que switch/case de outras linguagens
    # Disponível somente a partir do Python 3.10
    match escolha:
        case 1:
            inserirNovoCadastro()
        case 2:
            consultarCadastro()
        case 3:
            removerCadastro()
        case 4:
            alterarCadastro()
        case 5:
            listaCadastro()
        case 6:
            listagem_usuarios()
        case _:
            return 0


def inserirNovoCadastro():  # Este bloco de função permite a inserção de 2 ou mais cadastros
    qt_cadastro = int(input('Informe a quantidade de cadastros que serão efetuados: '))
    while qt_cadastro <= 1:
        print('Valor inválido, insira um valor igual ou maior a 2.')
        qt_cadastro = int(input('Informe a quantidade de cadastros que serão efetuados: '))
    for numero_i in range(qt_cadastro):
        nome = input('Informe o nome do usuário: ')
        telefone = input('Informe o número de telefone: ')
        email = input('Informe o e-mail: ')
        twitter = input('Informe o nome de usuário Twitter: ')
        instagram = input('Informe o nome de usuário do Instagram: ')
        info_contato[nome] = [telefone, email, twitter, instagram]
        print('Cadastro Efetuado!')
        numero_i += 1
    menu_programa()


def consultarCadastro():  # Este bloco de função efetua a consulta de cadastros efetuados no bloco acima
    nome = input('Informe o nome do usuário cujo o cadastro será consultado: ')
    if nome in info_contato:
        print(info_contato.get(nome))
        opcao = str(input('Gostaria de efetuar uma nova consulta?[S/N]: ')).upper()[0]
        if opcao == 'S':
            consultarCadastro()
        elif opcao == 'N':
            menu_programa()
        else:
            print("Opção incorreta. Digite somente 'S' ou 'N'.")
            consultarCadastro()
    else:
        print('Usuário não encontrado.')
        menu_programa()
    menu_programa()


def removerCadastro():  # Os cadastros poderão ser removidos utilizando este bloco de função
    nome = input('Informe o nome cujo o cadastro será excluído: ')
    if nome in info_contato.keys():
        opcao = str(input('Confirma a exclusão do cadastro deste usuário? [S/N]: ')).upper()[0]
        if opcao == 'S':
            info_contato.pop(nome)
            print(nome + ' excluído')
            nova_opcao = str(input('Gostaria de excluir outro cadastro? [S/N]: ')).upper()[0]
            if nova_opcao == 'S':
                removerCadastro()
            else:
                menu_programa()
        elif opcao == 'N':
            print('Eliminação de cadastro cancelada.')
            menu_programa()
        else:
            print("Opção incorreta. Digitem somente 'S' ou 'N'.")
            removerCadastro()
    else:
        print('Nome de usuário não encontrado. Tentar novamente? [S/N]: ')
        opcao = str(input()).upper()[0]
        if opcao == 'S':
            removerCadastro()
        elif opcao == 'N':
            menu_programa()
        else:
            print("Opção incorreta. Digitem somente 'S' ou 'N'.")
            removerCadastro()


def alterarCadastro():  # Este bloco de função permite a alteração de cadastros existentes dentro do dicionário
    nome = input('Informe o Nome constante no cadastro: ')
    if nome in info_contato.keys():
        print('Informe o dado a ser alterado:')
        print('1 - para alterar o telefone.')
        print('2 - para alterar o e-mail.')
        print('3 - para alterar o nome do usuário do Twitter.')
        print('4 - para alterar o nome do usuário do Instagram.')
        print('5 - Cancelar')
        alterar_dado = int(input('Digite o número desejado: '))
        match alterar_dado:
            case 1:
                print('Número de telefone cadastrado atualmente para o usuário:')
                print(info_contato[nome][0])
                telefone = input('Informe o novo número de telefone: ')
                info_contato[nome][0] = telefone
                print('Telefone alterado: {} {}'.format(nome, info_contato[nome][0]))
            case 2:
                print('E-mail cadastrado atualmente para o usuário:')
                print(info_contato[nome][1])
                email = input('Informe o novo e-mail: ')
                info_contato[nome][1] = email
                print('E-mail alterado: {} {}'.format(nome, info_contato[nome][1]))
            case 3:
                print('Usuário Twitter cadastrado atualmente:')
                print(info_contato[nome][2])
                twitter = input('Informe o novo usuário Twitter: ')
                info_contato[nome][2] = twitter
                print('Usuário Twitter alterado: {} {}'.format(nome, info_contato[nome][2]))
            case 4:
                print('Usuário Instagram cadastrado atualmente:')
                print(info_contato[nome][3])
                instagram = input('Informe o novo usuário Twitter: ')
                info_contato[nome][3] = instagram
                print('Usuário Instagram alterado: {} {}'.format(nome, info_contato[nome][3]))
            case 5:
                menu_programa()
        opcao = str(input('Alterar outro dado? [S/N]: ')).upper()[0]
        if opcao == 'S':
            alterarCadastro()
        elif opcao == 'N':
            menu_programa()
        else:
            print("Opção incorreta. Digitem somente 'S' ou 'N'.")
            alterarCadastro()


def listaCadastro():  # Este bloco de função mostra todos os elementos dos cadastros separados por ','
    print('Cadastros salvos:')
    print("Nome, Telefone, Email, Twitter, Instagram")
    for cadastro in info_contato.keys():
        print("{}, {}, {}, {}, {}".format(cadastro, info_contato[cadastro][0], info_contato[cadastro][1],
                                          info_contato[cadastro][2], info_contato[cadastro][3]))
    menu_programa()


def listagem_usuarios():  # Gerar o relatório
    print("Nome \t\t Telefone \t Email \t\t Twitter \t Instagram")
    for cadastro in info_contato.keys():
        print("{} \t\t {} \t {} \t {} \t {}".format(cadastro, info_contato[cadastro][0], info_contato[cadastro][1],
                                                    info_contato[cadastro][2], info_contato[cadastro][3]))
    menu_programa()


menu_programa()
