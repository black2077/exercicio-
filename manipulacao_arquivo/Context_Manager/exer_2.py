import json
import os.path


class Arquivo:
    def __init__(self,*caminho_pasta):
        self.caminho = self.cria_caminho(*caminho_pasta)

    def __enter__(self):
        return self

    def cria_caminho(self,*pasta_caminho):
        return os.path.join(*pasta_caminho)

    def lista_diretorios(self,caminho):
        with os.scandir(caminho) as arquivo:
            return {f'{num}': item.name for num,item in enumerate(arquivo)}

    def lista_arquivos(self,diretorio):
        self.caminho_arquivo = self.caminho[:] +'\\'+ diretorio
        with open(self.caminho_arquivo) as arquivo:
            lista = [json.loads(item) for item in arquivo]
            self.tamanho = len(lista)
            return lista

    def crie_arquivo(self,subpasta,nome_arquivo):
        caminho = self.cria_caminho('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','Context_Manager',subpasta) + '\\' +nome_arquivo
        with open(caminho,'w') as arquivo:
            arquivo.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('foi')
        print(self.__dict__)

with Arquivo('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','Context_Manager','lista') as arquivo:
    print(arquivo.__dict__)



































