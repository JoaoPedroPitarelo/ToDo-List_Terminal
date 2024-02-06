from databasemanager import GerenciadorBD
from colors import *

db_manager = GerenciadorBD()


def criar_nova_categoria():
    print(GREEN, NEGRITO, "\nCriação de Categoria", RESET)
    while True:

        print("\nDigite o nome da categoria")
        entrada_categoria = input("Nome: ").strip()

        if not entrada_categoria:
            print(RED, NEGRITO, "\nA categoria precisa ter um nome!", RESET)
            continue

        if len(entrada_categoria) > 26:
            print("O nome não pode passar de 26 caracteres")
            continue

        flag = False
        for categoria in db_manager.lista_categorias():
            if entrada_categoria == categoria[0]:
                print("Está categoria já existe")
                flag = True
                pause = input("\nPressione ENTER para continuar...")

        if flag:
            break

        db_manager.criar_categoria(entrada_categoria)
        break


def excluir_categoria():
    print(RED, NEGRITO, "\nEXCLUSÃO DE CATEGORIA", RESET)
    print(RED, NEGRITO, "\n ATENÇÃO:", RESET,
          'Ao excluir uma categoria todas as tarefas com ela serão EXCLUÍDAS também!', RESET)

    print("\nDeseja continuar? [S/N]")

    while True:
        confimacao = input("\nResposta: ").strip().upper()

        if confimacao in ['S', 'N']:
            if confimacao == 'N':
                opcao_categoria()

            break

        else:
            print(RED, NEGRITO, '\nResposta invalida!', RESET)

    while True:

        if not db_manager.lista_categorias():
            print(RED, NEGRITO, "Não há categorias criadas!", RESET)
            pause = input("\nPressione ENTER para continuar...")
            break

        print("\nDigite o nome da categoria a ser excluida")
        entrada_categoria = input("Nome da categoria: ")

        flag = False
        for categoria in db_manager.lista_categorias():
            if entrada_categoria == categoria[0]:
                db_manager.excluir_categoria(entrada_categoria)
                print(f"{entrada_categoria} excluída!")
                pause = input("\nPressione ENTER para continuar...")
                flag = True
                break

        if flag is True:
            break

        print(RED, NEGRITO, '\nCategoria não achada!', RESET)


def opcao_categoria():

    lista_formatada = ''
    for i in db_manager.lista_categorias():
        lista_formatada += "" + i[0] + "  "

    print(
        '_' * 26,
        '\n\nCategorias: ',
        GREEN, NEGRITO, '[ ',
        WHITE, lista_formatada,
        GREEN, ']', RESET
    )

    # Criar ou excluir uma categoria
    print('\n Deseja criar ou excluir uma categoria?\n',
          '[E]xcluir    [C]riar nova\n'
          ' [S]air')

    while True:
        entrada_opcao = input('\nEscolha: ').upper().strip()

        if entrada_opcao in ['E', 'C', 'S']:
            break
        else:
            print(RED, NEGRITO, '\nEscolha inválida', RESET)

    if entrada_opcao == 'C':
        criar_nova_categoria()
    elif entrada_opcao == 'S':
        return
    else:
        excluir_categoria()
