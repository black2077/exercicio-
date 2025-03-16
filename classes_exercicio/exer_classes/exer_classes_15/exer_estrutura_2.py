





from abc import ABC,abstractmethod
import json


class Conta(ABC):
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    @abstractmethod
    def sacar(self,valor):...

    def deposita(self,valor):
        self.saldo += valor



class corrente_conta(Conta):
    def __init__(self,nome,cpf,senha,conta,agencia):
        super().__init__(nome,cpf,senha)
        self.conta = conta
        self.agencia = agencia
        self.limite = 300

    def sacar(self,valor):
        saldo_antigo = self.saldo
        valor_conta = self.saldo - valor
        self.saldo = 0

        if abs(valor_conta) < self.limite :
            self.saldo = valor_conta
        else:
            self.saldo = saldo_antigo
            print('seu limite foi atingido')



class usuario(corrente_conta):
    def __init__(self,nome, cpf, senha = '', conta = '', agencia = ''):
        super().__init__(nome, cpf, senha, conta, agencia)

    def cliente(self,cpf,senha,conta,agencia):
        with open('lista_contas.json') as arquivo:
            lista = [ ]
            for item in arquivo:
                lista.append(json.loads(item))



if __name__ == '__main__':

    p1 = usuario('54543545434' , 'marcela' , 'SFOFD2' ,'rt- 57845', '667432')
    p1.deposita(500)
    p1.sacar(1000)
    p1.cliente('54543545434' , 'SFOFD2' ,'rt- 57845', '667432')
    print(p1.__dict__)





