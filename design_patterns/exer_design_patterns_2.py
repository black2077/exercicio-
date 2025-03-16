
from abc import ABC,abstractmethod






class Restaurante(ABC):

    @abstractmethod
    def entrega(self,endereco): pass

    @abstractmethod
    def cadapio(self): pass

# ==================================================================================
class Restaurante_duque_de_caxias(Restaurante):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def entrega(self,endereco):
        print(f'endereço = {endereco} | enviado para entregador')
        print('taxa = 4.00')

    def cadapio(self):
        print('costela a coentro')
        print('frango pote')
        print('linguiça suina')
        print('bife role')

# =================================================================================
class Restaurante_rio_de_janeiro(Restaurante):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def entrega(self,endereco):
        print(f'endereço = {endereco} | enviado para entregador')
        print('taxa = 7.00')

    def cadapio(self):
        print('costela a coentro')
        print('salmão')
        print('frango pote')
        print('linguiça suina')
        print('linguiça de frango')
        print('bife role')


info = {'direção ': 'carlos mario alves skatok','endereço':'rua lucas otavio'}

restaurante_shopping = Restaurante_duque_de_caxias(**info)
restaurante_shopping.cadapio()
restaurante_shopping.entrega('rua bbk mario')

print(restaurante_shopping.quandro_funcionario('fd'))


