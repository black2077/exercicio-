



import json

def quarda_arquivo(cls):
    def interna(*args,**kwargs):
        classe = cls(*args,**kwargs)
        with open("arquivo_lista.json", 'a') as arquivo:
            json.dump(classe.__dict__ , arquivo)
            arquivo.write('\n')
        return classe
    return interna


@quarda_arquivo
class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf



if __name__ == '__main__':
    while True:
        nome = input('digite seu __nome :')
        idade = input('digite sua idade :')
        cpf = input('digite seu __cpf :')
        Pessoa(nome,idade,cpf)
        print('=' * 40)





















