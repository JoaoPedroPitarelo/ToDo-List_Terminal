package Tarefas;

public class Tarefa {
	
	// Atributos de cada tarefa
	private char estado;
	private int indice;
	private String data;
	private int prioridade;
	private String nome;
	
	// Construtor
	public Tarefa(char estado, int indice, String data, int prioridade, String nome) {
		this.estado = estado;
		this.indice = indice;
		this.data = data;
		this.prioridade = prioridade;
		this.nome = nome;
	}
}
