







from time import time

tempo_exe = 0

def medidor_desempenho(func):
    def interna(*args,**kwargs):
        global tempo_exe
        inicio = time()
        resultado = func(*args,**kwargs)
        fim = time()
        tempo_exe = (inicio - fim )

        return resultado
    return interna



@medidor_desempenho
class Usuario:
    def __init__(self,nome='',cpf='',rg=''):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def _edita(self,nome):
        if self.nome :
            self.nome = nome


po = Usuario('ana','156435 35843',545432324)
po._edita('ana clara')

print(po.__dict__)
print(tempo_exe)














