
from abc import ABC,abstractmethod


class Arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio

    def __call__(self,cls):
        def interna(*args,**kwargs):
            resultado = cls(*args,**kwargs)
            rer = resultado.__dict__
            del rer['saldo'],rer['usuario'],rer['agencia']

            return resultado
        return interna


class Banco(ABC):
    def __init__(self,nome,cpf,senha,saldo:int):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo

    @abstractmethod
    def sacar(self):...

    def depositar(self,valor):
        return self.saldo + valor

# ===========================================================================
@Arquivo('56465')
class Banco_Corrente(Banco):
    def __init__(self,nome,cpf,senha,saldo,conta,agencia):
        super().__init__(nome,cpf,senha,saldo)
        self.conta = conta
        self.agencia = agencia


    def sacar(self,valor):
        saldo_antigo = self.saldo
        valor_conta = self.saldo - valor
        if abs(valor_conta) <= self.limite or self.saldo > valor:
            return self.saldo - valor

        else:
            self.saldo = saldo_antigo
            return self.saldo
            print('seu limite foi atingido')


lk = Banco_Corrente('ana','5676577567','567657',100,'54353','546456')






















