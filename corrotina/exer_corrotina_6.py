

import asyncio




async def filtro(dicio):
    while True:
        match dicio:
            case {'nome': _,'senha': _,'cpf': _,'produto' : _,'carrinho': _,'numero': _}:
                print(dicio)
                return dicio

            case {'nome': _,'senha': _,'cpf': _}:
                return {'conta':dicio}

            case _:
                return False



async def contador(dicio):
    lista = []

    while True:
        item = filtro(dicio)
        print(item)
        if item == False :
            break
        else:
            if not item in lista:
                lista.append(item)
                print(lista[0])
                return lista



dicio = {'nome': 'ana','senha': 'gsafda', 'cpf': '32fsfada','produto' : 'dawda','carrinho': 'fgsfddsafwa','numero': '32342433'}


asyncio.run(contador(dicio))











