cpf = '21619917793'
cpf_valido = cpf[:-2]
lista = []
digito = 0
print(cpf_valido)

while 2 > digito:
    digito += 1
    cont = 0
    for num in range(9 + digito, 1, -1):
        lista.append(int(num * int(cpf_valido[cont])))
        cont+=1
    cpf_valido += str(0) if 11 - (sum(lista) % 11) > 9 else str(11 - (sum(lista) % 11))
    lista.clear()

if  cpf == cpf_valido :
    print('__cpf verdadeiro')
else:
    print('__cpf falso')
print(cpf_valido)