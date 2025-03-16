



from abc import ABC,abstractmethod

class conta(ABC):
    def __init__(self,conta,agencia,saldo):
        self.conta = conta
        self.agencia = conta
        self.saldo = saldo

    @abstractmethod
    def conta_poupanca(self):...

    @abstractmethod
    def conta_corrente(self):...



class Pessoa(conta):
    def __init__(self, cpf):
        self._cpf = cpf


    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self,conta):
        self._conta


    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(self._cpf, str):
            return self._cpf


    def conta_poupanca(self):...
        





    def conta_corrente(self):...




p1 = Pessoa('Ana','H')

p1.conta = 'ana55'

print(p1.__dict__)





















