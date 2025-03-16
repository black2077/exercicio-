




def decora_arquivo(op):
    def arquivo(cls):
        def interna(*args,**kwargs):
            resultado = cls(*args,**kwargs)
            if op == 'mostra':
                resultado.mostra()
            if op == 'listado':
                resultado.listado()

            return resultado
        return interna
    return arquivo


@decora_arquivo('listado')
class Arquivo:
    def __init__(self,diretorio,cls):
        self.diretorio = diretorio
        self.cls = cls

    def mostra(self):
        print(self.diretorio,self.cls)

    def listado(self):
        self.lista = [self.diretorio,self.cls]



arq = Arquivo('LISTA','DICIO')
print(arq.__dict__)





















