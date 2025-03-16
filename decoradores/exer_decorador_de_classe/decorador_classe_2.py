

import json

class usuario:
    def __init__(self,nome_arquivo):
        self.arquivo_nome = nome_arquivo

    def checa_arquivo(self):
        with open(self.arquivo_nome) as arquivo:
            return [json.loads(item) for item in arquivo]


    def __call__(self,cls):
        def interna(*args):
            classe = cls(*args).__dict__
            if classe in self.checa_arquivo():
                return classe
            print('usuario nao existe')

        return interna


@usuario('arquivo_lista.json')
class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


#
# p1 = Pessoa('ana','35456634432')
# print(p1)

# ========================================================================================

def filtro_cpf(func):
    def interna(*args,**kwargs):
        while True:
            resultado = func(*args,**kwargs)
            if len(str(resultado)) == 11 and str(resultado).isnumeric():
                return resultado
    return interna

@filtro_cpf
def pega_cpf():
    resultado = input('digite seu __cpf :')
    return resultado


# pre = pega_cpf()
# print(pre)

# =======================================================================================
class adiciona_arquivo:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self._arquivos = None

    @property
    def arquivos(self):
       return self.arquivos

    @arquivos.setter
    def arquivos(self):
        with open(self.nome_arquivo) as arquivo:
            self.arquivos = [json.loads(item) for item in arquivo]

    def adiciona(self,dicio):
        with open(self.nome_arquivo,'a') as arquivo_o:
            json.dump(dicio,arquivo_o)

    def __call__(self,cls):
        def interna(*args):
            resultado = cls(*args).__dict__
            print(resultado)
            if resultado in self.arquivos:
                print('usuario ja existe')
            else:
                return self.adiciona(resultado)

            return resultado
        return interna



@adiciona_arquivo('arquivo_lista.json')
class Pessoa:
    def __init__(self,nome,cpf,rg,data):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data = data


p1 = Pessoa('ana','44344542334','6432343434-21','09/08/98')


# ===================================================================================




























