

import json
import os
from datetime import datetime



class Gerencia_Arquivo:
    def __init__(self,diretorio,nome_arquivo):
        self.caminho = self.caminho_arquivo(diretorio, nome_arquivo)
        print(self.caminho)
    def caminho_arquivo(self,diretorio, nome_arquivo='', modificador=''):
        if nome_arquivo == '' and modificador == '':
            caminho = os.path.join('/Users', 'johnr', 'PycharmProjects', 'exercicio',
                                   'manipulacao_arquivo', 'teste_diretorios_arquivos', diretorio)
        else:
            caminho = os.path.join('/Users', 'johnr', 'PycharmProjects', 'exercicio',
                                   'manipulacao_arquivo', 'teste_diretorios_arquivos',
                                   diretorio) + '\\'+ nome_arquivo + modificador

        return caminho

    def medidor_de_diretorio(self,pasta):
        itens = os.listdir(pasta)
        contador = 0

        for item in itens:
            if os.path.isfile(self.caminho_arquivo(pasta,item)):
                contador += 1

        return contador

    def listar(self):
        with open(self.caminho) as arquivo:
            return [json.loads(item) for item in arquivo]

    def delete_arquivo(self,diretorio,nome_arquivo):
        os.remove(self.caminho_arquivo(diretorio,nome_arquivo))

    def backup(self,diretorio,nome_arquivo):
        lista = self.listar()
        caminho_backup = self.caminho_arquivo(diretorio, nome_arquivo)

        with open(caminho_backup,'w') as arquivo:
            arquivo.close()

        with open(caminho_backup,'a') as arquivo:
            for item in lista:
                json.dump(item,arquivo)
                arquivo.write('\n')

    def backup_automatico(self,diretorio,nome_arquivo):
        caminho = self.caminho_arquivo(diretorio)
        tamanho = self.medidor_de_diretorio(caminho)

        if tamanho <= 10 :
            listado = self.lista_arquivos_diretorio(caminho)
            pagar = listado.pop()
            self.delete_arquivo(caminho,pagar)

            data = f"{tamanho}_" + nome_arquivo
            self.backup(diretorio, data)

        else:
            data = f"{tamanho}_" + nome_arquivo
            self.backup(diretorio, data)

    def lista_arquivos_diretorio(self,pasta):
        return os.listdir(pasta)


gf = Gerencia_Arquivo('usuarios','backup__lista_nomes_vogais.json')

gf.backup_automatico('usuarios_backup',"backup_lista_nomes_vogais.json")

# gf.delete_arquivo('usuarios_backup','(1)_backup_lista_nomes_vogais.json')
# print(gf.lista_arquivos_diretorio('usuarios_backup'))

print(gf.__dict__)
