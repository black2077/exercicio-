
import os
import json

def cria_caminho(diretorio):
    caminho = os.path.join('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','teste_diretorios_arquivos','produtos')
    caminho = caminho +'\\'+diretorio
    print(caminho)
    if os.path.exists(caminho):
        return caminho
    else:
        raise f'diretorio não existe ={diretorio}'


class arquivo:
    def __init__(self,caminho):
        self.caminho = cria_caminho(caminho)


    def lista_arquivos(self):
        with open(self.caminho) as arquivo:
            return [json.loads(item) for item in arquivo]


    def adiciona(self,dicio):
        with open(self.caminho,'a',encoding='UTF-8') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')


    def busca_indice(self,indice):
        lista = self.lista_arquivos()
        return lista[indice]


class produto:
    def __init__(self,nome,tipo,marca,modelo,preco):
        self.nome = nome
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.preco = preco


def verifica_diretorio():
    caminho = os.path.join('/Users','johnr','PycharmProjects','exercicio','manipulacao_arquivo','teste_diretorios_arquivos','produtos')
    if os.path.exists(caminho):
        return caminho
    else:
        raise f'diretorio não existe ={diretorio}'



hg = arquivo('eletrodomestico.json')
print(hg.busca_indice(0))


# vj = verifica_diretorio()
# print(vj)
#
# for item in os.listdir(vj):
#     print(item)



