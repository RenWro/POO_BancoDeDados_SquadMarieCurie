import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE usuario(id INTEGER PRIMARY KEY, nome VARCHAR(100), sobrenome VARCHAR(100), '
    'telefone INTEGER, nacionalidade VARCHAR(50), FOREIGN KEY (id) REFERENCES emprestimo(usuario_id))')

conexao.commit()
conexao.close()
