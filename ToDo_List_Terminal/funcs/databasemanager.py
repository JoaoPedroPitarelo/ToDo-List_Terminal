import sqlite3


#  Classe gerenciadora de Banco de dados.
class GerenciadorBD:
    #  Conexão com o Banco de dados
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("create table if not exists tbcategoria(categoria_nome text primary key)")
        self.cursor.execute("create table if not exists tbtarefa(id_tarefa INTEGER primary key,"
                            " tarefa text not null,"
                            " estado integer not null,"
                            " data date not null,"
                            " descricao text not null,"
                            " prioridade int not null,"
                            " categoria text,"
                            " foreign key (categoria) references tbcategoria(categoria_nome))")
        self.conn.commit()

    #  Fechamento da conexão
    def close_connection(self):
        self.conn.close()

    #  Retornar todos os campos da tabela TBTAREFA ordenados pelo campo PRIORIDADE
    def tarefas(self):
        self.cursor.execute("SELECT * FROM TBTAREFA ORDER BY id_tarefa")
        return self.cursor.fetchall()

    #  Adição de uma nova linha à TBTAREFA
    def adicionar_tarefa(self, tarefa, data, obs, prioridade, categoria):
        self.cursor.execute("INSERT INTO TBTAREFA (tarefa, estado, data, descricao, prioridade, categoria) VALUES (?, 0, ?, ?, ?, ?)",
                            (tarefa, data, obs, prioridade, categoria))
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
        self.cursor.execute("UPDATE TBTAREFA SET estado = ? WHERE id_tarefa = ?", (1, id_indice))
        self.conn.commit()

    #  Alterar a linha 'feita' para 0 quando o usuário completar a tareafa e selcionar dentre as opções '[N]ão Feita' 
    def alt_nao_feita(self, id_indice):
        self.cursor.execute("UPDATE TBTAREFA SET estado = ? WHERE id_tarefa = ?", (0, id_indice))
        self.conn.commit()

    #  Retorna o campo descrições da TBTAREFA
    def descricoes(self, task_id):
        self.cursor.execute("SELECT descricao FROM TBTAREFA WHERE id_tarefa = ?", (task_id,))
        return self.cursor.fetchall()

    def lista_categorias(self):
        self.cursor.execute("SELECT categoria_nome FROM tbcategoria")
        return self.cursor.fetchall()

    def criar_categoria(self, nome_categoria):
        self.cursor.execute("INSERT INTO tbcategoria (categoria_nome) VALUES (?)", (nome_categoria,))
        self.conn.commit()

    def excluir_categoria(self, nome_categoria):
        self.cursor.execute("DELETE FROM tbcategoria WHERE categoria_nome = ?", (nome_categoria,))

        for tarefa in self.tarefas():
            if tarefa[6] == nome_categoria:
                self.remover_tarefa(tarefa[0])

        self.conn.commit()

