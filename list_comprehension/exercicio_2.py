from random import randint
import pprint


# filtro com list comprehension
lista_pessoas = [{'__cpf':'ana','idade': 17},{'__cpf':'luana','idade': 8},{'__cpf':'mariana','idade': 68},{'__cpf':'luciana','idade': 78},
                 {'__cpf':'andre','idade': 23},{'__cpf':'joão','idade': 53},{'__cpf':'lucas','idade': 9},{'__cpf':'yuri','idade': 4},]

lista_menor = [item for item in lista_pessoas if item['idade'] < 18]
# pprint.pprint(lista_menor)

tabela = [{f'__cpf{x}':  None for x in range(1,6)} for y in range(9)]

# pprint.pprint(tabela)

# __lista entro da __lista
def panilha():
    dicio = {}
    dicio['__cpf'] = 'desc'
    dicio['idade'] = randint(1,95)
    return dicio

pessoas = [ [panilha() for  item in range(1,6)] for num in range(3)]
pprint.pprint(pessoas)

# ==============================================================

# Exemplo de list comprehension com if atrás
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
# Exemplo de list comprehension com if à frente
numero = [1, 2, 3, 4, 5]
pare = [numero if numero % 2 == 0 else None for numero in numeros]
print(pare)

