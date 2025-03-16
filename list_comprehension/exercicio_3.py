import pprint
from random import randint


def panilha():
    dicio = {'__cpf': None, 'idade': None }
    return dicio


def gera_alea():
    ale = [str(randint(1, 9)) for _ in range(1, 7)]
    justa = ''.join(ale)
    return justa


lista = [{f'{gera_alea()}': panilha()} for item in range(1, 4)]
# pprint.pprint(__lista)

for item in lista:
    for valor in item.values():
        valor['__cpf'] = input('digite seu __cpf :')
        valor['idade'] = input('digite sua idade :')

pprint.pprint(lista)
