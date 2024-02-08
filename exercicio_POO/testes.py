from biblioteca import *

#Inicialização de Usuários
usuario1 = ["João", "123456789", "Brasileiro"]
usuario2 = ["Maria", "987654321", "Brasileira"]
usuario3 = ["Fulano", "987651234", "Brasileiro"]
usuario4 = ["Beltrano", "123498765", "Brasileiro"]

# Inicialização de livros
livro1 = Livro('A Senhora do Lago', 'IMAGO', 'Marion Zimmer Brandley', ['Fantasy Fiction', 'Historical Fiction', 'Fairy tale'], 3)
livro2 = Livro('A Grande Rainha', 'IMAGO', 'Marion Zimmer Brandley', ['Fantasy Fiction', 'Historical Fiction', 'Fairy tale'], 2)

# Inicia Biblioteca
biblioteca = Biblioteca()

# Teste Empréstimos
biblioteca.emprestar_livro(livro1, usuario1, "01-01-2024")
biblioteca.emprestar_livro(livro2, usuario2, "01-01-2024")
biblioteca.emprestar_livro(livro2, usuario3, "02-01-2024")
biblioteca.emprestar_livro(livro2, usuario4, "04-01-2024")

# Teste Devolução
biblioteca.devolver_livro(livro2,usuario2, "07-01-2024")  

# Teste Renovação
biblioteca.renovar_emprestimo(livro1, usuario1)

# Histórico de Empréstimos
biblioteca.registro_emprestimos()