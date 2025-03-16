

from  time import time


def contas(func):
    def interna(*args):
        conta = {'interna' : [func(*args)]}
        return conta
    return interna


@contas
def soma(A,B):
    return A + B


def verificador(func):
    while True:
        try:
            item = int(func())
            if isinstance(item,int):
                return item
        except (TypeError,ValueError):
            break

# @verificador
# def __lista():
#     lis = input('digite sua idade:')
#     return lis






k = construtor

print(k,callable(k),k)

print(k)









# l = __lista
# print(l)


# f = soma(42,534)
# print(f)


# def contador(start = 0) :
#     passos = start
#     def func_interna():
#         nonlocal passos
#         passos += 1
#         return passos
#     return func_interna
#
# # cont = contador()
# #
# # print(cont())
# # print(cont())
# # print(cont())
# # print(cont())
# # print(callable(cont),callable(cont()))
#
#
# def adiciona_repr(cls):
#     def meu_repr(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return f'{class_repr}'
#     cls.__repr__ = meu_repr
#     return cls
#
#
# @adiciona_repr
# class Time:
#     def __init__(self, __cpf):
#         self.__cpf = __cpf
#
# @adiciona_repr
# class Planeta:
#     def __init__(self, __cpf):
#         self.__cpf = __cpf
#
#
# brasil = Time('Brasil')
# portugal = Time('Portugal')
#
# terra = Planeta('Terra')
# marte = Planeta('Marte')
#
# print(brasil)
# print(portugal)
#
# print(terra)
# print(marte)















