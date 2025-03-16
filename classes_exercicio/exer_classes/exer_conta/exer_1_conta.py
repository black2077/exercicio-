
from abc import ABC,abstractmethod




class Conta(ABC):
    def __init__(self,agencia,conta,saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self,valor):...


    def depositar(self,valor):
        self.saldo += valor
        self.detalhes(f'depositou = {valor}')

    def detalhes(self,txt):
        print(f'seu saldo = {self.saldo} | {txt}')


class Conta_poupanca(Conta):
    def sacar(self,valor):
        valor_saldo = self.saldo - valor

        if valor_saldo >= 0:
            self.saldo -= valor
            self.detalhes(f'sacou {valor}')
            return self.saldo

        self.detalhes(f'seu saque de {valor} não foi posivel !')


class Conta_corrente(Conta):
    def __init__(self,agencia,conta,saldo,limite):
        super().__init__(agencia,conta,saldo)
        self.limite = -limite

    def sacar(self,valor):
        saca = self.saldo - valor

        if saca >= self.saldo or saca >= self.limite :
            self.saldo = saca
            self.limite = saca - self.limite
            return

        self.detalhes(f'saldo insufiente ! voce tentou saca = {valor}')



if __name__ == '__main__':

    cla = Conta_corrente('32234','3243',500,150)
    # cla.depositar(0)
    cla.sacar(750)

    # cla.sacar(130)

    print(cla.__dict__)










