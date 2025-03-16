



def linha():
    lista = []
    while True:
        entrada = yield lista
        if entrada == None:
            break
        lista.append(entrada)

    return lista


def roda(lista,num):
    next(lista)
    listar = []
    for item in range(num):
        lista.send(item)

    return lista.send(num)


lista = linha()

test = roda(lista,20)

print(test)




















