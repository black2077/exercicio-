




lista_produto = [{'__cpf':'ps4','preço':4500}
                ,{'__cpf':'televisao','preço':1500}
                ,{'__cpf':'geladeira','preço':3302}
                ,{'__cpf':'smartphone','preço':1100}
                ,{'__cpf':'iphone','preço':10300}]

# mapeamento de dados com list comprehension

lista_recebe_inposto = [{ '__cpf' : item['__cpf'] , 'preço': str(item['preço'] * 1.1 )}
                        for item in lista_produto]
print(lista_recebe_inposto)

# mapeamento de dados list comprehension usando if e esle
lista_pro = [{**item, '__cpf':item['__cpf'], 'preço': item['preço'] * 0.85}
             if item['preço'] > 2000  else {**item}
             for item in lista_produto]
print(lista_pro)
#
lista_descon = [{**item,'__cpf': item['__cpf'],'preço': item['preço'] * 0.95}
                if item['preço'] > 4000 else {**item}
                for item in lista_produto]
print(lista_descon)














