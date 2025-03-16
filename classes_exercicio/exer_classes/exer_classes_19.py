

def filtro_tipo(tipo):
    def interna(func):

        def filtro(*args, **kwargs):
            resultado  = func(*args,**kwargs)
            while True:
                print('fg')
                if  resultado.isnumeric():
                    print('foi')
                    return resultado

        return filtro    
    return interna


class Usuario:
    def __init__(self,nome = '',cpf = '',rg =''):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    @filtro_tipo(int)
    def input_info(self) :
        self.cpf = input('digite seu __cpf :')



usu = Usuario()
usu.input_info()
print(usu.__dict__)

da = 'fra'
da.isnumeric()












