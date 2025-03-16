

class arquivo:
    def __init__(self,pasta):
        self.pasta = pasta

    def copíar(self):
        return 'copiar'

    def colar(self):
        return 'colado'

    def apagar(self):
        return 'apagado'



def lista_ordem(func_1,func_2,func_3):
    yield func_1
    yield func_2
    yield func_3



def teste():
    classe = arquivo('lista')

    kl = lista_ordem(classe.copíar(),classe.colar(),classe.apagar())

    print(next(kl))
    print(next(kl))
    print(next(kl))

    # for func in kl:
    #     print('foi',func)












def linha_1(txt):
    return txt

def linha_2(txt):
    return txt

def linha_3(txt):
    return txt

def lista_func():
    yield linha_1('tainha')
    yield linha_2('vinho')
    yield linha_3('e muito sexo')



# li = lista_func()
# print(next(li))
# print(next(li))
# print(next(li))


















