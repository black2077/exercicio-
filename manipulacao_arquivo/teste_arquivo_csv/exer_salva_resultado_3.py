


import csv
import pathlib


class Arquivo:
    def __init__(self,pasta,arquivo):
        self.caminho = self.cria_caminho(pasta,arquivo)

    def cria_caminho(self,pasta,arquivo):
        caminho = pathlib.Path(__file__).parent / pasta / arquivo
        return caminho

    def listo_arquivo(self):
        with open(self.caminho) as arquivo:
            return  list(csv.reader(arquivo))

    def busco(self,dicio):
        lista = self.listo_arquivo()
        if dicio['conta'] == lista[1][0] and dicio['agencia'] == lista[1][1]:
            self.arquivo = lista[1]

            return True
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



def memoria_salva(pasta,arquivo):
    def memoria(cls):
        def interna(*args):
            classe = cls(*args)

            with Arquivo(pasta,arquivo) as arquivo_csv:
                # print(arquivo_csv.__dict__)
                # arquivo_csv.listo_arquivo()
                if arquivo_csv.busco(classe.__dict__):
                    return classe
                else:
                    lista = arquivo_csv.listo_arquivo()
                    novo_lista = list(args)
                    novo_lista.extend(lista[1])
                    return cls(*novo_lista)

        return interna
    return memoria



@memoria_salva('arquivo','conta.csv')
class Usuario:
    def __init__(self,nome,cpf,senha,conta =None,agencia=None):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.conta = conta
        self.agencia = agencia


usu = Usuario('ana','645645646545','6545645')


print(usu.__dict__)




















