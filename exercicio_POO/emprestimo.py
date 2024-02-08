from abc import ABC, abstractmethod

class Emprestimo(ABC):
    def __init__(self):
        self.__emprestimos = {}

    @abstractmethod
    def emprestar_livro(self, livro, usuario):
        pass

    @abstractmethod
    def devolver_livro(self, livro):
        pass

    @abstractmethod
    def renovar_emprestimo(self, livro):
        pass
