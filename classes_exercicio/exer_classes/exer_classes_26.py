








class Cliente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha





class cliente_arquivo:
    def __init__(self,usuario):
        self.usuario = usuario
    
    def __get__(self,obj,objtype= None):
        return self.usuario

    def __delete__(self):
        del self.usuario['senha']



usu = Cliente('ANA','354353354','FSFSEDA')

arq_usu = cliente_arquivo(usu)

print(usu.__dict__)
        
print(arq_usu.__dict__)
arq_usu.__delete__
print(arq_usu.usuario.__dict__)











































