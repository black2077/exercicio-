import json
import os.path
import shutil


class Gerenciador_Diretorio:
    def __init__(self,lista_caminhos):
        self.caminho = self.cria_caminho(lista_caminhos)

    def __enter__(self):
        return self

    def cria_caminho(self,lista):
        return os.path.join(*lista)

    def lista_arquivo(self,nome_arquivo):
        with open(nome_arquivo) as arquivo:
            return [json.loads(item) for item in arquivo]

    def lista_diretorio(self,pasta):
        return os.listdir(pasta)

    def medidor_arquivos(self,caminho):
        caminho_arquivo = self.caminho[:] + '\\' + caminho
        return len(self.lista_arquivo(caminho_arquivo))

    def busca_item(self,cpf,senha,diretorio):
        caminho = self.caminho[:]+ '\\'+diretorio
        contador =0

        with open(caminho) as arquivo:
            try:
                while True:
                    item = json.loads(arquivo.readline())

                    if item['cpf']== cpf   and item['senha'] == senha:
                        return {f'{contador}': item}
                    # print(item)
                    contador +=1

            except json.decoder.JSONDecodeError:
                print('foi')

    def mover(self,arquivo,pasta_backup):
        os.rename(arquivo,pasta_backup)

    def backup(self,arquivo,pasta_backup):
        shutil.copy2(arquivo,pasta_backup)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print()


# \Users\johnr\PycharmProjects\exercicio\manipulacao_arquivo\Context_Manager\lista

caminhos = ['/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','Context_Manager']

with Gerenciador_Diretorio(caminhos) as arquivo:
    caminho = arquivo.caminho[:]+'\\'+'lista\lista_teste.json'
    arquivo.backup(caminho,'lista_backup\lista_teste.json')













