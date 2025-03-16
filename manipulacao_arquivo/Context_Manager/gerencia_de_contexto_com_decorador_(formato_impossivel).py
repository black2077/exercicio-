




# formato impossivel 

def decorador_contador(chave_1):
    def contador(func):
        def interna(*args,**kwargs):
            resultado = func(*args,**kwargs)
            print(resultado.__dict__)

            print('no decorador',chave_1)
            return resultado
        return interna
    return decorador_contador



@decorador_contador('faawdw')
class Arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio


    def __enter__(self):
        print('no gerenciador de contexto')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



with Arquivo('FAFDADWA') as arquivo:
    print(arquivo.__dict__)







