from DataBaseManager import *
from validations import *

class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    dbmanager = DataBaseManager("database.db")    
        
    def set_category(category_name):
        
        if not validate_category(category_name):
            dbmanager.add_category(category_name)
            return True
        else:
            return False
        
    def remove_category(category_name):
        
        if validate_category(category_name):
            dbmanager.remove_category(category_name)
            
            for task in dbmanager.get_tasks():
                if task[3] == category_name:
                    dbmanager.remove_task(task[0])
            return True
        else:
            return False
        
    def modify_category_name(old_category_name, new_category_name):
        
            
            if validate_category(old_category_name):
                dbmanager.modify_name_category_from_tbcategory(old_category_name, new_category_name)
                
                for task in dbmanager.get_tasks():
                    if task[3] == old_category_name:
                        dbmanager.modify_name_category_from_tbtask(old_category_name, new_category_name)
                return True
            else:
                return False

    
        
    
