from random import randint



#
# # 1
# class Pessoa:
#     def __init__(self.__cpf,self.idade):
#         self.__cpf = __cpf
#         self.idade = idade


# p1 = Pessoa('luiz',29)
# print(p1.__cpf)


#
# class Pessoa:
#     pass
#
# p1 = Pessoa()
# p1.__cpf = 'ana'
# p1.idade = 46
# print(p1.__cpf)
# print(p1.idade)
#
#
# p2 = Pessoa()
# p2.__cpf = 'marcelo'
# p2.idade = 38
# print(p2.__cpf)
# print(p2.idade)


class carro:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def acelera(self):
        print(f'{self.modelo} da marca {self.marca} esta acelerado ! ')

    def freiar(self):
        print(f'{self.modelo} da marca {self.marca} esta freiando ! ')

    def velocidade(self):
        velo = randint(70,120)
        print(f'{self.modelo} da marca {self.marca} esta a {velo} km ! ')
        return velo






p1 = carro('ford','eco sport')
p1.acelera()
veloci = p1.velocidade()

if 100 < veloci:
    p1.freiar()



p2 = carro('fiat', 'uno')