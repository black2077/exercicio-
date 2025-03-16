import json


#
# def monitora_atividade(func,dicio_cls,valor):
#     global dicio
#     dicio = {'usuario' : dicio_cls,f'{func.__name__}': []}
#     dicio[f'{func.__name__}'].append(valor)
#     print(dicio)
#


class monitora_atividade:
    def __init__(self,diretorio,func,dicio_cls,valor):
        self.diretorio = diretorio
        self.nome_func = func.__name__
        self.dicio_cls = dicio_cls
        self.valor = valor
        self.carrega_arquivo()
        self.procura()
        self.edita_arquivo()


    def carrega_arquivo(self):
        with open(self.diretorio) as arquivo:
            return [json.loads(item) for item in arquivo]


    def procura(self):
        lista = self.carrega_arquivo()
        for num,item in enumerate(lista):
            if self.dicio_cls['nome'] == item['conta']['nome'] and self.dicio_cls['cpf'] == item['conta']['cpf']:
                self.indice , self.arquivo = num,item

        del self.dicio_cls

    def edita_arquivo(self):

        def edita():
            lista = self.carrega_arquivo()
            lista[self.indice] = self.arquivo

            with open(self.diretorio, 'w') as arquivo:
                lista_arquivo = [json.dumps(item) + '\n' for item in lista]
                arquivo.writelines(lista_arquivo)

        if len(self.arquivo[f'{self.nome_func}']) < 10:
            self.arquivo[f'{self.nome_func}'].append(self.valor)
            edita()
        else:
            del self.arquivo[f'{self.nome_func}'][0]
            edita()


class Cliente_Acesso:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


class Cliente:
    def __init__(self,nome,cpf,senha,saldo,conta,banco):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo
        self.conta = conta
        self.banco = banco


    def saque(self,valor):
        self.saldo -= valor
        hj = monitora_atividade('_lista_atividade_contas.json',self.saque,self.__dict__,valor)
        print(hj.__dict__)


    def deposito(self,valor):
        self.saldo += valor
        # hg = monitora_atividade('_lista_atividade_contas.json',self.deposito,self.__dict__,valor)


if __name__ == '__main__':

    Cliente_1 = Cliente('ana','6535345435','867767',200,'76767','75654')
    Cliente_1.saque(340)
    Cliente_1.deposito(100)

    # print(Cliente_1.__dict__)














