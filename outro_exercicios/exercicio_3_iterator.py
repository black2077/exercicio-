




import sys


# serve pra ocupar menos espaço na memoria
tab = int(input('digite o numero :'))
lista  = ( tab  * num for num in range(11) )
print(lista)

for item in lista:
    print(item)

print(sys.getsizeof(lista))










