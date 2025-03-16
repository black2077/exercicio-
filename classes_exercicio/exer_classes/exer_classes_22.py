from abc import ABC,abstractmethod
from datetime import datetime

def acesso_cliente(classe):
    class Cliente(classe):
        tempo = datetime.now().strftime('%d/%m/%Y %H:%M')

        def acesso(self):
            self.acesso_conta = False

        def __repr__(self):
            return str(self.__dict__)

    return Cliente

#==========================================
@acesso_cliente
class ContaPoupanca:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
# =========================================
@acesso_cliente
class ContaCorrente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def banco(self, conta, agencia):
        self.conta = conta
        self.agencia = agencia


cli = ContaCorrente('ana','56563454353','554523')
cli.banco('6545345','64543')
cli.acesso()


print(cli)





















