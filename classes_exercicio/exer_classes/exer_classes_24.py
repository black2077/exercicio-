


lista_registro = {'deposito' : [],'saque' : []}

def registro_exe(cls):
    def interna(*args,**kwargs):
        global lista_registro
        resultado =cls(*args,**kwargs)

        if cls.__name__ == 'saque' and len(lista_registro['saque']) <= 4:
            lista_registro['saque'].append(args[1])
            return resultado

        elif cls.__name__ == 'deposito':
            lista_registro['deposito'].append(args[1])

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
cl.saque(120)
cl.saque(140)
cl.saque(139)


cl.deposito(1000)


print(cl.__dict__)
print(lista_registro)
