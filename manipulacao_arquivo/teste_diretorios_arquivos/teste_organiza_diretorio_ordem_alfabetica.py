


from random import randint
import json
import os


def gerador(tamanho):
    return ''.join(str(randint(0,9)) for _ in range(tamanho))


class Arquivo:

    def listar(self,diretorio):
        with open(diretorio) as arquivo:
            return [json.loads(item) for item in arquivo]

    def adiciona(self,diretorio,dicio):
        with open(diretorio,'a') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')

    def caminho_diretorio(self,diretorio):
        caminho = os.path.join('/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo',
                                 'teste_diretorios_arquivos', 'usuarios') + '\\' + diretorio
        return caminho

    def filtra(self,dicio,*lista_de_diretorio):

        if dicio['nome'][0] in ('a','e','i','o','u') and lista_de_diretorio[0] == 'backup_lista_nomes_vogais.json':
            self.adiciona(self.caminho_diretorio(lista_de_diretorio[0]),dicio)

        if not dicio['nome'][0] in ('a','e','i','o','u') and lista_de_diretorio[1] == 'backup_lista_nomes_consoantes.json':
            self.adiciona(self.caminho_diretorio(lista_de_diretorio[1]),dicio)

    def organiza_diretorio(self,diretorio):
        caminho = self.caminho_diretorio(diretorio)
        lista = self.listar(caminho)
        lista.sort(key= lambda item : item['nome'])

        with open(caminho,'w') as arquivo_limpo:
            with open(caminho,'a') as arquivo:
                for item in lista:
                    json.dump(item,arquivo)
                    arquivo.write('\n')

    def mostra(self,caminho):
        caminho_arquivo = self.caminho_diretorio(caminho)
        for item in arq.listar(caminho_arquivo):
            print(item)


def caminho_diretorio(diretorio):
    caminho = os.path.join('/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo',
                           'teste_diretorios_arquivos', 'usuarios') + '\\' + diretorio
    return caminho



arq = Arquivo()
caminho = arq.caminho_diretorio('backup_lista_nomes_vogais.json')
print(caminho)
cont = 0
print('=' * 50)

while True:
    cont +=1
    nome = input('digite o nome :')
    dicio = {'nome': nome,'cpf':gerador(11),'senha':gerador(6)}

    arq.filtra(dicio, 'backup_lista_nomes_vogais.json', 'backup_lista_nomes_consoantes.json')
    if cont >= 5:
        cont = 0
        arq.organiza_diretorio('backup_lista_nomes_vogais.json')
        arq.organiza_diretorio('backup_lista_nomes_consoantes.json')
        break























