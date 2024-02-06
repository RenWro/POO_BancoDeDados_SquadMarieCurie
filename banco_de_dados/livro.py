import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE livro(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(100), disponivel BOOLEAN, copias INTEGER, '
    'editora_id INTEGER,'
    'genero_id INTEGER, FOREIGN KEY(editora_id) REFERENCES editora(id), FOREIGN KEY(genero_id) REFERENCES genero(id))')

conexao.commit()
conexao.close()
