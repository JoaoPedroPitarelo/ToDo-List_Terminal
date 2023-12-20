"""" Algoritmo de Lista To Do """
from database_manager import GerenciadorBD
import os

# conexão com banco de dados
db_manager = GerenciadorBD()

# Cores e constantes
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE= '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_RED = "\033[41m"
NEGRITO = '\033[1m'
CLARO = '\033[90m'


def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')  # Linux


#  Funções da parte "Home" do algoritmo
def logo():
    print(NEGRITO, "                     ", GREEN + "_____                   _             _ \n" +
        WHITE + "     /////|           " + GREEN + "|_   _|__ _ __ _ __ ___ (_)_ __   __ _| |\n" +
        WHITE + "    ///// |    (\       " + GREEN + "| |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |\n" +
        WHITE + "   |~~~|  |    \ \      " + GREEN + "| |  __/ |  | | | | | | | | | | (_| | |\n" +
        WHITE + "   |===|  |     \ \     " + GREEN + "|_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|\n" +
        WHITE + "   |T  |  |     / '|   " + MAGENTA + "         _____     ____   ___  _     ___    _____\n" +
        WHITE + "   | D |  |     \ '/  " + MAGENTA+  "         |_   _|__ |  _ \ / _ \| |   |_ _|__|_   _|\n" +
        WHITE + "   |  L| /        \      " + MAGENTA + "        | |/ _ \| | | | | | | |    | |/ __|| |  \n" +
        WHITE + "   |===|/         ==).   " + MAGENTA + "        | | (_) | |_| | |_| | |___ | |\__ \| | \n" +
        WHITE + "   '---'         (__)   " + MAGENTA + "         |_|\___/|____/ \___/|_____|___|___/|_| \n" + RESET
    )


def exibir_tarefas():
    lista_tarefas = db_manager.tarefas()

    if not lista_tarefas:
        print(NEGRITO + GREEN + "\n Não há nada para fazer :)" + RESET)
    else:
        print('Suas tarefas...')
        print("_" * 24, "\n")
        
        for i, tarefa in enumerate(lista_tarefas):
            
            if tarefa[5] == 2:
                prioridade = "🔴"
                
                print(GREEN + NEGRITO + " \u2713 " + RESET if tarefa[2] == 1 else RED + NEGRITO + " \u2718 " + RESET,
                NEGRITO, "|",
                f"ID: {tarefa[0]}",
                f"| Data: {tarefa[3]}",
                f"| Prioridade: {prioridade}{RESET} | Tarefa:  {tarefa[1]}{RESET}")
                
            elif tarefa[5] == 1:
                prioridade = "🟡"
                
                print(GREEN + NEGRITO + " \u2713 " + RESET if tarefa[2] == 1 else RED + NEGRITO + " \u2718 " + RESET,
                NEGRITO, "|",
                f"ID: {tarefa[0]}",
                f"| Data: {tarefa[3]}",
                f"| Prioridade: {prioridade}{RESET} | Tarefa:  {tarefa[1]}{RESET}")
                
            else:
                prioridade = "🟢"
                
                print(GREEN + NEGRITO + " \u2713 " + RESET if tarefa[2] == 1 else RED + NEGRITO + " \u2718 " + RESET,
                NEGRITO, "|",
                f"ID: {tarefa[0]}",
                f"| Data: {tarefa[3]}",
                f"| Prioridade: {prioridade}{RESET} | Tarefa:  {tarefa[1]}{RESET}")
            
        print("_" * 24, "\n")


def entrada_opcao():
    print("\nOPÇÕES: ")
    print("     [A]dicionar Tarefa  [N]ão Feita  [D]esc tarefas\n"  # Opções de entrada do Usuário
          "     [R]emover Tarefa    [F]eita      [S]air")

    while True:
        entrada_opcao = input('\n Escolha: ').upper().strip()

        if entrada_opcao.isalpha() and entrada_opcao.upper() in ["A", "R", "F", "N", "D", "S"]:
            break
        else:
            print(RED, NEGRITO, "\n Entrada INVALIDA >(", RESET)

    if entrada_opcao == "A":  # "Switch case" da entrada
        adicionar_tarefa()
        clear_terminal()
    elif entrada_opcao == "R":
        remover_tarefa()
        clear_terminal()
    elif entrada_opcao == "N":
        alt_nao_feita()
        clear_terminal()
    elif entrada_opcao == "F":
        alt_feita()
        clear_terminal()
    elif entrada_opcao == "D":
        acessar_descricoes()
        clear_terminal()
    elif entrada_opcao == "S":
        return entrada_opcao


#   Função Principal(main)
def main():  # Função main
    while True:
        clear_terminal()
        logo()
        exibir_tarefas()

        if entrada_opcao() == "S":
            break


#  Funções das opções do algoritmo (adicionar, remover, marcar como feita...)

#  Validação da data
def validacao_data():
    while True:
        dia_entrada = input("\n  Dia: ")
        mes_entrada = input("    Mês: ")
        ano_entrada = input("      Ano: ")

        try:
            dia_entrada = int(dia_entrada)
            mes_entrada = int(mes_entrada)
            ano_entrada = int(ano_entrada)

            if 0 <= dia_entrada >= 30 and mes_entrada in [2]:  # Verificação dos dias com seus respectivos meses
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


def adicionar_tarefa():
    print(CLARO, '\n "Faça em breves palavras Ex: Tomar café"', RESET)
    nova_tarefa = input("   Nome Tarefa: ")
    entrada_obsevacao = input("      Desc da tarefa: ")
    
    while True:
        print(CLARO, "\n         [0-Baixa] [1-Média] [2-Alta]", RESET)
        prioridade_tarefa = input("         Qual a prioridade da tarefa?: ").strip()
    
        try:
            prioridade_tarefa = int(prioridade_tarefa)
            
            if prioridade_tarefa in [0, 1, 2]:
                break
            else:
                print(RED, NEGRITO, "\n Digite entre 0 - 2!")
        except ValueError:
            print(RED, NEGRITO,  "\n Entrada inválida ", RESET)

    
    data_validada = validacao_data()

    if data_validada[0] in range(0, 9) and data_validada[1] in range(0, 9):
        data_formatada = f"0{data_validada[0]}/0{data_validada[1]}/{data_validada[2]}"
    elif data_validada[0] in range(0, 9):
        data_formatada = f"0{data_validada[0]}/{data_validada[1]}/{data_validada[2]}"
    elif data_validada[1] in range(0, 9):
        data_formatada = f"{data_validada[0]}/0{data_validada[1]}/{data_validada[2]}"
    else:
        data_formatada = f"{data_validada[0]}/{data_validada[1]}/{data_validada[2]}"

    db_manager.adicionar_tarefa(nova_tarefa, data_formatada, entrada_obsevacao, prioridade_tarefa)


#  Validação dos índices
def validacao_indice():
    lista_de_tuplas_indices = db_manager.indices()
    tupla_indice = ()

    for tupla in lista_de_tuplas_indices:
        tupla_indice += tupla

    entrada_indice = ''
    while True:
        if tupla_indice == ():
            return None

        entrada_indice = input("\n   Índice: ").strip()

        try:
            entrada_indice = int(entrada_indice)
            if entrada_indice in tupla_indice:
                print(GREEN, NEGRITO,  "Encontrado", RESET)
                break
            else:
                print(RED, NEGRITO,  "\n Índice não encontrado", RESET)
        except ValueError:
            print(RED, NEGRITO,  "\n Índice INVALIDO ", RESET)

    return entrada_indice



def remover_tarefa():  # Remover tarefa
    db_manager.remover_tarefa(validacao_indice())


def alt_feita():  # Mudar para feita a tarefa
    db_manager.alt_feita(validacao_indice())


def alt_nao_feita():  # Mudar para não feita a tarefa
    db_manager.alt_nao_feita(validacao_indice())


def acessar_descricoes():  # Descrições das tarefas
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
