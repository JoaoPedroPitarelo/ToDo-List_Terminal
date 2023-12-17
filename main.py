"""" Algoritmo de Lista To Do """
import sqlite3
import os

conn = sqlite3.connect("database.db")  # conexão com banco de dados
cursor = conn.cursor()


def main():  # Função main
    clear_terminal()
    """Coleta dos dados do DB e retorna uma lista de tarefas"""
    cursor.execute("SELECT * FROM TBTAREFA")  # Coletar dados do BD
    lista_tarefas = cursor.fetchall()  # Captura dos dados
    print(" ")

    print('Lista de Tarefas: ')

    if not lista_tarefas:  # Menu de tarefas
        print("\n Não há nada para fazer :)")
    else:
        print("_" * 17, "\n")
        for i, tarefa in enumerate(lista_tarefas):
            print("  FEITA     |" if tarefa[2] == 1 else "  NÃO FEITA |", "ID: ", tarefa[0], "| Data: ", tarefa[3],
                  "| Tarefa: ", tarefa[1])

    print("\nOPÇÕES: ")
    print("[A]dicionar Tarefa  [N]ão Feita\n"  # Opções de entrada do Usuário
          "[R]emover Tarefa    [F]eita")

    while True:  # Entrada opção
        entrada_opcao = input('\n Escolha: ').upper().strip()

        if entrada_opcao.isalpha() and entrada_opcao.upper() in ["A", "R", "F", "N"]:
            break
        else:
            print("\n Entrada INVALIDA >(")
            # entrada_opcao = input('\n Escolha: ').upper().strip()  # Entrada opção

    if entrada_opcao == "A":  # "Switch case" da entrada
        adicionar_tarefa()
        clear_terminal()
        main()
    elif entrada_opcao == "R":
        remover_tarefa()
        # clear_terminal()
        main()
    elif entrada_opcao == "N":
        alt_nao_feita()
        main()
    elif entrada_opcao == "F":
        alt_feita()
        main()
    else:
        # clear_terminal()
        print("\n Nenhuma das opções Selecionadas :(")
        main()


def adicionar_tarefa():  # Adicionar nova tarefa à lista
    nova_tarefa = input("\n Nova Tarefa: ")

    while True:  # Entrada da data

        dia_entrada = input("  Dia: ")
        mes_entrada = input("    Mês: ")
        ano_entrada = input("      Ano: ")

        try:
            dia_entrada = int(dia_entrada)
            mes_entrada = int(mes_entrada)
            ano_entrada = int(ano_entrada)

            if 0 <= dia_entrada >= 30 and mes_entrada in [2]:  # Verificação dos dias com seus respectivos meses
                print("\n Data INVALIDA")
            elif 0 <= dia_entrada >= 31 and mes_entrada in [4, 6, 9, 11]:
                print("\n Data INVALIDA")
            elif 1 <= dia_entrada <= 31 and 1 <= mes_entrada <= 12 and 2000 <= ano_entrada <= 3000:
                break
            else:
                print("\n Data INVALIDA")

        except ValueError:
            print("\n Data INVALIDA")

    if dia_entrada in range(0, 9) or mes_entrada in range(0, 9):  # Formatação da data. Para não ficar Ex: 1/1/2024
        data_formatada = f"0{dia_entrada}/0{mes_entrada}/{ano_entrada}"
    else:
        data_formatada = f"{dia_entrada}/{mes_entrada}/{ano_entrada}"

    cursor.execute("INSERT INTO TBTAREFA (tarefa, feita, data) VALUES (?, 0, ?)", (nova_tarefa, data_formatada))
    conn.commit()


def remover_tarefa():  # Remover tarefa
    cursor.execute("SELECT id_tarefa FROM TBTAREFA")  # Coleta dos índices no BD
    lista_de_tuplas_indices = (cursor.fetchall())  # Lista de tuplas [(0,), (1,), (2,)]
    tupla_indice = ()

    for tupla in lista_de_tuplas_indices:  # Desempacotando a lista de tuplas em somente uma tupla
        tupla_indice += tupla

    while True:
        if tupla_indice == ():  # Caso a lista esteja vazia
            break

        entrada_indice = input("\n Índice: ").strip()

        try:
            entrada_indice = int(entrada_indice)
            if entrada_indice in tupla_indice:
                print("Encontrado")
                cursor.execute(f"DELETE FROM TBTAREFA WHERE id_tarefa = {entrada_indice};")
                conn.commit()
                break
            else:
                print("\n Índice não encontrado")
        except ValueError:
            print("\n Índice INVALIDO ")


def alt_feita():  # Mudar para feita a tarefa
    cursor.execute("SELECT id_tarefa FROM TBTAREFA")  # Coleta dos índices no BD
    lista_de_tuplas_indices = (cursor.fetchall())  # Lista de tuplas [(0,), (1,), (2,)]
    tupla_indice = ()

    for tupla in lista_de_tuplas_indices:  # Desempacotando a lista de tuplas em somente uma tupla
        tupla_indice += tupla

    while True:
        if tupla_indice == ():  # Caso a lista esteja vazia
            break

        entrada_indice = input("\n Índice: ").strip()

        try:
            entrada_indice = int(entrada_indice)
            if entrada_indice in tupla_indice:
                print("Encontrado")
                cursor.execute("UPDATE TBTAREFA SET feita = ? WHERE id_tarefa = ?", (1, entrada_indice))
                conn.commit()
                break
            else:
                print("\n Índice não encontrado")
                entrada_indice = input("\n Índice: ").strip()
        except ValueError:
            print("\n Índice INVALIDO >(")
            entrada_indice = input("\n Índice: ").strip()


def alt_nao_feita():  # Mudar para não feita a tarefa
    cursor.execute("SELECT id_tarefa FROM TBTAREFA")  # Coleta dos índices no BD
    lista_de_tuplas_indices = (cursor.fetchall())  # Lista de tuplas [(0,), (1,), (2,)]
    tupla_indice = ()

    for tupla in lista_de_tuplas_indices:  # Desempacotando a lista de tuplas em somente uma tupla
        tupla_indice += tupla

    while True:
        if tupla_indice == ():  # Caso a lista esteja vazia
            break

        entrada_indice = input("\n Índice: ").strip()

        try:
            entrada_indice = int(entrada_indice)
            if entrada_indice in tupla_indice:
                print("Encontrado")
                cursor.execute("UPDATE TBTAREFA SET feita = ? WHERE id_tarefa = ?", (0, entrada_indice))
                conn.commit()
                break
            else:
                print("\n Índice não encontrado")
                entrada_indice = input("\n Índice: ").strip()
        except ValueError:
            print("\n Índice INVALIDO >(")
            entrada_indice = input("\n Índice: ").strip()


def clear_terminal():  # Função para limpar o terminal
    if os.name == 'nt':  # Caso seja Windows
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')  # Caso seja sistemas Linux


main()
