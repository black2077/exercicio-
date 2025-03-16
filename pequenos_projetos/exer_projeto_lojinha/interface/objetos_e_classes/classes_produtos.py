import datetime


class Produto:
    def __init__(self,id,nome='',modelo='',marca='',tipo='',preco=  None,frete=None):
        self.id = id
        self.nome = nome
        self.modelo = modelo
        self.marca = marca
        self.tipo = tipo
        self.preco = preco
        self.frete = frete


    # ================
    @property
    def nome(self):
        return self.nome

    def nome(self):
        self.nome
    # =================
    @property
    def modelo(self):
        return self.modelo

    def modelo(self):
        self.modelo
    # =================
    @property
    def marca(self):
        return self.marca

    def marca(self):
        self.marca
    # =================
    @property
    def tipo(self):
        return self.tipo

    def tipo(self):
        self.tipo
    # =================
    @property
    def frete(self):
        return self.frete

    def frete(self):
        self.frete
    # ==================
    @property
    def preco(self):
        return self.preco

    def preco(self):
        self.preco


class Novo_Produto(Produto):
    def __init__(self,id,nome='',modelo='',marca='',tipo='',preco =None,frete =None,preco_lote=None,contidade=None,preco_unidade= None,lote='',data_entrega=''):
        super().__init__(id,nome,modelo,marca,tipo,preco,frete)
        self.preco_lote = preco_lote
        self.contidade = contidade
        self.preco_unidade = preco_unidade
        self.lote = lote
        self.data_entrega = data_entrega

    # =================
    @property
    def preco_unidade(self):
        return self.preco_unidade

    def preco_unidade(self):
        self.preco_unidade
    # =================
    @property
    def preco_lote(self):
        return self.preco_lote

    def preco_lote(self):
        self.preco_lote
    # =================
    @property
    def contidade(self):
        return self.contidade

    def contidade(self):
        self.contidade
    # =================
    @property
    def lote(self):
        return self.lote

    def lote(self):
        self.lote
    # ==================
    @property
    def data_entrega(self):
        return self.data_entrega


    def data_entrega(self):
        self.data_entrega
    # ==================

    def calcula_preco_unidade(self):
        self.preco_unidade = (self.preco_lote + self.frete) / self.contidade

    def lucro(self):
        return abs(self.preco_unidade - self.preco)

    def altera_atributo(self, nome_atributo, novo_valor):
        setattr(self, nome_atributo, novo_valor)


class Produto_Perecivel(Produto):
    def __init__(self,id,nome='',modelo='',marca='',tipo='',preco='',frete='',validade =''):
        super().__init__(id,nome,modelo,marca,tipo,preco,frete)
        self.validade = validade



class Novo_Produto_Perecivel(Produto_Perecivel):
    def __init__(self,id,nome='',modelo='',marca='',tipo='',preco='',frete='',validade ='',preco_lote='',contidade='',preco_unidade='',lote='',data_entrega=''):
        super().__init__(id,nome,modelo,marca,tipo,preco,frete,validade)
        self.preco_lote = preco_lote
        self.contidade = contidade
        self.preco_unidade = preco_unidade
        self.lote = lote
        self.data_entrega = data_entrega



    # =================
    @property
    def preco_unidade(self):
        return self.preco_unidade

    def preco_unidade(self):
        self.preco_unidade

    # =================
    @property
    def preco_lote(self):
        return self.preco_lote

    def preco_lote(self):
        self.preco_lote

    # =================
    @property
    def contidade(self):
        return self.contidade

    def contidade(self):
        self.contidade
    # =================
    @property
    def lote(self):
        return self.lote

    def lote(self):
        self.lote
    # ==================
    @property
    def data_entrega(self):
        return self.data_entrega

    def data_entrega(self):
        self.data_entrega
    # ===================
    @property
    def validade(self):
        return self.validade

    def validade(self):
        self.validade


    # ===================
    def calcula_preco_unidade(self):
        self.preco_unidade = (self.preco_lote + self.frete) / self.contidade


    def lucro(self):
        return abs(self.preco_unidade - self.preco)


    def altera_atributo(self, nome_atributo, novo_valor):
        setattr(self, nome_atributo, novo_valor)



if __name__ == '__main__':
    print('========== produto ===============')
    classes_produto = Produto('345','ps4','ps4 slim 2.0','sony','video game','20',20)
    print(classes_produto.__dict__)
    # ==========================
    print('========== novo produto ============')
    classes_produto_novo = Novo_Produto('433','TV 42 KJ','JH 42','LG','TV',1500,2000,200000,200,700,'FSE','09/09/2024')
    classes_produto_novo.calcula_preco_unidade()
    print(classes_produto_novo.__dict__)
    print(f'lucro = {classes_produto_novo.lucro()}')

    # ==========================
    print('========== produto perecivel ============')
    classes_produto_perecivel = Produto_Perecivel('343','ARROZ 5 KG','SACO 5KG','BARRIGA','CEREAIS',30,0,'09/09/2035')
    print(classes_produto_perecivel.__dict__)
    # ==========================
    print('========= novo produto perecivel =============')
    classes_produto_novo_perecivel = Novo_Produto_Perecivel('438','feijão','1 kg','barriga','cereais',11,2000,'09/09/2030',20000,1500,0,'gd','09/09/2035')
    classes_produto_novo_perecivel.calcula_preco_unidade()
    print(classes_produto_novo_perecivel.__dict__)
    print(f'lucro = {classes_produto_novo_perecivel.lucro()}')


