


class Produto:
    def __init__(self,nome,marca,valor):
        self.nome = nome
        self.marca = marca
        self.valor = valor

    def envio(self,endereco):
        self.endereco = endereco


class compra:
    def __init__(self,valor):
        self.valor = valor



def filtra_classe(cls,*args):

    classe = cls(*args)

    while True:
        if issubclass(cls,Produto):
            resultado = yield classe
            classe = None

        else:
            print('classe ')



c = filtra_classe(Produto,'ps4','sony',4000)

h = compra(1000)

print(c)
next(c)

print(next(c).__dict__)

print(next(c))














