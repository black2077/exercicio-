

import json


class registra_atividade:
    def __init__(self,conta,registra):
        self.usuario = conta
        self.registra = registra
        self.usuario = self.procuro()


    def arquivos(self,diretorio):
        with open(diretorio) as arquivo:
            return [json.loads(item) for item in arquivo]

    def procuro(self):
        self.lista = self.arquivos('atividades.json')
        for num,item in enumerate(self.lista):
            if self.usuario['nome'] == item['conta']['nome'] and self.usuario['cpf'] == item['conta']['cpf']:
                self.indice = num
                return item

    def atividade_conta(self,func,valor):
        self.usuario[f'{func.__name__}'].append(valor)
        self.lista[self.indice] = self.usuario

        def adiciona(item):
            with open('atividades.json','a') as arquivo:
                json.dump(item,arquivo)
                arquivo.write('\n')

        with open('atividades.json','w') as arquivo:
            [adiciona(item) for item in self.lista]



class Banco:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.saldo = 0
        self.cpf = cpf
        global dicio

    def deposito(self,valor):
        self.saldo += valor
        registra_atividade(self.__dict__, 'atividade.json').atividade_conta(self.deposito, valor)


class poupanca_banco(Banco):
    def __init__(self,nome,cpf):
        super().__init__(nome,cpf)


    def saque(self,valor):
        self.saldo -= valor
        registra_atividade(self.__dict__,'atividade.json').atividade_conta(self.saque,valor)



pessoa = poupanca_banco('luana','643535345345')
pessoa.deposito(646)
pessoa.deposito(5)
pessoa.saque(56)

# usuario = pessoa.__dict__
#
# print(usuario)
# print(dicio)
#
#



