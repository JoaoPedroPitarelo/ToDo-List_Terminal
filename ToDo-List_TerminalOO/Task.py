from DataBaseManager import DataBaseManager
from validations import *


class Task:
    def __init__(self, state, index, date, priority, name, description, category):
        self.__index = index
        self.__name = name
        self.__state = state
        self.__date = date
        self.__priority = priority
        self.__description = description
        self.__category = category        
  
    dbmanager = DataBaseManager("database.db")
    dbmanager.create_tables()

    def set_task(task_name, description, category, date, priority):        
       
        if validate_date(date) and validate_priority(priority) and validate_category(category):  
            dbmanager.add_task(task_name, description, category, date, priority)
            return True
        else:
            return False  # Não sei se seria correto, porém com raise ele para a execução 
        
        
    def remove_task(id_task): 
        
        if validate_index(id_task):
            dbmanager.remove_task(id_task)
            return True
        else:    
            return False  # Não sei se seria correto, porém com raise ele para a execução 
                

    def set_state_to_done(id_task):
        
        if (validate_index):
            dbmanager.modify_state_to_done(id_task)
            return True
        else:
            return False  # Não sei se seria correto, porém com raise ele para a execução 
            
            
    def set_state_to_not_done(id_task):
        
        if (validate_index):
            dbmanager.modify_state_to_not_done(id_task)
            return True
        else:
            return False  # Não sei se seria correto, poém com raise ele para a execução 
                 
                      
    
    # def alt_feita():  # Mudar para feita a tarefa
    #     print('_' * 26)
    #     print(funcs.GREEN, funcs.NEGRITO, '\n Marcar como Feita', funcs.RESET)
    #     db_manager.alt_feita(validacao_indice())
    
    # def alt_nao_feita():  # Mudar para não feita a tarefa
    #     print('_' * 26)
    #     print(funcs.RED, funcs.NEGRITO, '\n  Marcar como Não funcs.Feita', funcs.RESET)
    #     db_manager.alt_nao_feita(validacao_indice())


