"""" ToDo-List Terminal """

from database_manager import GerenciadorBD #  Importando de 'database_manager.py' a classe gerenciadora do BD  
import time
import os

# Conexão com o gerenciador do BD
db_manager = GerenciadorBD()

#  Constantes da cores de acordo com os escapes ANSII
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


#  Função para limpar o terminar
def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')  # Sistemas Linux


#  Funções da parte "Home" do algoritmo

#  Função que exibe o 'logo' do algoritmo. Essa função é para organização do código
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


#  Fução que exibe a lista de tarefas
def exibir_tarefas():
    lista_tarefas = db_manager.tarefas()

    if not lista_tarefas:
        print(NEGRITO + GREEN + "\n Não há nada para fazer :)" + RESET)
    else:
        print('Suas tarefas...')
        print("_" * 24, "\n")
        
        for i, tarefa in enumerate(lista_tarefas):
            
            if tarefa[5] == 2:
                prioridade = f"{RED}***"
                
                print(GREEN + NEGRITO + "  \u2713 " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  \u2718 " + RESET,
                NEGRITO, "|",
                f"ID: {tarefa[0]}",
                f"| Data: {tarefa[3]}",
                f"| Prioridade: {prioridade}{NEGRITO}{WHITE} | Tarefa:  {tarefa[1]}{RESET}")
                
            elif tarefa[5] == 1:
                prioridade = f"{YELLOW}***"
                
                print(GREEN + NEGRITO + "  \u2713 " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  \u2718 " + RESET,
                NEGRITO, "|",
                f"ID: {tarefa[0]}",
                f"| Data: {tarefa[3]}",
                f"| Prioridade: {prioridade}{NEGRITO}{WHITE} | Tarefa:  {tarefa[1]}{RESET}")
                
            else:
                prioridade = f"{GREEN}***"
                
                print(GREEN + NEGRITO + "  \u2713 " + RESET if tarefa[2] == 1 else RED + NEGRITO + "  \u2718 " + RESET,
                NEGRITO, "|",
                f"ID: {tarefa[0]}",
                f"| Data: {tarefa[3]}",
                f"| Prioridade: {prioridade}{NEGRITO}{WHITE} | Tarefa:  {tarefa[1]}{RESET}")
            
        print("_" * 24, "\n")


#  Função para a entrada do usuário nas opções
def entrada_opcao():
    print("\nOPÇÕES: ")
    print("     [A]dicionar Tarefa  [N]ão Feita  [D]esc tarefas\n"  # Opções de entrada do Usuário
          "     [R]emover Tarefa    [F]eita      [S]air\n"
          "     [-R]efresh                                       ")

    while True:  # Cria um loop que certifica que o usuário não irá passar se não digitar uma das opções válidas
        entrada_usuario = input('\n Escolha: ').upper().strip()

        if entrada_usuario in ["A", "R", "F", "N", "D", "S", "-R"]:
            break
        else:
            print(RED, NEGRITO, "\n Entrada INVALIDA", RESET)

    if entrada_usuario == "A":  # "Switch case" da entrada
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
    elif entrada_usuario == "S":
        return entrada_usuario


#   Função Principal(main)
def main():  # Função main
    while True:
        clear_terminal()
        logo()
        exibir_tarefas()

        if entrada_opcao() == "S":
            print("  Saindo...")
            break


#  Funções das opções do algoritmo (adicionar, remover, marcar como feita, sair...)


def refresh():
    palavra = 'refresh'
    for loop in range(0,3):
        palavra = palavra + '.'
        print(palavra)
        time.sleep(0.2)
    time.sleep(1)


#  Validação de data
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


#  Adicionar uma tarefa à lista de tarefas
def adicionar_tarefa():
    print(CLARO, '\n "Faça em breves palavras Ex: Tomar café"', RESET)
    nova_tarefa = input("   Nome Tarefa: ")
    entrada_obsevacao = input("      Desc da tarefa: ")
    
    while True:
        print(f"\n         [0-Baixa {GREEN}***{RESET}] [1-Média {YELLOW}***{RESET}] [2-Alta {RED}***{RESET}]", RESET)
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

    #  Essa parte da função foi feita para formatação da data. Para que não saísse por exemplo: 2/1/2023
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

    for tupla in lista_de_tuplas_indices: #  Parte da função para desempacotar as listas de tuplas 
       tupla_indice += tupla

    while True:  #  Além de verificar se o que o usuario digitou é um inteiro verifica se esse inteiro está entre os índices
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
