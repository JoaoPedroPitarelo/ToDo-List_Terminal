#include <iostream>
#include <sqlite3.h>
using namespace std;

class GerenciadorDB {
private:
    sqlite3* db;

public:
    GerenciadorDB(const char* db_name = "database.db") {
        int rc = sqlite3_open(db_name, &db);

        if (rc != SQLITE_OK) {
            cout << "Erro ao abrir o banco de dados: " << sqlite3_errmsg(db) << std::endl;
        }
    }

    ~GerenciadorDB() {
        sqlite3_close(db);
    }

    void executeQuery(const char* sql) {
        char* errMsg = nullptr;

        int rc = sqlite3_exec(db, sql, nullptr, nullptr, &errMsg);

        if (rc != SQLITE_OK) {
            std::cerr << "Erro ao executar a consulta: " << errMsg << std::endl;
            sqlite3_free(errMsg);
            // Aqui você pode adicionar tratamento de erro, se necessário.
        }
    }
};