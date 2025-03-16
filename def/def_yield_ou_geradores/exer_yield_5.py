


class arquivo:
    def __init__(self,pasta):
        self.pasta = pasta

    def copíar(self):
        # print('foi 1')
        return 'copiar'

    def colar(self):
        # print('foi 2')
        return 'colar'

    def apagar(self):
        # print('foi 3')
        return 'apagar'


def ordena_funcao(*args):
    for func in args:
        yield func()


def valores_valor():
    print('começo')
    valor = yield
    print(f'recebir o valor :{valor}')


def teste_funcao_ordena(num):
    classe = arquivo('lista')
    lista = ordena_funcao(classe.copíar,classe.colar,classe.apagar)

    for item in range(num):
        print(next(lista))


def teste_valores_yield(num):
    test = valores_valor()
    next(test)
    test.send(num)


teste_funcao_ordena(3)

print('======================================')

teste_valores_yield(4)


