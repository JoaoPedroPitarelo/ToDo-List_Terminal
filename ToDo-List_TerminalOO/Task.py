class Task:
    def __init__(self, state, index, date, priority, name, description):
        self.__index = index
        self.__name = name
        self.__state = state
        self.__date = date
        self.__priority = priority
        self.__description = description
        
       
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
        

    def set_task(self, state , index, date, priority, name):
        
            


    
