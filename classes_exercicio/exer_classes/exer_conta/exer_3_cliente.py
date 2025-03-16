

from exer_2_pessoa import Pessoa
from exer_1_conta import Conta_poupanca,Conta_corrente





# class cliente_met(exer_2_pessoa.Pessoa):
#     def __init__(self,nome,cpf,senha):
#         super().__init__(nome,cpf,senha)
#
#     def tipo_conta(self,cls):
#         self.conta = cls


class cliente_poupanca(Pessoa,Conta_poupanca):
    def __init__(self,nome,cpf,senha,agencia,conta,saldo=0):
        Pessoa.__init__(self,nome,cpf,senha)
        Conta_poupanca.__init__(self,agencia,conta,saldo)


class cliente_corrente(Pessoa,Conta_corrente):
    def __init__(self,nome,cpf,senha,agencia,conta,saldo=0,limite=0):
        Pessoa.__init__(self,nome,cpf,senha)
        Conta_corrente.__init__(self,agencia,conta,saldo,limite)



if __name__ == '__main__':
    df = cliente_poupanca('luana', '435345345', '5233423', '6524324', '45543', 90)
    print(df.__dict__)
    # ======================================================
    cd = cliente_corrente('ana','3423423','4242','54334','645646',4,300)
    print(cd.__dict__)
















