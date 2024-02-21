class Tarefas:
    def __init__(self, estado, indice, data, prioridade, nome):
        self.estado = estado
        self.indice = indice
        self.data = data
        self.prioridade = prioridade
        self.nome = nome
    
    
    def imprimir(self):
        print(f"{self.estado} id:{self.indice} data:{self.data} prioridade:{self.prioridade} nome:{self.nome}")      