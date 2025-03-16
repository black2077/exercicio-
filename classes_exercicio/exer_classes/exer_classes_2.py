
from  time import  sleep
#
# class camera:
#     def __init__(self,__cpf,filma = False,fotografar = False,camera_lenta = False, foto = False):
#         self.__cpf = __cpf
#         self.filma = filma
#         self.fotografar = fotografar
#         self.camera_lenta = camera
#         self.foto = foto
#
#
#     def filmar(self):
#         pernição = in
#             print('começar !')
#             self.filma = True
#             print(f'{self.filma} ta filmando ')
#
#
#     def fotografia(self):
#
#             self.filma = True
#             print(f'{self.filma} fotografia tirada ! ')
#
#
#
#     def slow_move(self):
#
#             print('1')
#             sleep(1)
#             print('2')
#             sleep(1)
#             print('3')
#             sleep(1)
#             self.filma = True
#             print(f'{self.filma} começo!')
#
#
#
#     def tirar_foto(self):
#             print('pronto !!!')
#             self.filma = True
#
# p1 = camera('sony')
# p1.filmar()
# p1.slow_move()








class Pessoa:
    def __init__(self,**infor):
        self.infor = infor

    def mostra(self):
        print(self.infor)


    @property
    def mudar_tipo(self):
        self.infor['idade'] = int(self.infor['idade'])


    @property
    def cria_financeira(self):
        self.infor.update({'renda': 0 ,'credito': 0,'__saldo': 0})







pessoa = {'__cpf': 'ana','idade':'23','__cpf':'93483312121'}

molde_1 = Pessoa(**pessoa)
molde_1.mudar_tipo
molde_1.cria_financeira

molde_1.mostra()






