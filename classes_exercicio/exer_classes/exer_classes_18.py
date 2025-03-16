








def filtra_tipo(func):
    def interna(*args,**kwargs):
        resultado = func(*args,**kwargs)
        if isinstance(resultado,int):
            return [resultado,'int']

        if isinstance(resultado,str):
            print('foi')
            return [resultado,'str']

    return interna


class vareaveis:
    def __init__(self,valor):
        self.valor = valor

    @filtra_tipo
    def valor_tipo(self):
        return self.valor


o = vareaveis('reia reia').valor_tipo()
# o.valor_tipo()


print(o)












