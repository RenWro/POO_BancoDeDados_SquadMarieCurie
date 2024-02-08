class Usuario:
    def __init__(self, nome, sobrenome, telefone, nacionalidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    def __repr__(self):
        return f"{self.nome} {self.sobrenome}"
    
    def __eq__(self, other):
        return self.nome == other.nome and self.sobrenome == other.sobrenome
    
    def __hash__(self):
        return hash(self.nome) + hash(self.sobrenome)
    
    def __lt__(self, other):
        return self.nome < other.nome and self.sobrenome < other.sobrenome
    
    def __le__(self, other):
        return self.nome <= other.nome and self.sobrenome <= other.sobrenome

    def __gt__(self, other):
        return self.nome > other.nome and self.sobrenome > other.sobrenome
    

    