import sqlite3

conexao = sqlite3.connect('biblioteca')

cursor = conexao.cursor()

cursor.execute(
    'CREATE TABLE editora(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100))')

conexao.commit()
conexao.close()
