"""" ToDo-List Terminal """
# Tentar levantar ele como um serviço, para que possa te enviar notificações

from databasemanager import GerenciadorBD
from categoriafuncs import opcao_categoria
from colors import *
import time
import os

db_manager = GerenciadorBD()


def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')  # Sistemas Linux


def exibir_tarefas():

    if not db_manager.tarefas():
        print(NEGRITO + GREEN + "\n Não há nada para fazer :)" + RESET)
    else:
        print('Suas tarefas: ')

        print("_" * 2, "Geral", "_" * 19)
        for tarefa in db_manager.tarefas():

            if tarefa[6] == 'Geral':

                if tarefa[5] == 3:
                    prioridade = f"{RED}alta{RESET} "

                    print(GREEN + NEGRITO + "  Feita   " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  N Feita " + RESET,
                          NEGRITO, "|",
                          f"ID: {tarefa[0]}",
                          f"| Data: {tarefa[3]}",
                          f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{RESET}")

                elif tarefa[5] == 2:
                    prioridade = f"{YELLOW}média{RESET}"

                    print(GREEN + NEGRITO + "  Feita   " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  N Feita " + RESET,
                          NEGRITO, "|",
                          f"ID: {tarefa[0]}",
                          f"| Data: {tarefa[3]}",
                          f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{RESET}")

                else:
                    prioridade = f"{GREEN}baixa{RESET}"

                    print(GREEN + NEGRITO + "  Feita   " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  N Feita " + RESET,
                          NEGRITO, "|",
                          f"ID: {tarefa[0]}",
                          f"| Data: {tarefa[3]}",
                          f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{RESET}")

        for categoria in db_manager.lista_categorias():
            print("_" * 2, f"{categoria[0]}", "_" * (24 - (len(categoria[0]))))

            for tarefa in db_manager.tarefas():
                if tarefa[6] == categoria[0]:

                    if tarefa[5] == 2:
                        prioridade = f"{RED}alta{RESET} "

                        print(GREEN + NEGRITO + "  Feita   " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  N Feita " + RESET,
                              NEGRITO, "|",
                              f"ID: {tarefa[0]}",
                              f"| Data: {tarefa[3]}",
                              f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{RESET}")

                    elif tarefa[5] == 1:
                        prioridade = f"{YELLOW}média{RESET}"

                        print(GREEN + NEGRITO + "  Feita   " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  N Feita " + RESET,
                              NEGRITO, "|",
                              f"ID: {tarefa[0]}",
                              f"| Data: {tarefa[3]}",
                              f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{RESET}")

                    else:
                        prioridade = f"{GREEN}baixa{RESET}"

                        print(GREEN + NEGRITO + "  Feita   " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  N Feita " + RESET,
                              NEGRITO, "|",
                              f"ID: {tarefa[0]}",
                              f"| Data: {tarefa[3]}",
                              f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{RESET}")


#  Função para a entrada do usuário nas opções
def entrada_opcao():
    print("\nOPÇÕES: ")
    # Opções de entrada do Usuário
    print("     [A]dicionar Tarefa  [R]emover Tarefa  [D]esc tarefas\n"
          "     [N]ão Feita         [F]eita           [C]ategorias\n"
          "     [-R]efresh          [S]air                            ")

    while True:  # Cria um loop que certifica que o usuário não irá passar se não digitar uma das opções válidas
        entrada_usuario = input('\n Escolha: ').upper().strip()

        if entrada_usuario in ["A", "R", "F", "N", "D", "S", "-R", "C"]:
            break
        else:
            print(RED, NEGRITO, "\n Entrada INVALIDA", RESET)

    # Achar uma maneira mais elegante de fazer isso
    if entrada_usuario == "A":
        adicionar_tarefa()
        clear_terminal()
    elif entrada_usuario == "R":
        remover_tarefa()
        clear_terminal()
    elif entrada_usuario == "N":
        alt_nao_feita()
        clear_terminal()
    elif entrada_usuario == "F":
        alt_feita()
        clear_terminal()
    elif entrada_usuario == "D":
        acessar_descricoes()
        clear_terminal()
    elif entrada_usuario == "-R":
        refresh()
    elif entrada_usuario == "C":
        opcao_categoria()
    elif entrada_usuario == "S":
        return entrada_usuario


#   Função Principal(main)
def main():  # Função main

    while True:
        clear_terminal()
        logo()
        exibir_tarefas()

        if entrada_opcao() == "S":
            clear_terminal()
            print("  Saindo...")
            time.sleep(0.4)
            break


#  Funções das opções do algoritmo (adicionar, remover, marcar como feita, sair...)


def refresh():
    palavra = 'refresh'
    for loop in range(0, 3):
        palavra = palavra + '.'
        print(palavra)
        time.sleep(0.2)
    time.sleep(1)


#  Validação de data "mudar para o tipo texto posteriormente"
def validacao_data():
    print('_' * 26)
    while True:
        dia_entrada = input("\n   Dia: ")
        mes_entrada = input("     Mês: ")
        ano_entrada = input("       Ano: ")

        try:
            dia_entrada = int(dia_entrada)
            mes_entrada = int(mes_entrada)
            ano_entrada = int(ano_entrada)

            # Verificação dos dias com seus respectivos meses
            if 0 <= dia_entrada >= 30 and mes_entrada in [2]:
                print(RED, NEGRITO, "\n Data INVALIDA", RESET)
            elif 0 <= dia_entrada >= 31 and mes_entrada in [4, 6, 9, 11]:
                print(RED, NEGRITO, "\n Data INVALIDA", RESET)
            elif 1 <= dia_entrada <= 31 and 1 <= mes_entrada <= 12 and 2000 <= ano_entrada <= 3000:
                break
            else:
                print(RED, NEGRITO, "\n Data INVALIDA", RESET)
        except ValueError:
            print(RED, NEGRITO, "\n Data INVALIDA", RESET)

    return dia_entrada, mes_entrada, ano_entrada


def formatacao_data(dia, mes, ano):

    if dia in range(0, 9) and mes in range(0, 9):
        data_formatada = f"0{dia}/0{mes}/{ano}"
    elif dia in range(0, 9):
        data_formatada = f"0{dia}/{mes}/{ano}"
    elif mes in range(0, 9):
        data_formatada = f"{dia}/0{mes}/{ano}"
    else:
        data_formatada = f"{dia}/{mes}/{ano}"

    return data_formatada


def adicionar_tarefa():
    print('_' * 26)
    print(GREEN, NEGRITO, "\n  Adicionar Tarefa", RESET)

    print(CLARO, '\n "Faça em breves palavras Ex: Tomar café"', RESET)
    while True:
        nova_tarefa = input("   Nome Tarefa: ")

        if not nova_tarefa:
            print(RED, NEGRITO, "\n A tarefa Precisa ter um nome!", RESET)
        else:
            break

    entrada_obsevacao = input("      Desc da tarefa: ")

    print('_' * 26)
    while True:
        print(CLARO, "\n  [1-Baixa 🟢] [2-Média 🟡] [3-Alta 🔴]", RESET)
        prioridade_tarefa = input("   Qual a prioridade da tarefa?: ").strip()

        try:
            prioridade_tarefa = int(prioridade_tarefa)

            if prioridade_tarefa in [1, 2, 3]:
                break
            else:
                print(RED, NEGRITO, "\n Digite entre 1 - 3!")
        except ValueError:
            print(RED, NEGRITO, "\n Entrada inválida ", RESET)

    print('_' * 26)
    while True:

        lista_formatada = ''
        for i in db_manager.lista_categorias():
            lista_formatada += "" + i[0] + "  "

        print(
            '\n    Categorias: ',
            GREEN, NEGRITO, '[ ',
            WHITE, lista_formatada,
            GREEN, ']', RESET
        )

        print(CLARO, "\n  <Enter> = Geral", RESET)
        print("   Qual a categoria?")
        entrada_categoria = input("\n   Escolha: ")

        try:
            if entrada_categoria == '':
                entrada_categoria = 'Geral'
                break

            flag = False
            for categoria in db_manager.lista_categorias():
                if categoria[0] == entrada_categoria:
                    flag = True

            if flag:
                break
        except ValueError:
            print(RED, NEGRITO, "\n Categoria não achada!")

    data_validada = formatacao_data(*validacao_data())

    db_manager.adicionar_tarefa(nova_tarefa, data_validada, entrada_obsevacao, prioridade_tarefa, entrada_categoria)


#  Validação dos índices
def validacao_indice():
    lista_de_tuplas_indices = db_manager.indices()
    tupla_indice = ()

    # Parte da função para desempacotar as listas de tuplas
    for tupla in lista_de_tuplas_indices:
        tupla_indice += tupla

    while True:
        if tupla_indice == ():
            return None

        entrada_indice = input("\n   Índice da tarefa: ").strip()

        try:
            entrada_indice = int(entrada_indice)
            if entrada_indice in tupla_indice:
                print(GREEN, NEGRITO, "Encontrado", RESET)
                break
            else:
                print(RED, NEGRITO, "\n Índice não encontrado", RESET)
        except ValueError:
            print(RED, NEGRITO, "\n Índice INVALIDO ", RESET)

    return entrada_indice


def remover_tarefa():  # Remover tarefa
    print('_' * 26)
    print(RED, NEGRITO, '\n  Remover Tarefa', RESET)
    db_manager.remover_tarefa(validacao_indice())


def alt_feita():  # Mudar para feita a tarefa
    print('_' * 26)
    print(GREEN, NEGRITO, '\n Marcar como Feita', RESET)
    db_manager.alt_feita(validacao_indice())


def alt_nao_feita():  # Mudar para não feita a tarefa
    print('_' * 26)
    print(RED, NEGRITO, '\n  Marcar como Não Feita', RESET)
    db_manager.alt_nao_feita(validacao_indice())


# Descrições das tarefas
def acessar_descricoes():
    print('_' * 26)
    print(GREEN, NEGRITO, '\n  Acessar Descrições', RESET)
    indice_validacao = validacao_indice()

    if not db_manager.descricoes(indice_validacao):
        print(RED, NEGRITO, "\n  Não há descrições!", RESET)
        pause = input("\nPressione ENTER para continuar")
    elif db_manager.descricoes(indice_validacao)[0][0].strip() == '':
        print(RED, NEGRITO, '\n   Não há descrições para essa tarefa!', RESET)
        pause = input("\nPressione ENTER para continuar")
    else:
        print(f'\n {NEGRITO}   " {db_manager.descricoes(indice_validacao)[0][0]} "{RESET}')
        pause = input("\nPressione ENTER para continuar")


if __name__ == "__main__":
    main()
