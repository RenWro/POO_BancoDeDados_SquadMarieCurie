import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE emprestimo(id INTEGER PRIMARY KEY AUTOINCREMENT,usuario_id INTEGER, livro_id INTEGER, pegou_em DATE, '
    'devolveu_em DATE,'
    'devolvido_em DATE,'
    'devolvido BOOLEAN, FOREIGN KEY(usuario_id) REFERENCES usuario(id), FOREIGN KEY(livro_id) REFERENCES livro(id))')

# Consulta os empréstimos em atraso
cursor.execute('SELECT * FROM emprestimo WHERE devolveu_em < DATE(\'now\') AND devolvido = 0')
emprestimos_atrasados = cursor.fetchall()
print("Empréstimos em atraso:")
for emprestimo in emprestimos_atrasados:
    print(emprestimo) # deixo apresentando tds os detalhes ou faço pegar o nome dos usuários em atraso?


conexao.commit()
conexao.close()
