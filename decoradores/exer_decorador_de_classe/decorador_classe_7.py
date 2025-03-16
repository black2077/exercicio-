


from datetime import datetime



class pagamentos_pendentes:
    def __init__(self,diretorio):
        self.diretorio = diretorio

    def adiciona(self,dicio):
        with open(self.diretorio,'a') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')

    def pendentes(self,dicio):
        self.adiciona(dicio.__dict__)

        print(dicio.__dict__)





class Usuario:
    def __init__(self,nome,cpf,senha,carrinho=[],compras = []):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.carrinho = carrinho
        self.compras = compras

    def add_carrinho(self,arquivo):
        self.carrinho.append(arquivo)

    def pagamento(self,valor,vezes,item,formata_de_pagamento,vendedor=None):
        data = datetime.now().strftime("%Y-%m-%d %H:%M")
        # , 'vezes' : item['preco'] / vezes, 'total pago':0
        dicio = {'data' : data, 'item vendido' : item, 'vendedor':vendedor, 'formata_de_pagamento': formata_de_pagamento}

        def pagamento_credito(vezes,valor):
            if  valor > 250:
                return {'vezes' : vezes, 'total pago': item['preco'] * 1.05}


        if formata_de_pagamento in ('pix' ,'deposito','dinheiro') :
            dicio_ = {'total pago': item['preco'] * 0.95}
            dicio.update(dicio_)

        else:
            print('compra não efetuada',item['preco'] * 0.95)


        if formata_de_pagamento == 'credito':
            valor_item = item['preco'] * 0.95
            dicio.update(pagamento_credito(vezes,valor_item))

        self.compras.append(dicio)





fd = Usuario('ANA','53454532','765654')
fd.pagamento(3150,1,{'nome': 'ps5','preco':3000},'credito','sistema')

pg = pagamentos_pendentes('avalidador_de_acesso.json')
pg.pendentes(fd)

# print(fd.__dict__)


