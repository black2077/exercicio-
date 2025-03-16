import json


class banco_de_dados:
    def __init__(self,diretorio):
        self.diretorio = diretorio

    def carrego_arquivos(self):
        with open(self.diretorio) as arquivo:
            return [json.loads(item) for item in arquivo]


    def procura(self,acesso,*args):
        lista = self.carrego_arquivos()
        for num,item in enumerate(lista):
            if item['Cliente']['nome'] == args[0] and item['Cliente']['cpf'] == args[1]:
                self.indice, self.arquivo= num,item[acesso].values()


    def __call__(self,cls):
        def interna(*args):
            self.procura(cls.__name__, *args)
            if cls.__name__ == 'Cliente':
                resultado = cls(*self.arquivo)

            if cls.__name__ == 'Dados_Bancarios':
                lista = self.carrego_arquivos()
                indice = args[0]
                valores = lista[indice][cls.__name__].values()
                resultado = cls(indice,*valores)

            return resultado
        return interna


@banco_de_dados('banco_de_dados_cliente.json')
class Cliente:
    def __init__(self,nome,cpf,senha,saldo=0,conta = ''):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo
        self.conta = conta


@banco_de_dados('banco_de_dados_cliente.json')
class Dados_Bancarios:
    def __init__(self,indice,banco='',chave=''):
        self.indice = indice
        self.banco = banco
        self.chave = chave



dad = Cliente('ana','987654321','123456')
print(dad.__dict__)

dte = Dados_Bancarios(0)
print(dte.__dict__)


























