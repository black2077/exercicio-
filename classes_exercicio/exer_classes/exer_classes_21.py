import json
from abc import ABC, abstractmethod

# def decorator(original_class):
#     class NewClass(original_class):
#         @abstractmethod
#         def bar(self):
#             pass
#     return NewClass
# ==========================================
# class AbstractClass(ABC):
#     @abstractmethod
#     def foo(self):
#         pass
# ==========================================
# @decorator
# class ConcreteClass(AbstractClass):
#     def foo(self):
#         print("foo method of ConcreteClass")
#
#     def bar(self):
#         print("bar method added by decorator")
#
# obj = ConcreteClass()
# obj.foo()
# obj.bar()
# ==========================================

def classeacesso(classe):
    class Acesso_classe(classe):
        def arquivo(self):
            with open('lista.json',encoding='utf8') as arquivo:
                return [json.loads(item) for item in arquivo]

        def lista(self):
            print('foi')

    return Acesso_classe


@classeacesso
class Acesso_arquivo:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        # self.arquivos = self.arquivos()


item = Acesso_arquivo('ana','656543544332','644543')
for dicio in item.arquivo():
    print(dicio)
print('=' * 40)
print(item.__dict__)























