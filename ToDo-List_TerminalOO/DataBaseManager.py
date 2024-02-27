import sqlite3

class DataBaseManager:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def create_tables(self):
        self.cursor.execute("create table if not exists tbcategory(category_name text primary key)")
        self.cursor.execute("create table if not exists tbtask(id_task INTEGER primary key,"
                            " task_name text not null,"
                            " state integer not null,"
                            " date date not null,"
                            " task_description text not null,"
                            " priority int not null,"
                            " category text,"
                            " foreign key (category) references tbcategory(category_name))")
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


    def get_tasks(self):
        self.cursor.execute("SELECT * FROM tbtask ORDER BY id_task")
        return self.cursor.fetchall()
    
    def get_indexes(self):
        self.cursor.execute("SELECT id_task FROM tbtask")
        return self.cursor.fetchall()

    def get_categories(self):
        self.cursor.execute("SELECT category_name FROM tbcategory")
        return self.cursor.fetchall()

    def get_description(self, id_task):
        self.cursor.execute("SELECT task_description FROM tbtask WHERE id_task = ?", (id_task,))
        return self.cursor.fetchall()
    

    def add_task(self, task_name, date, description, priority, category):
        self.cursor.execute("INSERT INTO tbtask (task_name,date, state, task_description, priority, category) VALUES (?, ?, 0, ?, ?, ?)",
                            (task_name, date, description, priority, category))
        self.conn.commit()
    
    def remove_task(self, id_task):
        self.cursor.execute("DELETE FROM tbtask WHERE id_task = ?", (id_task))
        self.conn.commit()

    def add_category(self, category_name):
        self.cursor.execute("INSERT INTO tbcategory (category_name) VALUES (?)", (category_name,))
        self.conn.commit()
        
    def remove_category(self, category_name):
        self.cursor.execute("DELETE FROM tbtask WHERE category_name = ?", (category_name,))
        self.conn.commit()
    

    def modify_status_to_done(self, id_task):
        self.cursor.execute("UPDATE tbtask SET state = ? WHERE id_task = ?", (1, id_task))
        self.conn.commit()

    def modify_status_to_not_done(self, id_task) :
        self.cursor.execute("UPDATE tbtask SET state = ? WHERE id_task = ?", (0, id_task))
    
