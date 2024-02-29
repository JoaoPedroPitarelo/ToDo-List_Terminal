from DataBaseManager import DataBaseManager

dbmanager = DataBaseManager()

__ALL__ = ['validate_index', 'validate_priority', 'validate_categoty', 'validate_date']

def validate_index(index):
    list_indexes = []
    
    for tuple in dbmanager.get_indexes():
        list_indexes += tuple
    
    if index in list_indexes:
        return True 
    return False 
    

def validate_priority(input_value):
    if input_value in [1, 2, 3]:
        return True
    return False


def validate_category(input_value):
    list_categories = []
    
    for tuple in dbmanager.get_categories():
        list_categories += tuple
    
    if input_value in list_categories:
        return True
    return False
    
    
def validate_date(input_date):
    # Brazilian form
    
    numeric_date = int(input_date[0:2]),\
                   int(input_date[3:5]),\
                   int(input_date[6:10])
                   
    numeric_date = list(numeric_date)
                   
    if numeric_date[2] <= 2000:
        numeric_date[2] += 2000
               
    if 0 <= numeric_date[0] >= 30 and numeric_date[1] == 2:
        return False
    
    elif 0 <= numeric_date[0] >= 31 and numeric_date[1] in [4, 6, 9, 11]:
        return False
    
    elif 1 <= numeric_date[0] <= 31 and 1 <= numeric_date[1] <= 12 and 2000 <= numeric_date[2] <= 3000:
        return True
    
    else:
        return False
    