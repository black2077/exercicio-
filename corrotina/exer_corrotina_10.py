import asyncio


async def tarefa(valor):
    return 's'+str(valor)


async def executa(n1,n2,n3,n4):
    return await asyncio.gather(tarefa(n1),tarefa(n2),tarefa(n3),tarefa(n4))


async def tarefas(*args):
    lista = []

    for item in args:
        lista.append(await tarefa(item))

    return lista


async def tarefa_c(valor):
    await asyncio.sleep(0.6)
    return 'a'+str(valor)


async def tarefas_concorrente(*args):
    return await asyncio.gather(*[tarefa_c(item) for item in args])



async def executa_tarefa(*args):
    lista = []

    for item in args:
        lista.append(await tarefa_c(item))

    return lista




# lista = asyncio.run(tarefas_concorrente(2,56,57,454,232,453,32,34))
lista_2 = asyncio.run(executa_tarefa(54,53,67,3,21,32,32,35))


# print(lista)
print(lista_2)








