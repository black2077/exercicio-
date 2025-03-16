




dicio = [{'tipo': 'tv','marca':'sony','nome':'sony tvz'},{'tipo': 'som','marca':'lg','nome':'kinj d3'},{'tipo': 'tv','marca':'samsung','nome':'fd 567'}]

procura = ('sony','tv')



def procura(dicio,lista):
    print(dicio)
    return  all(dicio.get(chave) for chave in lista.values())

fg = procura(dicio[0],procura)
print(fg)

















