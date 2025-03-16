




from datetime import datetime


def filtro_str(func):
    def interna(*kwargs):
        while True:
            resultado: str = func(*kwargs)
            if isinstance(resultado,str) and resultado.isalpha() and not resultado.isspace():
                return resultado

    return interna












class Pessoa:
    info_global = {'data' : datetime.now().strftime('%d%m%Y') , 'hora' : datetime.now().strftime('%H :%M')}

    def __init__(self,nome ='',data ='',email ='',cpf =''):
        self._nome = nome
        self._data_nas = data
        self._email = email
        self._cpf = cpf


#==========================================================================
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self) -> str:
        self._nome

#=========================================================================
    @property
    def data_nas(self):
        return self._data_nas

    @data_nas.setter
    def data_nas(self):
        self._data_nas

#========================================================================
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self):
        self._email

#========================================================================
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self):
        self._cpf

#========================================================================





pessoa_1 = Pessoa()
pessoa_1._nome = 'ana'
pessoa_1._data_nas = 'das'
pessoa_1._email = 'dadw'
pessoa_1._cpf = '54535343432'

print(pessoa_1.__dict__)