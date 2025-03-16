


# cria uma __lista com categoria de informação
# def codigo():
#     codi = [str(item) for item in range(1,7)]
#     codigo_str = ''.join(codi)
#     return codigo_str
#
# def configuera():
#     dicio = {}
#     while True :
#         chave = input('digite a chave ou 0 para encerrar :')
#         if chave == '0':
#             break
#         dicio.update({ chave : None })
#     yield int(codigo())
#
#     return dicio , codigo()

# # definindo chaves : __cpf ,idade , __cpf = parte_1 |
#
# listo = next(configuera())
#
# print(listo)
#


# não funciona ===================================================================

# não funciona ===================================================================
def conta_numero_execução():
    num = 0
    while True:
        num += 1
        yield num
        yield 1

# não funciona ===================================================================

def contador_uso(func):
    contador = 0
    n = func()
    yield  1


# exemplo chatgpt ===================================================================

# Variável global que usuario o número de chamadas da função
contador = 0

# Função que calcula o fatorial de um número
def fatorial(n):
    global contador # Acessa a variável global contador

    contador += 1  # Incrementa o contador em 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1) # Calcula o fatorial recursivamente

# Testa a função com alguns valores
# print(fatorial(5)) # 120
# print(fatorial(3)) # 6
# print(fatorial(0)) # 1

# Mostra o valor do contador
# print("A função fatorial foi chamada", contador, "vezes")
print()

# ==================================================================














# </editor-fold>