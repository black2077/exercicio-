


class Visitante:
    def __init__(self,IP,id = '',nome ='',cpf ='',senha ='',carrinho =[]):
        self.IP = IP
        self.id = id
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self.carrinho_lista = carrinho


    def adicionar_carrinho(self,item):
        self.carrinho_lista.append(item)
        #===================================
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome
    #===================================
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf
    # ==================================
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self,senha):
        self._senha = senha

    @property
    def carrinho(self):
        return self.carrinho_lista

    @carrinho.setter
    def carrinho(self, item):
        self.carrinho_lista = item



class Cliente(Visitante):
    def __init__(self,IP,id,nome,cpf,senha,carrinho =[],data_de_nascimento = '',endereco ='',rua ='',estado =''):
        super().__init__(IP,id,nome,cpf,senha,carrinho)
        self.data_nascimento = data_de_nascimento
        self.endereco = endereco
        self.rua = rua
        self.estado = estado

    def pagamentos(self,forma,preco,parcelas):...




























