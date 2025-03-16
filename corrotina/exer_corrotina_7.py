import json
import pathlib
import asyncio
import os

class Arquivo:
    def __init__(self,caminho = ''):
        self.caminho = self.cria_caminho(caminho)

    def cria_caminho(self,caminho):
        novo_caminho = pathlib.Path(__file__).parent / caminho
        return novo_caminho

    def cria_arquivo(self,pasta,nome_arquivo):
        caminho = self.caminho / pasta / nome_arquivo
        # print(caminho)
        with open(caminho,'w') as arquivo:
            arquivo.close()

    def cria_diretorio(self,nome):
        caminho = self.caminho.parent / nome
        if not os.path.exists(caminho):
            os.mkdir(caminho)

    def lista_diretoio(self,pasta=''):
        novo = self.caminho / pasta
        return {'tamanho' : len(os.listdir(novo)), 'arquivos' : os.listdir(novo),'diretorio': pasta}

    def lista_arquivo(self,nome_arquivo):

        with open(nome_arquivo) as arquivo:
            for item in arquivo:
                dicio = json.loads(item)
                yield dicio

    def adiciona(self,nome_arquivo,item):
        with open(nome_arquivo,'a') as arquivo:
            json.dump(item,arquivo)
            arquivo.write('\n')

    def busco_arquivo_nome(self,dicio,pasta,diretorio):
        caminho = arquivo.caminho / pasta /diretorio
        info = []

        for nun,item in enumerate(self.lista_arquivo(caminho)):
            dados = json.loads(item)
            if dicio['nome'] == dados['nome']:
                info.append({f'{nun}':dados})
                return info

    def busco_indice(self,indice,pasta,diretorio):
        novo = self.caminho / pasta / diretorio
        for num,item in enumerate(self.lista_arquivo(novo)):
            if indice == num:
                return item

    def altera_arquivo(self,indice,novo_arquivo,pasta,diretorio):
        novo_caminho = self.caminho / pasta / diretorio
        lista = [item for item in self.lista_arquivo(novo_caminho)]
        lista[indice] = novo_arquivo

        with open(novo_caminho,'w') as arquivo:
            [(json.dump(item,arquivo),arquivo.write('\n')) for item in lista]

    def verifica_existencia(self,nome_arquivo):
        if os.path.exists(nome_arquivo):
            return True
        else:
            return False

    def excluir(self,nome_arquivo):
        caminho = self.caminho / nome_arquivo
        if self.verifica_existencia(caminho):
            os.remove(caminho)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



async def arquivo_as(pasta = '',arquivo =''):

    with Arquivo() as arquivo_s:
        novo_caminho = arquivo_s.caminho / pasta / arquivo
        arquivo_s.cria_arquivo('backup_arquivos',arquivo)



async def arquivo_backup(pasta ='',nova_pasta = '',arquivo =''):
    with Arquivo() as arquivo_back:

        novo = arquivo_back.caminho / pasta / arquivo
        novo_arq = arquivo_back.caminho / nova_pasta / arquivo

        lista = [item for item in arquivo_back.lista_arquivo(novo)]
        [arquivo_back.adiciona(novo_arq,item) for item in lista]




async def executa():
    pasta = 'arquivos'
    arquivo = 'lista_1_backup.json'

    await arquivo_as(pasta,arquivo)
    await arquivo_backup('arquivos','backup_arquivos' ,arquivo)

    print('fim')

if __name__ == '__main__':

    asyncio.run(executa())






























