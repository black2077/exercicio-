
produto = [{'produto': 'tv 32','preço' : 1000},{'produto': 'ps4','preço' : 4000},{'produto': 'sofa','preço' : 1230}
           ,{'produto': 'piraque','preço' : 4},{'produto': 'camisa','preço' : 48},{'produto': 'tv 32','preço' : 12}]


def aplica(item):
    return round(item['preço'] * 1.1,2)


def pegar(lista):
    return [ {f"{item['produto']}" :aplica(item)} for item in lista]

hjh = pegar(produto)
print(hjh)


usando_map = list(map(aplica,produto))
print(usando_map)













