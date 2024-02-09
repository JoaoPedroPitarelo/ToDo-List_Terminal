from .generalfuncs import *


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

    if dia in range(0, 10) and mes in range(0, 10):
        data_formatada = f"0{dia}/0{mes}/{ano}"
    elif dia in range(0, 10):
        data_formatada = f"0{dia}/{mes}/{ano}"
    elif mes in range(0, 9):
        data_formatada = f"{dia}/0{mes}/{ano}"
    else:
        data_formatada = f"{dia}/{mes}/{ano}"

    return data_formatada

