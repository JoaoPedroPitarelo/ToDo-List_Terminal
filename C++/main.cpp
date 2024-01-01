#include <iostream>
#include <sqlite3.h>
#include <locale.h>
#include <ctype.h>
#include <array>
using namespace std;


// Constantes das cores 
#define RESET     "\033[0m"
#define RED       "\033[31m"
#define GREEN     "\033[32m"
#define YELLOW    "\033[33m"
#define BLUE      "\033[34m"
#define MAGENTA   "\033[35m"
#define CYAN      "\033[36m"
#define WHITE     "\033[37m"
#define BG_GREEN  "\033[42m"
#define BG_YELLOW "\033[43m"
#define BG_RED    "\033[41m"
#define NEGRITO   "\033[1m"
#define CLARO     "\033[90m"

// Prototipação das funções
void logo();
void adicionar_tarefa();
void remover_tarefa();
void alt_feita();
void alt_nao_feita();
void acessar_descricoes();
void entrada_opcoes();


// Função para limpar o terminal
void clear_terminal() {
    cout << "\033[2J\033[1;1H"; //  Saída ANSII para limpar o terminal
}


bool chave = true; //  Necessário para que possar ser quebrado o loop. Ver em entrada_opcoes()
// Função main
int main() {
    setlocale(LC_ALL, "portuguese");

    while (chave) {
        logo();
        entrada_opcoes();
    }
}


// Função que exibe o 'logo' do algoritmo. Essa função é para organização do código
void logo() {
    cout << NEGRITO << "                     "    << GREEN <<"  _____                   _             _ \n";
    cout << WHITE << "     /////|           "     << GREEN << "|_   _|__ _ __ _ __ ___ (_)_ __   __ _| |\n";
    cout << WHITE << "    ///// |    (\\       "  << GREEN <<   "| |/ _ \\ '__| '_ ` _ \\| | '_ \\ / _` | |\n";
    cout << WHITE << "   |~~~|  |    \\ \\      " << GREEN <<   "| |  __/ |  | | | | | | | | | | (_| | |\n";
    cout << WHITE << "   |===|  |     \\ \\     " << GREEN <<   "|_|\\___|_|  |_| |_| |_|_|_| |_|\\__,_|_|\n";
    cout << WHITE << "   |T  |  |     / '|   "    << MAGENTA <<  "         _____     ____   ___  _     ___    _____\n"; 
    cout << WHITE << "   | D |  |     \\ '/  "    << MAGENTA << "         |_   _|__ |  _ \\ / _ \\| |   |_ _|__|_   _|\n"; 
    cout << WHITE << "   |  L| /        \\      " << MAGENTA <<    "        | |/ _ \\| | | | | | | |    | |/ __|| |  \n"; 
    cout << WHITE << "   |===|/         ==).   "  << MAGENTA <<    "        | | (_) | |_| | |_| | |___ | |\\__ \\| | \n"; 
    cout << WHITE << "   '---'         (__)   "   << MAGENTA <<   "         |_|\\___/|____/ \\___/|_____|___|___/|_| \n" << RESET;
}


//  Função para a entrada do usuário nas opções
void entrada_opcoes() { 
    cout << "\nOPÇÕES:  \n";
    cout << "     [A]dicionar Tarefa  [N]ão Feita  [D]esc tarefas\n"
            "     [R]emover Tarefa    [F]eita      [S]air"; 

    char entrada_usuario;
    bool encontrou = false;
    
    while (encontrou == false) {
        char entrada_validas[] = {'A', 'R', 'F', 'N', 'D', 'S'}; 

        
        cout << "\n\n Escolha: ";
        cin >> entrada_usuario; 
        entrada_usuario = toupper(entrada_usuario); // Convertendo para maiuscúla


        for (char letra : entrada_validas) {
            if (letra == entrada_usuario) {
                encontrou = true;
                break;
            }
        }
        if (encontrou == false) {
            cout << "\n Entrada inválida!";
        }
    }

    switch (entrada_usuario) {
        case 'A': 
            clear_terminal();
            cout << "adicionar_tarefa()";
            break;
        case 'R':
            clear_terminal();
            cout << "remover_tarefa()";
            break;
        case 'F':
            clear_terminal();
            cout << "alt_feita()";
            break;
        case 'N':
            clear_terminal();
            cout << "alt_nao_feita()";
            break;
        case 'D':
            clear_terminal();
            cout << "acessar_descricoes()";
            break;
        case 'S':
            clear_terminal();
            cout << "Sair";
            chave = false;
    }
}