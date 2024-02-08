import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE autor(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), sobrenome VARCHAR(100))')

# Consultar os livros escritos por um autor específico
nome_autor = input("Digite o nome do autor: ")
cursor.execute('SELECT * FROM livro WHERE id IN (SELECT livro_id FROM autores_livros WHERE autor_id IN (SELECT id FROM autor WHERE nome = ?))', (nome_autor,))
livros_autor_especifico = cursor.fetchall()
print("Livros escritos por", nome_autor + ":")
for livro in livros_autor_especifico:
    print(livro.titulo)

conexao.commit()
conexao.close()
