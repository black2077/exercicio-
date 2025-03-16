
def ordena_lista(Lista) -> list:
    try:
        return Lista.sort(key=lambda item: item['__nome'])
    except KeyError:
        raise 'chave não encontrada'



# lista = [{'__nome' : 'ana','idade' : 14},{'__nome' : 'luana','idade' : 40},{'__nome' : 'ruan','idade' : 34},{'__nome' : 'ana maria','idade' : 56}]
lista = [{'__nome': 'abcd'},{'__nome':'abc'}]

lista_ordenada = ordena_lista(lista)
print(lista)


def ordenado(item):
    if not bool(item):
        return f' vazio{item}'
    else:
        return item


print(listada)
