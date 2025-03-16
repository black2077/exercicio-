

def procura(valor,chave_1,chave_2):
    dicio = valor.__dict__

    match dicio:
        case {'__nome': _ , '__cpf' : _ } as arquivo:
            if dicio['__nome'] == chave_1 and dicio['__cpf'] == chave_2:
                print(arquivo)
            else:
                print('nao foi')
        case _:
            print('nao foi')


class Usuario:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


usu = Usuario('maria','5646454355','567654')

procura(usu,'maria','5646454355')

