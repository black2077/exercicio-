
lista = {'__nome':'ana','__cpf' : '545434324','__senha' : '5434432','idade': 34,'RG' : '6345345654','usuario' : '54353'}



# =====================================================================
def procuro(dicio):
    lista = {'__nome':'ana','__cpf' : '545434324','__senha' : '5434432','idade': 34,'RG' : '6345345654','usuario' : '54353'}
    match lista.values():
        case dicio:
            print(dicio)


# ====================================================================
def search_dict(dictionary, key):
    match key:
        case k if k in dictionary:
            print(dictionary[k])
            return dictionary[k]
        case _:
            return None

search_dict(lista,'__nome')
# ====================================================================



dicio = {'__nome': 'ana','__cpf' : '545434324','__senha' : '5434432'}
dicio_2 = {'__nome': 'luana','__cpf' : '557652332','__senha' : '787868'}
procuro(dicio_2)














