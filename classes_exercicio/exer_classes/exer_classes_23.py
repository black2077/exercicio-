



lista_saque = []
lista_deposito = []

def registro_exe(cls):
    def interna(*args,**kwargs):
        global lista_saque
        resultado =cls(*args,**kwargs)

        if cls.__name__ == 'saque' and len(lista_saque) <= 4:
            lista_saque.append({f'{cls.__name__}' : f'{args[1]}'})
            return resultado

        elif cls.__name__ == 'deposito':
            lista_deposito.append({f'{cls.__name__}': f'{args[1]}'})

        else:
            print('limite diario atingido')

    return interna


class Banco:
    def __init__(self,nome ='',cpf ='',senha =''):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    @registro_exe
    def saque(self,valor):
        self.saldo -= valor

    @registro_exe
    def deposito(self,valor):
        self.saldo += valor


cl = Banco('ana','75666545443','564553')

cl.deposito(1000)
cl.saque(100)
cl.saque(100)
cl.saque(100)
cl.saque(100)
cl.saque(100)
cl.saque(100)
cl.saque(100)
cl.saque(100)
cl.deposito(1000)


print(cl.__dict__)
print(len(lista_saque),lista_saque)
print(len(lista_deposito),lista_deposito)




















