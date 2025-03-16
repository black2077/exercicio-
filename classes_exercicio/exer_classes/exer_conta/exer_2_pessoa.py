



class Pessoa:
    def __init__(self,nome ,cpf ,senha ):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def senha(self):
        return self._senha

    @nome.getter
    def nome(self, valor):
        self._nome = valor

    @cpf.getter
    def cpf(self, valor):
        self._cpf = valor

    @senha.getter
    def senha(self,valor):
        self._senha = valor


if __name__ == '__main__':
    li = Pessoa('ana','65345234234','5453SFS')



    print(li.__dict__)













