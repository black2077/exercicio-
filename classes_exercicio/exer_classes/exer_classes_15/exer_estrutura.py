




from abc import ABC,abstractmethod
import json


class Conta(ABC):
    def __init__(self,nome,cpf,saldo = 0):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo


    @abstractmethod
    def sacar(self):...

    def depositar(self,valor):
        self.saldo += valor



class Cliente_conta_corrente(Conta):
    def __init__(self,conta,agencia):
        super().__init__(nome,cpf,saldo)
        self.saldo = saldo
        self.conta = conta
        self.agencia = agencia
        self.limite = 250


    def sacar(self,valor):
        saldo_antigo = self.saldo
        valor_conta = self.saldo - valor
        self.saldo = 0

        if abs(valor_conta) < self.limite :
            self.saldo = valor_conta
        else:
            self.saldo = saldo_antigo


class Cliente_conta_poupanca(Conta):
    def __init__(self,nome,cpf,senha,conta,agencia):
        super().__init__(nome,cpf)
        self.conta = conta
        self.agencia = agencia
        self.senha = senha

    def sacar(self,valor):
        if self.saldo > valor :
            self.saldo = self.saldo - valor
        else:
            print('__saldo insuficiente !!!! seu __saldo atual :',self.saldo)


class usuario(Cliente_conta_poupanca):
    with open('lista_contas.json') as arquivo:...

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def cliente(self,senha,conta,agencia):
        super().__init__(senha, conta, agencia)


        print(f'em nome : {self.nome}  | __saldo : {self.saldo} ')
        print(f'numero da conta {self.conta} |')

    def novo_cliente(self):...


    def rede_agencia(self):...



if __name__ == '__main__':
    p1 = usuario('ana','54554587655')
    p1.cliente('4ttyypop','s8-43432','rj-dc-xerem -345654')






    #
    # print('=======================')
    # p1 = Cliente_conta_corrente('ana','4838438483','32342','DC-4332','ADADRR')
    # print('usuario corrente')
    # p1.depositar(150)
    # print(p1.__saldo)
    # p1.sacar(293)
    # print(p1.__saldo)
    #
    # print('=======================')
    # print('usuario poupança')
    #
    # p2 = Cliente_conta_poupanca('ana','4838438483','32342','DC-4332','ADADRR')
    # p2.depositar(200)
    # print(p2.__saldo)
    # p2.sacar(195)
    # p2.sacar(2)
    # print(p2.__saldo)
    # p
















