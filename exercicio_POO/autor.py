class Autor:
    def __init__(self, nome, lista_livros=None):
        self.__nome = nome
        self.__lista_livros = lista_livros if lista_livros is not None else []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def lista_livros(self):
        return self.__lista_livros

    def adicionar_livro(self, livro):
        if livro not in self.__lista_livros:
            self.__lista_livros.append(livro)

    def __str__(self):
        return f"Autor: {self.__nome}, Livros: {', '.join([livro.titulo for livro in self.__lista_livros])}"
