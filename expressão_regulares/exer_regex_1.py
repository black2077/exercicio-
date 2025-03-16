
import  re
from datetime import datetime



# info_atual = datetime.now()
# data_atual = info_atual.strftime("%Y")
# print(data_atual)



data = '09/07/1987'



class monitorador:
    data_atual = datetime.now().strftime("%Y")

    def __init__(self,data):
        self._data = data

    @property
    def ano_atual(self):
        return self._data

    @ano_atual.setter
    def ano_atual(self)-> int:
        try:
            return -int(_data[6:10]) + int(data_atual) if re.search('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]',_data) else 0
        except TypeError:
            print('erro de tipo')


    def data(self):
        print(self._data)



dat = monitorador
print(dat.data_atual)

data_atual_cadastro = monitorador
data_de_cadastro = monitorador.data()
print(data_de_cadastro_cadastro)



















