




class Funcionario:
    def __init__(self,nome,codigo,senha):
        self.nome = nome
        self.codigo = codigo
        self.senha = senha



class Administrador(Funcionario):
    def __init__(self,nome,codigo,senha):
        super().__init__(nome,codigo,senha)



class Proprietario(Administrador):
    def __init__(self,nome,codigo,senha,cnpj,cpf):
        super().__init__(nome,codigo,senha)
        self.cnpj = cnpj
        self.cpf = cpf







# if __name__ == '__main__':
    #fun = Funcionario('nome','54345434','43444')
    #print(fun.__dict__)

    #do = Proprietario('ANDERSON','85355664','65434','45456456545','667576576')
    #print(do.__dict__)

    








