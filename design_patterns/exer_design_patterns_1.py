











from abc import ABC,abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def busca_clinte(self): pass

    @abstractmethod
    def ronta(self): pass



class van(Veiculo):
    def __init__(self,**documentos):
        self.__documentos = documentos

    def ronta(self,inicio,fim):
        print(inicio,' -----> ',fim)

    def busca_clinte(self,**info_cliente):
        self.endereco = info_cliente['endereço']
        print(self.endereco)


class onibus(Veiculo):
    def __init__(self,**documentos):
        self.__documentos = documentos

    def ronta(self,inicio,fim):
        print(inicio,' -----> ',fim)

    def busca_clinte(self,**info_cliente):
        self.endereco = info_cliente['endereço']
        print(self.endereco)





veicu_1 = {'marca': 'ford' , 'modelo': 'belta_t','ano': '2011','placa':'43dffd'}
veicu_2 = {'marca': 'ford' , 'modelo': 'belta_t','ano': '2011','placa':'gie873'}
veicu_3 = {'marca': 'honda' , 'modelo': 'b4','ano': '2020','placa':'54jfda'}


cliente_1 = {'__cpf': 'luana' , 'local': 'rua adelio bispo','referecia': """ enfrente a fabrica de aço """,'endereço' : 'central rua °15' }
cliente_2 = {'__cpf': 'luana' , 'local': 'rua adelio bispo','referecia': """ enfrente a fabrica de aço """}
cliente_3 = {'__cpf': 'luana' , 'local': 'rua adelio bispo','referecia': """ enfrente a fabrica de aço """}


van_duque_de_caxias = van(**veicu_1)
van_duque_de_caxias.ronta('xerem','rio de janeiro')


van_cliente = van(**veicu_2)
van_cliente.busca_clinte(**cliente_1)

onibus_niteroi = onibus(**veicu_3)
onibus_niteroi.ronta('xerem','niteroi')


