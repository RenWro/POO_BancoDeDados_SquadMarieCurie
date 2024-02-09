import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE livro(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(100), disponivel BOOLEAN, copias INTEGER, '
    'editora_id INTEGER,'
    'genero_id INTEGER, FOREIGN KEY(editora_id) REFERENCES editora(id), FOREIGN KEY(genero_id) REFERENCES genero(id))')

# Consulta para listar todos os livros disponíveis
cursor.execute('SELECT * FROM livro WHERE disponivel = 1')
livros_disponiveis = cursor.fetchall()
print("Livros disponíveis: ")
for livro in livros_disponiveis:
    print(livro.titulo) # é pra retornar tds os detalhes?

# Consulta para encontrar todos os livros emprestados no momento
cursor.execute('SELECT * FROM livro WHERE id IN (SELECT livro_id FROM emprestimo WHERE devolvido = 0)')
livros_emprestados = cursor.fetchall()
print("Livros emprestados no momento: ")
for livro in livros_emprestados:
    print(livro.titulo) # apenas o título? 

# Consulta o número de cópias disponíveis de um determinado livro
titulo_livro = input("Digite o título do livro: ")
cursor.execute('SELECT copias FROM livro WHERE titulo = ?', (titulo_livro,))
num_copias = cursor.fetchone()
if num_copias:
    print("Número de cópias disponíveis de", titulo_livro + ": ", num_copias[0])
else:
    print("Livro não encontrado.")

conexao.commit()
conexao.close()

