
import json




class Conta:
    def __init__(self,nome,cpf,senha,saldo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo

    def deposito(self,valor):
        self.saldo += valor
        self.detalhes(f'seu deposito foi de :{valor}')

    def saque(self,valor):
        self.saldo -= valor
        self.detalhes(f' voce sacou : {valor}')

    def detalhes(self,txt):
        print(f'seu saldo atual :{self.saldo} |{txt}')



class Arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio


    def adicionar(self,dicio):
        with open(self.diretorio,'a') as arquivos:
            json.dump(dicio,arquivos)


    def editar_arquivo(self,novo_arquivo,antigo_arquivo):

        with open(self.diretorio) as arquivo:
            lista = [json.loads(item) for item in arquivo]
            for num,item in enumerate(lista):

                if self.busca(antigo_arquivo,item) and isinstance(antigo_arquivo,dict) and isinstance(novo_arquivo,dict):
                    lista[num] = novo_arquivo
                    with open(self.diretorio,'w') as arquivo_2:
                        [(json.dump(item,arquivo_2),arquivo_2.write('\n')) for item in lista]

    def busca(self,dicio,item):
        if dicio['nome'] == item['nome'] and dicio['cpf'] == item['cpf'] and dicio['senha'] == item['senha']:
            return True


    def carrega_arquivo(self,dicio):
        with open('lista.json') as arquivo:
            for item in arquivo:
                linha = json.loads(item)
                if self.busca(dicio,linha):
                    return linha


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass





class Banco:
    def __init__(self,cls :Conta,diretorio :str):
        self.classe = cls
        self.diretorio = diretorio


    def deposito(self,valor):
        with Arquivo(self.diretorio) as arq:
            dicio = arq.carrega_arquivo(self.classe.__dict__).values()
            novo_classe = Conta(*dicio)
            novo_classe.deposito(valor)
            arq.editar_arquivo(novo_classe.__dict__,self.classe.__dict__)


    def sacar(self,valor):
        with Arquivo(self.diretorio) as arq:
            dicio = arq.carrega_arquivo(self.classe.__dict__).values()
            novo_classe = Conta(*dicio)
            novo_classe.saque(valor)
            arq.editar_arquivo(novo_classe.__dict__,self.classe.__dict__)




conta = Conta('ana lima','12345','12345',0)


ban = Banco(conta,'fsfsdfse')

ban.deposito(105)
# ban.sacar(110)


dicio = ban.__dict__
print(dicio['classe'].__dict__)








