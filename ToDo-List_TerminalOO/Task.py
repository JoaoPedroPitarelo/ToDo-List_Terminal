class Task:
    def __init__(self, state, index, date, priority, name):
        self.__state = state
        self.__index = index
        self.__date = date
        self.__priority = priority
        self.__name = name
       
    # Getters 
    def get_state(self):
        return self.__state
    
    def get_index(self):
        return self.__index
    
    def get_date(self):
        return self.__date
    
    def get_priority(self):
        return self.__priority
    
    def get_name(self):
        return self.__name
    
    
    