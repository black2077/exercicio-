








class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf



class usuario(Pessoa):
    def __init__(self,nome,cpf,senha,conta):
        super().__init__(nome,cpf)
        self.senha = senha
        self.conta = conta


p1 = usuario('ana','6567878365656','sefsf','f6567676')
print(p1.__dict__)























