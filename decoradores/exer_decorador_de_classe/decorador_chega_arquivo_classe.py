


import json


def checa_classe_arquivo(cls):
    with open('arquivo_lista.json') as arquivo:
        lista = list([json.loads(item) for item in arquivo])

    def interna(*args,**kwargs):
        classe = cls(*args,**kwargs)
        if classe.__dict__ in lista:
            return classe,True

    return interna


@checa_classe_arquivo
class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def __call__(self):
        return f'{self.nome} | {self.cpf}'




p1 = Pessoa('thiago','79858853432')


print(p1[0].__dict__,p1[1])





# while True :
#     __lista = []
#     __nome = input('digite seu __nome :')
#     __cpf = input('digite seu __cpf :')
#
#     __lista.append(Pessoa(__nome,__cpf))
#     print(__lista)
















