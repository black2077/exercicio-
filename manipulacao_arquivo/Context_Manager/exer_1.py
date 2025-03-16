

import json


class Arquivo:
    def __init__(self,caminho_arquivo ,dicio):
        self.caminho_arquivo = caminho_arquivo
        self.dicio = dicio

    def __enter__(self):
        self.arquivo = open(self.caminho_arquivo,'r',encoding= 'utf 8')
        self.lista = [json.loads(item) for item in self.arquivo]
        self.arquivo.close()
        print(self.lista)

    def substitue_arquivo(self,novo_arquivo):
        with open(self.caminho_arquivo,'a') as arquivo:
            json.dump(novo_arquivo,arquivo)
            arquivo.write('\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.substitue_arquivo(self.dicio)





dicio = {'__nome': 'mariana','__cpf' : '64565645654','__senha' : '565464'}
with Arquivo('lista_teste.json',dicio):
    pass






















