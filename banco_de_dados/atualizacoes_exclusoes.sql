-- Atualizar um livro como devolvido
UPDATE livros
SET status = 'Devolvido'
WHERE id_livro = 'id_do_livro';

/* Remover um autor e seus livros associados
   Esta operação removerá todos os livros associados ao autor antes de remover o autor */
DELETE FROM autores
WHERE id_autor = 'id_do_autor';

DELETE FROM livros
WHERE id_autor = 'id_do_autor';

