""" Foi de bom ânimo a criação de outro arquivo para o banco de dados. 
    Para que dessa maneira fique mais organizado e encapsulado os métodos do BD """
    
import sqlite3  #  Banco de dados nativo do Python. Dessa forma não precisando que o usuário
                #  abaixe qualquer biblioteca python


#  Classe gerenciadora de Banco de dados.
class GerenciadorBD:
    #  Conexão com o Banco de dados
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    #  Fechamento da conexão
    def close_connection(self):
        self.conn.close()

    #  Retornar todos os campos da tabela TBTAREFA ordenados pelo campo PRIORIDADE
    def tarefas(self):
        self.cursor.execute("SELECT * FROM TBTAREFA ORDER BY PRIORIDADE DESC")
        return self.cursor.fetchall()

    #  Adição de uma nova linha à TBTAREFA
    def adicionar_tarefa(self, tarefa, data, obs, prioridade):
        self.cursor.execute("INSERT INTO TBTAREFA (tarefa, feita, data, nota, prioridade) VALUES (?, 0, ?, ?, ?)",
                            (tarefa, data, obs, prioridade))
        self.conn.commit()

    #  Retornar somente os índices da TBTAREFA
    def indices(self):
        self.cursor.execute("SELECT id_tarefa FROM TBTAREFA")
        return self.cursor.fetchall()

    #  Remoção de uma linha da TBTAREFA
    def remover_tarefa(self, id_indice):
        self.cursor.execute("DELETE FROM TBTAREFA WHERE id_tarefa = ?", (id_indice,))
        self.conn.commit()

    #  Alterar a linha 'feita' para 1 quando o usuário completar a tarefa e selecionar dentre as opções '[F]eita'
    def alt_feita(self, id_indice):
        self.cursor.execute("UPDATE TBTAREFA SET feita = ? WHERE id_tarefa = ?", (1, id_indice))
        self.conn.commit()

    #  Alterar a linha 'feita' para 0 quando o usuário completar a tareafa e selcionar dentre as opções '[N]ão Feita' 
    def alt_nao_feita(self, id_indice):
        self.cursor.execute("UPDATE TBTAREFA SET feita = ? WHERE id_tarefa = ?", (0, id_indice))
        self.conn.commit()

    #  Retorna o campo descrições da TBTAREFA
    def descricoes(self, task_id):
        self.cursor.execute("SELECT nota FROM TBTAREFA WHERE id_tarefa = ?", (task_id,))
        return self.cursor.fetchall()
