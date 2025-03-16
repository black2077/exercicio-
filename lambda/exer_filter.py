






lista_pessoas = [{'__cpf':'ana','idade': 17},{'__cpf':'luana','idade': 8},{'__cpf':'mariana','idade': 68},{'__cpf':'luciana','idade': 78},
                 {'__cpf':'andre','idade': 23},{'__cpf':'joão','idade': 53},{'__cpf':'lucas','idade': 9},{'__cpf':'yuri','idade': 4},]



filtra_maior = list(filter(lambda pessoa : pessoa['idade'] >= 18,lista_pessoas))
filtra_menor = list(filter(lambda pessoa : pessoa['idade'] <= 18,lista_pessoas))

print(filtra_maior)
print(filtra_menor)


























