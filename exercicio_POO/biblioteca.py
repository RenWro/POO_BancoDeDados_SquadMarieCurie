from emprestimo import *
from livro import *
# from usuario import *

class Biblioteca(Emprestimo):
    def __init__(self):
        super().__init__()
        self.__emprestimos = {}

    def emprestar_livro(self, livro, usuario, data_emprestimo):
        if livro._numero_exemplares > 0:
            if livro.titulo in self.__emprestimos:
                self.__emprestimos[livro.titulo]["emprestimos"].append({"Para o usuário": usuario, "status": "emprestado", "Data": data_emprestimo, "renovacoes": 0})
                livro._numero_exemplares -= 1
                print(f"Livro '{livro.titulo}' emprestado para {usuario} na data {data_emprestimo}.")
            else:
                self.__emprestimos[livro.titulo] = {"emprestimos": [{"Para o usuário": usuario, "status": "emprestado", "Data": data_emprestimo, "renovacoes": 0}]}
                livro._numero_exemplares -= 1
                print(f"Livro '{livro.titulo}' emprestado para {usuario} na data {data_emprestimo}.")
        else:
            print(f"Não há exemplares do livro {livro.titulo} disponíveis para empréstimos.")

    def devolver_livro(self, livro, usuario, data_devolucao):
        if livro.titulo in self.__emprestimos:
            emprestimos = self.__emprestimos[livro.titulo]["emprestimos"]
            for emprestimo in emprestimos:
                if emprestimo["Para o usuário"] == usuario:
                    livro._numero_exemplares += 1
                    if "devolucoes" not in self.__emprestimos[livro.titulo]:
                        self.__emprestimos[livro.titulo]["devolucoes"] = []
                    self.__emprestimos[livro.titulo]["devolucoes"].append({"Pelo usuário": usuario, "status": "devolvido", "Data": data_devolucao})
                    print(f"Livro '{livro.titulo}' foi devolvido por {usuario} na data {data_devolucao}.")
                    return
            print(f"Este exemplar de '{livro.titulo}' não foi emprestado para {usuario}.")
        else:
            print(f"Livro '{livro.titulo}' não consta como emprestado.")

    def renovar_emprestimo(self, livro, usuario):
        if livro.titulo in self.__emprestimos:
            emprestimo_atual = None
            for emprestimo in self.__emprestimos[livro.titulo]["emprestimos"]:
                if emprestimo["Para o usuário"] == usuario:
                    emprestimo_atual = emprestimo
                    break
            if emprestimo_atual:
                if emprestimo_atual["renovacoes"] < 3:
                    emprestimo_atual["renovacoes"] += 1
                    print(f"Empréstimo do livro '{livro.titulo}' renovado por {usuario}. Total de renovações: {emprestimo_atual['renovacoes']}.")
                else:
                    print("Limite de renovações atingido.")
            else:
                print(f"O usuário {usuario} não possui empréstimo do livro '{livro.titulo}' para renovar.")
        else:
            print(f"Livro '{livro.titulo}' não está emprestado para ser renovado.")

    def registro_emprestimos(self):
        print('\n---------- Histórico de Empréstimos ------------\n')
        if self.__emprestimos:
            for titulo, info in self.__emprestimos.items():
                print(f"Livro: {titulo}")
                for emprestimo in info.get("emprestimos", []):
                    print(f"  Status: {emprestimo['status']}, Para o usuário: {emprestimo['Para o usuário']}, Na data: {emprestimo['Data']}, Renovações: {emprestimo['renovacoes']}")
                for devolucao in info.get("devolucoes", []):
                    print(f"  Status: {devolucao['status']}, Pelo usuário: {devolucao['Pelo usuário']}, Na data: {devolucao['Data']}")
        else:
            print("Não há empréstimos registrados na biblioteca.")
        print('\n------------------------------------------------\n')