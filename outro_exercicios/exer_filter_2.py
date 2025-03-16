




lista = [{'marca':'sony','tipo':'tv','polegadas':'32','preço':'1000'},{'marca':'samsung','tipo':'som','preço':'400'},
         {'marca':'lg','tipo':'tv','polegadas':'42','preço':'1500'},{'marca':'sony','tipo':'video game','preço':'1000'}]


def procura_lista(lista,*args):
    lista_arquivo = list(filter(lambda item : item['marca'] == args[0] or item['tipo'] == args[1] ,lista))
    return lista_arquivo


hj = procura_lista(lista,'sony','tv')
print(hj)
























