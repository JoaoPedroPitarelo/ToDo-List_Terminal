from DataBaseManager import *

dbmanager = DataBaseManager("database.db")
dbmanager.create_tables()


class Task:
    def __init__(self, state, index, date, priority, name, description, category):
        self.__index = index
        self.__name = name
        self.__state = state
        self.__date = date
        self.__priority = priority
        self.__description = description
        self.__category = category        
       
    # Getters 
    def get_index(self):
        return self.__index
    
    def get_name(self):
        return self.__name
    
    def get_state(self):
        return self.__state
    
    def get_date(self):
        return self.__date 
    
    def get_priority(self):
        return self.__priority
    
    def get_description(self):
        return self.__description
        

    def set_task(name, description, date, priority, category):        
        dbmanager.add_task(name, description, category, date, priority)