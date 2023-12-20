import sqlite3


class GerenciadorBD:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def tarefas(self):
        self.cursor.execute("SELECT * FROM TBTAREFA ORDER BY PRIORIDADE DESC")
        return self.cursor.fetchall()

    def adicionar_tarefa(self, tarefa, data, obs, prioridade):
        self.cursor.execute("INSERT INTO TBTAREFA (tarefa, feita, data, nota, prioridade) VALUES (?, 0, ?, ?, ?)",
                            (tarefa, data, obs, prioridade))
        self.conn.commit()

    def indices(self):
        self.cursor.execute("SELECT id_tarefa FROM TBTAREFA")
        return self.cursor.fetchall()

    def remover_tarefa(self, id_indice):
        self.cursor.execute("DELETE FROM TBTAREFA WHERE id_tarefa = ?", (id_indice,))
        self.conn.commit()

    def alt_feita(self, id_indice):
        self.cursor.execute("UPDATE TBTAREFA SET feita = ? WHERE id_tarefa = ?", (1, id_indice))
        self.conn.commit()

    def alt_nao_feita(self, id_indice):
        self.cursor.execute("UPDATE TBTAREFA SET feita = ? WHERE id_tarefa = ?", (0, id_indice))
        self.conn.commit()

    def descricoes(self, task_id):
        self.cursor.execute("SELECT nota FROM TBTAREFA WHERE id_tarefa = ?", (task_id,))
        return self.cursor.fetchall()
