import json
from  time import sleep
import pathlib

class AlterarArquivoContext:
    def __init__(self,pasta,arquivo,backup_pasta):
        self.caminho = self.cria_arquivo(pasta,arquivo)
        self.backup_caminho = self.cria_arquivo(backup_pasta,arquivo)

    def cria_arquivo(self,pasta,arquivo):
        caminho = pathlib.Path(__file__).parent / pasta /arquivo
        return caminho


    def __enter__(self):
        # Abre o arquivo para leitura e le o conteúdo
        with open(self.caminho) as arquivo:
            self.conteudo = [json.loads(item) for item in arquivo.readlines()]

        return self


    def adiciona_arquivo(self,dicio):
        self.conteudo.append(dicio)


    def backup(self,pasta_backup,arquivo):
        with open(self.backup_caminho, 'w') as arqui:

            [(json.dump(item,arqui),arqui.write('\n')) for item in self.conteudo]


    def __exit__(self, exc_type, exc_val, exc_tb):
        # del self.conteudo
        print('foi')

# Exemplo de uso


def teste_1():
    pasta = 'arquivos'
    nome_do_arquivo = 'lista_test.json'
    backup_pasta = 'backup_arquivos'

    with AlterarArquivoContext(pasta,nome_do_arquivo,backup_pasta) as contexto:
        contexto.backup('backup_arquivos','lista_test.json')
        



while True:
    sleep(5)
    teste_1()























