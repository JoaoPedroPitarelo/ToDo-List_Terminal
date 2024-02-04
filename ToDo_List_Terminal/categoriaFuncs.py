from databasemanager import GerenciadorBD
from colors import *

db_manager = GerenciadorBD()


def criar_nova_categoria():
    print(GREEN, NEGRITO, "\nCriação de Categoria", RESET)
    while True:

        print("\nDigite o nome da categoria")
        entrada_categoria = input("Nome: ").strip()

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
    while True:

        if not db_manager.lista_categorias():
            print(RED, NEGRITO, "Não há categorias criadas!", RESET)
            pause = input("\nPressione ENTER para continuar...")
            break

        print("\nDigite o nome da categoria a ser excluida")
        entrada_categoria = input("Nome: ")

        flag = False
        for categoria in db_manager.lista_categorias():
            if entrada_categoria == categoria[0]:
                db_manager.excluir_categoria(entrada_categoria)
                print(f"{entrada_categoria} excluida!")
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
