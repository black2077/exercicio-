



class Produto:
    def __init__(self,nome,preco,modelo,marca,tipo):
        self.nome = nome
        self.preco = preco
        self.modelo = modelo
        self.marca = marca
        self.tipo = tipo



class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf



class Cliente(Pessoa):
    def __init__(self,nome,cpf,senha):
        super().__init__(nome,cpf)
        self.senha = senha
        self.lista_carrinho = []


    def carrinho(self,item):
        self.lista_carrinho.append(item)



usuario = Cliente('ANA','5654645656','465645')

def carrinho(cls: Cliente):
    while True:
        print('=====================================')
        # nome = input('digite o nome do produto:')
        # preco = input('digitee o preço :')
        # modelo = input('digite o modelo :')
        # marca = input('digite a marca :')
        # tipo = input('digite o tipo do produto :')

        nome = 'ana'
        preco = '56675'
        modelo = 'fhfh'
        marca = '5464'
        tipo = 'gdse'

        pro = Produto(nome,preco,modelo,marca,tipo)
        cls.carrinho(pro)
        op = input('deseja adicionar |s|n|:')
        if op == 'n':
            return cls


lk = carrinho(usuario)

for item in lk.lista_carrinho:
    print(item.__dict__)
