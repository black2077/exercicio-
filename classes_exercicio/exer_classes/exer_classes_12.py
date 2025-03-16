


class AcessoCliente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


class DecoradorAcesso:
    def __init__(self,dicio_classe):
        self.classe_acesso = dicio_classe.__dict__

    def procura(self,classe):
        conta = {'__nome': 'ana', '__cpf': '65323443243', '__senha': '453242'}
        if self.classe_acesso['__nome'] == conta['__nome'] and self.classe_acesso['__cpf'] == conta['__cpf'] and self.classe_acesso['__senha'] == conta['__senha']:
            return True

    def __call__(self,classe):
        def interna(*args, **kwargs):
            resultado = classe(*args,**kwargs)
            if self.procura(resultado):
                return resultado
        return interna


clien = AcessoCliente('ana','65323443243','453242')

@DecoradorAcesso(clien)
class Cliente:
    def __init__(self,nome= '',cpf= '',senha= ''):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    def saque(self,valor):
        self.saldo -= valor

    def depositar(self,valor):
        self.saldo += valor


cli = Cliente('ana','65323443243','453242')
print(cli.__dict__)













