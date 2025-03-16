

import json

def le_arquivo():
    with open('arquivos/lista_test.json') as arquivo:
        return [{f'{num}':json.loads(item)} for num,item in enumerate(arquivo)]


def procura(posicao,lista):
    if isinstance(posicao,str) or posicao > len(lista) :
        raise f'{posicao} não existe'

    else:
        return lista[posicao]

lista = le_arquivo()

lista_procura = procura(4,lista)
print(lista_procura)















