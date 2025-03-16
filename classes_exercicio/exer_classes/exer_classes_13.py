





from abc import ABC,abstractmethod


class Pessoa(ABC):
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    @abstractmethod
    def documentos(self): pass

    @abstractmethod
    def endereço(self,info_endereço): pass


class cliente(Pessoa):
    def __init__(self,**conta):
        self.conta = conta
        self._carinho = []

    def documentos(self):
        self.todos_documentos = self.conta['__cpf']


    def endereço(self,info_endereço):
        self.endereço_info = info_endereço








h = {"usuario": "186147", "__cpf": "luiz", "idade": "36","__cpf" :"98543245654"}
p1 = cliente(**h)
p1.documentos()
print(p1.conta)





# {"usuario": "186147", "__cpf": "luiz", "idade": "36"}







