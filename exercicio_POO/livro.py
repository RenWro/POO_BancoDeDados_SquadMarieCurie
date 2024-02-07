class Livro:
    def __init__(self, titulo, editora, autores=None, lista_generos=None, numero_exemplares=0):
        self.__titulo = titulo
        self.__editora = editora
        self.__autores = autores if autores is not None else []  # Inicializa com uma lista vazia se nenhum autor for fornecido
        self.__lista_generos = lista_generos if lista_generos is not None else []  # Inicializa com uma lista vazia se nenhum gênero for fornecido
        self._numero_exemplares = numero_exemplares

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, nova_editora):
        self.__editora = nova_editora

    @property
    def lista_generos(self):
        return self.__lista_generos

    @lista_generos.setter
    def lista_generos(self, nova_lista_generos):
        self.__lista_generos = nova_lista_generos

    @property
    def autores(self):
        return self.__autores


    def adicionar_autor(self, autor):
        if autor not in self.__autores:
            self.__autores.append(autor)
            autor.adicionar_livro(self)

    def detalhes_livro(self):
        estado = ' ----------------------------------\n'
        estado += f'  Livro: {self.__titulo}\n'
        estado += f'  Editora: {self.__editora}\n'
        estado += f'  Autor(es): {", ".join([autor.nome for autor in self.__autores])}\n'
        estado += f'  Gênero(s): {", ".join(self.__lista_generos)}\n'
        estado += f'  Número de exemplares: {self._numero_exemplares}\n'
        estado += ' ----------------------------------\n'
        return estado

    def __str__(self):
        return self.detalhes_livro()
