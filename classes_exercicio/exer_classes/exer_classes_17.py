
from datetime import datetime


def marca_acesso(fun):

    def interna(*args,**kwargs):
        info = datetime.now().strftime('%d/%m/%Y | %H :%M ')
        resultado = fun(*args,**kwargs)

        return [resultado.__dict__,info]

    return interna


@marca_acesso
class Usuario:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


m = Usuario('ana','5435354353')


print(m)














