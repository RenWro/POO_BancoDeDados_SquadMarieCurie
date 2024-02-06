import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE autores_livros(livro_id INTEGER, autor_id INTEGER, PRIMARY KEY (livro_id, autor_id), FOREIGN KEY ('
    'livro_id) REFERENCES livro(id), FOREIGN KEY (autor_id) REFERENCES autor(id))')

conexao.commit()
conexao.close()
