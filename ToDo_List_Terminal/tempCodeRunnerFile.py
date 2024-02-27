
def alt_nao_feita():  # Mudar para não feita a tarefa
    print('_' * 26)
    print(funcs.RED, funcs.NEGRITO, '\n  Marcar como Não funcs.Feita', funcs.RESET)
    db_manager.alt_nao_feita(validacao_indice())

