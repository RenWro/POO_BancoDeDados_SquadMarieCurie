import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE emprestimo(id INTEGER PRIMARY KEY AUTOINCREMENT,usuario_id INTEGER, livro_id INTEGER, pegou_em DATE, '
    'devolveu_em DATE,'
    'devolvido_em DATE,'
    'devolvido BOOLEAN, FOREIGN KEY(usuario_id) REFERENCES usuario(id), FOREIGN KEY(livro_id) REFERENCES livro(id))')

conexao.commit()
conexao.close()
