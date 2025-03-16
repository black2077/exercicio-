from pprint import pprint





#
# __cpf = input('digite o __cpf :')
# idade = int(input('digite a idade :'))
#
# dicio = {'__cpf':None , 'idade' : None}
#
#
#
# if isinstance(idade,int):
#     dicio['idade'] = idade
#
# if isinstance(__cpf,str):
#     dicio['__cpf'] = __cpf
#     print(dicio)


#===================================================================
def checar_tipo(lista):
    conjuto = []
    for item in lista:
        if isinstance(item,str):
            conjuto.append({'str': item})
        if isinstance(item,int):
            conjuto.append({'int': item})
        if isinstance(item,dict):
            conjuto.append({'dict': item})
        if isinstance(item,bool):
            conjuto.append({'bool': item})
    return conjuto

lista =['ana','piba',2345678,True,{'bu':'din'},{'cartao-':'din'},False]

n = checar_tipo(lista)

lugar = dir(n)
pprint(lugar)
#=========================================================================