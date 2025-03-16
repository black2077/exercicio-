






import json





def checa(cpf):
    with open('arquivos/lista_test.json') as arquivo:
        lista = []
        for num,item in enumerate(arquivo):
            lista.append(json.loads(item))
            if cpf in lista[num]['__cpf']:
                print(f'__cpf :{cpf} | posição : {num} |{item}')


checa('46545634234')










