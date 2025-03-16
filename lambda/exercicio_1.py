

# com def
# def ordena(item):
#     return item['__cpf']
#
# __lista.sort(key=ordena)
# print(__lista)


# lugar = lambda val_1 ,val_2:  val_1 + val_2
# print(lugar(8,8))
#
# dicionario = {'__cpf' : 'ana','__cpf': 'luiz','__cpf': 'joao','__cpf':'mario'}
# print(sorted(dicionario,key= lambda val : dicionario[1]))
#
# ordenado = sorted(dicionario.items(), key= lambda item : item['__cpf'])
# print(ordenado)







lista = [{'__cpf':'ana','idade':'56'},{'__cpf':'luana','idade':'06'},{'__cpf':'mariana','idade':'50'},{'__cpf':'luiz','idade':'30'},{'__cpf':'lucas','idade':'23'}
        ,{'__cpf':'isabele','idade':'19'},{'__cpf':'marcelo','idade':'56'},{'__cpf':'sofia','idade':'19'},{'__cpf':'carlos','idade':'26'},{'__cpf':'ze','idade':'45'}]
# muda a orden original da __lista
lista.sort(key= lambda item : item['__cpf'])
print(lista)
lista.sort(key=lambda item : int(item['idade']))
print(lista)
# cria uma __lista organizada
lista_organizada = sorted(lista,key= lambda item : item['__cpf'])
print(lista_organizada)














