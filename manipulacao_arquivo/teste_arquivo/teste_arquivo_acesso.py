

import json
import time
import psutil
import os

tempo = 0

def monitora_velocidade_memoria(func):
    def wrapper(*args, **kwargs):
        global tempo
        t1 = time.time()
        process = psutil.Process(os.getpid())
        mem1 = process.memory_info().rss / 1024 / 1024
        result = func(*args, **kwargs)
        t2 = time.time()

        process = psutil.Process(os.getpid())
        mem2 = process.memory_info().rss / 1024 / 1024
        tempo = t2-t1

        print(f"A função {func.__name__}   levou {t2 - t1} segundos para executar e usou {mem2 - mem1} MB de memória.")
        return result
    return wrapper


class Acesso_Cliente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


class Arquivo:
    def __init__(self,diretorio):
        self.diretorio : str = diretorio


    def __arquivos(self):
        with open(self.diretorio) as arquivo:
            return  [json.loads(item) for item in arquivo]


    def procura(self,usuario):
        lista = self.__arquivos()
        for num,item in enumerate(lista):
            if usuario['nome'] == item['nome'] and usuario['cpf'] == item['cpf'] and usuario['senha'] == item['senha']:
               self.indice,self.arquivo = num,item
               return True

    def edita_arquivo(self,novo_arquivo):
        with open(self.diretorio,'w') as arquivo:
            self.arquivos = self.__arquivos()
            self.arquivos[self.indice] = novo_arquivo
            lista = [json.dumps(item) +'\n' for item in self.__arquivos]
            arquivo.writelines(lista)
        del self.arquivos,self.indice



class Cliente:
    def __init__(self,nome,cpf,senha,saldo):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo

    def saque(self,valor):
        self.saldo -= valor


    def deposito(self,valor):
        self.saldo += valor


class ligacao_banco_dados(Arquivo):
    def __init__(self,diretorio,cls_acesso):
        super().__init__(diretorio)
        self.cls = cls_acesso
        arquivo_ligacao = Arquivo(diretorio)
        if arquivo_ligacao.procura(self.cls):
            self.lista_info = arquivo_ligacao.arquivo

    def acesso(self):
        lista = [item for item in self.lista_info.values()]
        del self.lista_info
        return lista



if __name__ == '__main__':

    cliente_ace = Acesso_Cliente('ana','45435345543','432422')
    base_cliente = ligacao_banco_dados('lista_clientes.json', cliente_ace.__dict__)
    # =========
    # conta = Cliente(*base_cliente.acesso())
    # conta.deposito(900)
    # conta.saque(1700)
    # =========
    base_cliente.edita_arquivo(cliente_ace.__dict__)


    print(conta.__dict__)
    print(base_cliente.__dict__)
