import json
import os



class Manipulacao_Arquivo:
    def __init__(self,*caminho):
        self.caminnho = self.caminho_arquivo(*caminho)

    def caminho_arquivo(self,*caminho):
        return os.path.join(*caminho)

    def listar(self):
        with open(self.caminnho) as arquivo:
            return [json.loads(item) for item in arquivo]

    def migra_arquivo(self,*caminho):
        lista = self.listar()
        caminho_do_arquivo = self.caminho_arquivo(*caminho)

        with open(caminho_do_arquivo,'w') as arquivo:
            arquivo.close()
            with open(caminho_do_arquivo,'a') as arquivo_:
                [(json.dump(item, arquivo_),arquivo_.write('\n')) for item in lista]

    def conta_arquivo(self,*caminho):
        caminho_arq = self.caminho_arquivo(*caminho)
        with os.scandir(caminho_arq) as diretorio:
            return [item.name for item in diretorio]



 # \Users\johnr\PycharmProjects\exercicio\manipulacao_arquivo\teste_diretorio\usuarios\backup__lista_nomes_vogais.json

jh = Manipulacao_Arquivo('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','teste_diretorio','usuarios','backup__lista_nomes_vogais.json')

jh.migra_arquivo('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','teste_diretorio','backup_usuarios','backup_usuarios_vogais','backup_lista_nomes_vogais.json')

jh.conta_arquivo('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','teste_diretorio','backup_usuarios','backup_usuarios_vogais')

#
# for item in jh.listar():
#     print(item)







