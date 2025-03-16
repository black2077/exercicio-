

class Cliente:
    def __init__(self,nome,cpf,senha,saldo,conta,agencia,limite):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo
        self.conta = conta
        self.agencia = agencia
        self.limite = limite

    def deposito(self,valor):
        self.saldo += valor

    def saque(self,valor):
        if (self.saldo - valor) >= 0:
            self.saldo -= valor
        else:
            self.saldo
            print('não foi')




