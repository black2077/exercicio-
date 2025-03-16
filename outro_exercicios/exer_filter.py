


lista = ['ana','luana','joao','matheus','felipe']

lista_pessoas = [{'nome': 'ana', 'idade': 29 , 'cpf': '85343543535'},
                 {'nome': 'luana','idade': 23 ,'cpf':'65643354445'},
                 {'nome': 'mariana','idade': 67 ,'cpf':'6775675632'}]


def filtro(item):
    lista = list(filter(lambda x: x in ('ana','luana'),item))
    return lista

filtro(lista)



def filtro_dicio(item,*chave):
    lista = list(filter(lambda arquivo: arquivo['nome'] == chave[0] and arquivo['cpf'] == chave[1],item))
    return lista



filtro_dicio(lista_pessoas,'mariana','6775675632')
































