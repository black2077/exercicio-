

import csv
import pathlib


class Arquivo:
    def __init__(self):
        self.caminho = self.cria_caminho()

    def cria_caminho(self,nome_arquivo = ''):
        return pathlib.Path(__file__).parent / nome_arquivo

    def cria_arquivo(self,nome_arquivo):
        caminho = self.cria_caminho(nome_arquivo)
        with open(caminho,'w') as arquivo:
            pass

    def adiciona(self, caminho,item):
        with open(caminho,'a') as arquivo:
            arquivo.write(item)
            arquivo.write(',')

    def lista_arquivo(self,arquivo):
        with open(caminho) as arquivo:
            return [[item.rstrip(',')] for item in arquivo]

    def lista_linha(self,caminho):
        with open(caminho) as arquivo:
            return next(arquivo).replace('\n','').rsplit(',')

    def teste(self,caminho):
        with open(caminho) as arquivo:
            return {f'{num}':list(item.replace('\n','').rsplit(',')) for num,item in enumerate(arquivo)}

    def teste_2(self,caminho):
        with open(caminho, newline='') as csvfile:
            return {f'{num}' : item  for num,item in enumerate(csv.reader(csvfile, delimiter=','))}

    def teste_dicio(self,caminho):
        with open(caminho) as arquivo:
            return [item for item in csv.DictReader(arquivo)]


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



with Arquivo() as arquivo:
    caminho = 'arquivo/nome.csv'
    # arquivo.cria_arquivo(caminho)
    # arquivo.adiciona(caminho,'fafada')
    # lista_2 = arquivo.teste_2(caminho)
    #
    # for num,item in lista_2.items():
    #     print(num,item)
    teste = arquivo.teste_dicio(caminho)
    print(teste)











