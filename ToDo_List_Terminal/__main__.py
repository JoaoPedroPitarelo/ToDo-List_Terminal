"""" ToDo-List Terminal """
# Tentar levantar ele como um serviço, para que possa te enviar notificações

import time

import funcs

db_manager = funcs.GerenciadorBD()
db_manager.create_table()


def exibir_tarefas():

    if not db_manager.tarefas():
        print(funcs.NEGRITO + funcs.GREEN + "\n Não há nada para fazer :)" + funcs.RESET)
    else:
        print('Suas tarefas: ')

        print("_" * 2, "Geral", "_" * 19)
        for tarefa in db_manager.tarefas():

            if tarefa[6] == 'Geral':

                if tarefa[5] == 3:
                    prioridade = f"{funcs.RED}alta{funcs.RESET} "

                    print(funcs.GREEN + funcs.NEGRITO + "  Feita   " + funcs.RESET if tarefa[2] == 1 else funcs.RED + funcs.NEGRITO + "  N Feita " + funcs.RESET,
                          funcs.NEGRITO, "|",
                          f"ID: {tarefa[0]}",
                          f"| Data: {tarefa[3]}",
                          f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{funcs.RESET}")

                elif tarefa[5] == 2:
                    prioridade = f"{funcs.YELLOW}média{funcs.RESET}"

                    print(funcs.GREEN + funcs.NEGRITO + "  Feita   " + funcs.RESET if tarefa[2] == 1 else funcs.RED + funcs.NEGRITO + "  N Feita " + funcs.RESET,
                          funcs.NEGRITO, "|",
                          f"ID: {tarefa[0]}",
                          f"| Data: {tarefa[3]}",
                          f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{funcs.RESET}")

                else:
                    prioridade = f"{funcs.GREEN}baixa{funcs.RESET}"

                    print(funcs.GREEN + funcs.NEGRITO + "  Feita   " + funcs.RESET if tarefa[2] == 1 else funcs.RED + funcs.NEGRITO + "  N Feita " + funcs.RESET,
                          funcs.NEGRITO, "|",
                          f"ID: {tarefa[0]}",
                          f"| Data: {tarefa[3]}",
                          f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{funcs.RESET}")

        for categoria in db_manager.lista_categorias():
            print("_" * 2, f"{categoria[0]}", "_" * (24 - (len(categoria[0]))))

            for tarefa in db_manager.tarefas():
                if tarefa[6] == categoria[0]:

                    if tarefa[5] == 2:
                        prioridade = f"{funcs.RED}alta{funcs.RESET} "

                        print(funcs.GREEN + funcs.NEGRITO + "  Feita   " + funcs.RESET if tarefa[2] == 1 else funcs.RED + funcs.NEGRITO + "  N Feita " + funcs.RESET,
                              funcs.NEGRITO, "|",
                              f"ID: {tarefa[0]}",
                              f"| Data: {tarefa[3]}",
                              f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{funcs.RESET}")

                    elif tarefa[5] == 1:
                        prioridade = f"{funcs.YELLOW}média{funcs.RESET}"

                        print(funcs.GREEN + funcs.NEGRITO + "  Feita   " + funcs.RESET if tarefa[2] == 1 else funcs.RED + funcs.NEGRITO + "  N Feita " + funcs.RESET,
                              funcs.NEGRITO, "|",
                              f"ID: {tarefa[0]}",
                              f"| Data: {tarefa[3]}",
                              f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{funcs.RESET}")

                    else:
                        prioridade = f"{funcs.GREEN}baixa{funcs.RESET}"

                        print(funcs.GREEN + funcs.NEGRITO + "  Feita   " + funcs.RESET if tarefa[2] == 1 else funcs.RED + funcs.NEGRITO + "  N Feita " + funcs.RESET,
                              funcs.NEGRITO, "|",
                              f"ID: {tarefa[0]}",
                              f"| Data: {tarefa[3]}",
                              f"| Prioridade: {prioridade} | Tarefa:  {tarefa[1]}{funcs.RESET}")


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
            print(funcs.RED, funcs.NEGRITO, "\n Entrada INVALIDA", funcs.RESET)

    # Achar uma maneira mais elegante de fazer isso
    if entrada_usuario == "A":
        adicionar_tarefa()
        funcs.clear_terminal()
    elif entrada_usuario == "R":
        remover_tarefa()
        funcs.clear_terminal()
    elif entrada_usuario == "N":
        alt_nao_feita()
        funcs.clear_terminal()
    elif entrada_usuario == "F":
        alt_feita()
        funcs.clear_terminal()
    elif entrada_usuario == "D":
        acessar_descricoes()
        funcs.clear_terminal()
    elif entrada_usuario == "-R":
        refresh()
    elif entrada_usuario == "C":
        funcs.opcao_categoria()
    elif entrada_usuario == "S":
        return entrada_usuario


#   Função Principal(main)
def main():  

    while True:
        funcs.clear_terminal()
        funcs.logo()
        exibir_tarefas()

        if entrada_opcao() == "S":
            funcs.clear_terminal()
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


def adicionar_tarefa():
    print('_' * 26)
    print(funcs.GREEN, funcs.NEGRITO, "\n  Adicionar Tarefa", funcs.RESET)

    print(funcs.CLARO, '\n "Faça em breves palavras Ex: Tomar café"', funcs.RESET)
    while True:
        nova_tarefa = input("   Nome Tarefa: ")

        if not nova_tarefa:
            print(funcs.RED, funcs.NEGRITO, "\n A tarefa Precisa ter um nome!", funcs.RESET)
        else:
            break

    entrada_obsevacao = input("      Desc da tarefa: ")

    print('_' * 26)
    while True:
        print(f"\n  [{funcs.GREEN}1-Baixa{funcs.RESET}] [{funcs.YELLOW}2-Média{funcs.RESET}] [{funcs.RED}3-Alta{funcs.RESET}]")
        prioridade_tarefa = input("   Qual a prioridade da tarefa?: ").strip()

        try:
            prioridade_tarefa = int(prioridade_tarefa)

            if prioridade_tarefa in [1, 2, 3]:
                break
            else:
                print(funcs.RED, funcs.NEGRITO, "\n Digite entre 1 - 3!")
        except ValueError:
            print(funcs.RED, funcs.NEGRITO, "\n Entrada inválida ", funcs.RESET)

    print('_' * 26)
    while True:

        lista_formatada = ''
        for i in db_manager.lista_categorias():
            lista_formatada += "" + i[0] + "  "

        print(
            '\n    Categorias: ',
            funcs.GREEN, funcs.NEGRITO, '[ ',
            funcs.WHITE, lista_formatada,
            funcs.GREEN, ']', funcs.RESET
        )

        print(funcs.CLARO, "\n  <Enter> = Geral", funcs.RESET)
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
            print(funcs.RED, funcs.NEGRITO, "\n Categoria não achada!")

    data_validada = funcs.formatacao_data(*funcs.validacao_data())

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
                print(funcs.GREEN, funcs.NEGRITO, "Encontrado", funcs.RESET)
                break
            else:
                print(funcs.RED, funcs.NEGRITO, "\n Índice não encontrado", funcs.RESET)
        except ValueError:
            print(funcs.RED, funcs.NEGRITO, "\n Índice INVALIDO ", funcs.RESET)

    return entrada_indice


def remover_tarefa():  # Remover tarefa
    print('_' * 26)
    print(funcs.RED, funcs.NEGRITO, '\n  Remover Tarefa', funcs.RESET)
    db_manager.remover_tarefa(validacao_indice())


def alt_feita():  # Mudar para feita a tarefa
    print('_' * 26)
    print(funcs.GREEN, funcs.NEGRITO, '\n Marcar como Feita', funcs.RESET)
    db_manager.alt_feita(validacao_indice())


def alt_nao_feita():  # Mudar para não feita a tarefa
    print('_' * 26)
    print(funcs.RED, funcs.NEGRITO, '\n  Marcar como Não funcs.Feita', funcs.RESET)
    db_manager.alt_nao_feita(validacao_indice())


# Descrições das tarefas
def acessar_descricoes():
    print('_' * 26)
    print(funcs.GREEN, funcs.NEGRITO, '\n  Acessar Descrições', funcs.RESET)
    indice_validacao = validacao_indice()

    if not db_manager.descricoes(indice_validacao):
        print(funcs.RED, funcs.NEGRITO, "\n  Não há descrições!", funcs.RESET)
        pause = input("\nPressione ENTER para continuar")
    elif db_manager.descricoes(indice_validacao)[0][0].strip() == '':
        print(funcs.RED, funcs.NEGRITO, '\n   Não há descrições para essa tarefa!', funcs.RESET)
        pause = input("\nPressione ENTER para continuar")
    else:
        print(f'\n {funcs.NEGRITO}   " {db_manager.descricoes(indice_validacao)[0][0]} "{funcs.RESET}')
        pause = input("\nPressione ENTER para continuar")


if __name__ == "__main__":
    main()
