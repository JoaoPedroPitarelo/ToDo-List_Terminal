package Tarefas;

public class Tarefa {
	
	// Atributos de cada tarefa
	private char estado;
	private int indice;
	private String data;
	private int prioridade;
	private String nome;
	
	public char getEstado() {
		return estado;
	}
	public void setEstado() {
		this.estado = estado;
	}
	
	public int getIndice() {
		return indice;
	}
	public void setIndice() {
		this.indice = indice;
	}
	
	public String getData() {
		return data;
	}
	public void setData() {
		this.data = data;
	}
	
	public int getPrioridade() {
		return prioridade;
	}
	public void setPrioridade() {
		this.prioridade = prioridade;
	}
	
	public String getNome() {
		return nome;
	}
	public void setNome() {
		this.nome = nome;
	}
}
