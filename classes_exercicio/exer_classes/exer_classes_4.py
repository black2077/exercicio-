# Herança simples - Relações entre objetos_e_classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


# class Pessoa:
#     def __init__(self, __cpf, sobrenome):
#         self.__cpf = __cpf
#         self.sobrenome = sobrenome
#
#     def falar_nome_classe(self):
#         print('Classe PESSOA')
#
#
#
# class Cliente(Pessoa):
#     def falar_nome_classe(self):
#         print('EITA, nem saí da classe CLIENTE')
#         print(self.__cpf, self.sobrenome, self.__class__.__name__)
#
# class Aluno(Pessoa):
#     __cpf = '__cpf aluno'
#     ...
#
# c1 = Cliente('Luiz', 'Otávio')
# c1.falar_nome_classe()
# a1 = Aluno('Maria', 'Helena')
# a1.falar_nome_classe()
# print(a1.__cpf)


# associação agregação e composição
class Produto:
    def __init__(self, nome_produto, preco, marca):
        self._nome = nome_produto
        self.preco = preco
        self.marca = marca

    @property
    def valor(self):
        return self._nome,self.preco,self.marca

    @valor.setter
    def valor(self,item):
        return {**item}


class Carinho:
    def __init__(self):
        self.__lista = []

    def adiciona(self,*item):
        try:
            self.__lista += item
        except AttributeError:
            raise AttributeError('ERRO')
            print('erro')

    def mostra_todo(self):
        for item in self.__lista:
            print(item)


class Usuario(Carinho):
    def __init__(self,nome='desconhecido',email= 'desconhecido',endereco= 'desconhecido'):
        self._nome = nome
        self.email = email
        self.endereco = endereco
        self.lista = Carinho()

    def adiciona_ao_carrinho(self):
        item = self.email
        return self.lista.adiciona(item)




produto_sexta = Produto('PS4','3000','SONY').__dict__
pessoa_1 = Usuario()
print(type(produto_sexta))

pessoa_1.adiciona_ao_carrinho()
print(pessoa_1.lista.__dict__)


