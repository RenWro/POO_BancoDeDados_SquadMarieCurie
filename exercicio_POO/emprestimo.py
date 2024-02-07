class Emprestimo:
    def _init_(self):
        self.__emprestimos = {}

    def emprestar_livro(self, livro, usuario):
        if livro.titulo not in self.__emprestimos:
            if livro._numero_exemplares > 0:
                livro._numero_exemplares -= 1
                self.__emprestimos[livro.titulo] = {'usuario': usuario, 'renovacoes': 0}
                print(f"Livro '{livro.titulo}' emprestado para {usuario}.")
            else:
                print(f"Livro '{livro.titulo}' não disponível para empréstimo.")
        else:
            print(f"Livro '{livro.titulo}' já está emprestado.")

    def devolver_livro(self, livro):
        if livro.titulo in self.__emprestimos:
            livro._numero_exemplares += 1
            del self.__emprestimos[livro.titulo]
            print(f"Livro '{livro.titulo}' devolvido com sucesso.")
        else:
            print(f"Livro '{livro.titulo}' não consta como emprestado.")

    def renovar_emprestimo(self, livro):
        if livro.titulo in self.__emprestimos:
            if self.__emprestimos[livro.titulo]['renovacoes'] < 3:
                self.__emprestimos[livro.titulo]['renovacoes'] += 1
                print(f"Empréstimo do livro '{livro.titulo}' renovado. Total de renovações: {self.__emprestimos[livro.titulo]['renovacoes']}.")
            else:
                print("Limite de renovações atingido.")
        else:
            print(f"Livro '{livro.titulo}' não está emprestado para ser renovado.")