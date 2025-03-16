



import json


class organiza_arquivo:
    def __init__(self,nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.arquivos = None

    def converti_arquivo(self):
        with open(self.nome_arquivo) as arquivo:
            return [json.loads(item) for item in arquivo]

    def procuro_arquivo(self,dicio):
        for item in self.arquivos:
            if dicio['__nome'] == item['__nome'] and dicio['__cpf'] in item['__cpf']:
                return True

    def __call__(self,cls):
        self.arquivos = self.converti_arquivo()
        def interna(*args):
            resultado: dict = cls(*args).__dict__
            if self.procuro_arquivo(resultado):
                print('CONTA JA EXISTE')

            return resultado
        return interna


@organiza_arquivo('arquivo_lista.json')
class Cadastro:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf



pa = Cadastro('lucas','9765656456')
# ,'anabts10@gmail'
print(pa)






























