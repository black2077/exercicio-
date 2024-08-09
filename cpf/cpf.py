cpf = '16018088797'
cont_1 = 0
cont_2 = 0

lista = []
cpf_valido = str(cpf[:9])
print(cpf_valido)

for num in range(10,1,-1):
    digito_1 = num * int(cpf[cont_1])
    lista.append(digito_1)
    cont_1 +=1

cpf_valido += str(0 if 11 - (sum(lista) % 11) > 9 else 11 - (sum(lista) % 11))
lista.clear()

for num_2 in range(11,1,-1):
    digito_2 = num_2 * int(cpf[cont_2])
    lista.append(digito_2)
    cont_2 +=1
cpf_valido += str(0 if 11 - (sum(lista) % 11) > 9 else 11 - (sum(lista) % 11))

if cpf == cpf_valido:
    print('__cpf valido')
else:
    print('__cpf falso')
print(cpf_valido)

