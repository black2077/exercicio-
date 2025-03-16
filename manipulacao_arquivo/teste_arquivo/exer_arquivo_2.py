




import sys
import time
import json


def monitorador_desempenho(func):
    dicio = {}
    def interna(*args):
        inicio = time.time()
        resultado = func(*args)
        fim = time.time()
        dicio['tempo de execução'] = inicio - fim
        dicio['__nome do objeto'] = func.__name__
        dicio['uso de memoria'] = sys.getsizeof(resultado)
        return resultado,dicio
    return interna


@monitorador_desempenho
class edita_arquivo:
    with open('arquivos/lista_test.json') as arquivo:
        __lista = [json.loads(item) for item in arquivo]

    def __init__(self,classe_dict):
        self.classe_dict = classe_dict
        self.busca_arquivo()
        self.editor_arquivo()

    def busca_arquivo(self):
        for item in self.__lista:
            if self.classe_dict == item :
                return self.classe_dict

    def adiciona_arquivo(self,dicio):
        with open('arquivos/lista_test.json', 'a') as arquivo:
            json.dump(dicio ,arquivo)
            arquivo.write('\n')

    def editor_arquivo(self):
        with open('arquivos/lista_test.json', 'w') as arquivo:
            lista = [dicio if self.busca_arquivo() == dicio else self.adiciona_arquivo(dicio) for dicio in self.__lista ]




class Usuario:
    def __init__(self,nome,cpf,data_nas,RG):
        self.nome = nome
        self.cpf = cpf
        self.data_nas = data_nas
        self.RG = RG

    def informacoes_contato(self):
        self.telefone = telefone
        self.email = email

    def informacoes_financeira(self):
        self.saldo = 0
        self.limite = 900













