
import json



class Gerenciador_Diretorio:
    def __init__(self,lista_caminho):
        self.diretorio = self.cria_caminho(lista_caminho)

    def __enter__(self):
        return self

    def cria_caminho(self,lista):
        return ''.join(item + '\\' for item in lista)[:-1]

    def lista_arquivo(self,caminho):
        with open(caminho) as arquivo:
            return [json.loads(item) for item in arquivo]

    def cria_arquivo(self,diretorio_destino,nome_arquivo):

        novo_caminho = self.diretorio + '\\' + nome_arquivo
        with open(novo_caminho,'w') as arquivo:
            pass

    def cria_backup(self,destino,diretorio_arquivo):

        novo_caminho = self.diretorio[:] + '\\' + diretorio_destino
        atual = self.diretorio[:] + '\\' + diretorio_arquivo

        with open(novo_caminho,'w') as arquivo ,open(atual) as arquivos_lidos:
            lista = [item for item in arquivos_lidos]
            arquivo.writelines(lista)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print()



lista = ['/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','Context_Manager']


with Gerenciador_Diretorio(lista) as arquivo:
    caminho_arq = arquivo.diretorio
    # print(caminho_arq)
    # print(arquivo.lista_arquivo(caminho_arq))
    # arquivo.cria_arquivo(caminho_arq, 'lista_backup\\lista_teste_2.json')
    # arquivo.cria_backup('lista_backup\\lista_r.json','lista\\lista_teste_1.json')
























