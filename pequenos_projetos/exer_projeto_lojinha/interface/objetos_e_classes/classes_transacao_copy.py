
from datetime import datetime 


class Venda:
    def __init__(self,forma_de_pagamento: str,numero_parcelas: int,produtos: list):
        self.forma_de_pagamento = forma_de_pagamento
        self.numero_parcelas = numero_parcelas
        self.valor_dos_produtos = self.tipo_pagamneto(produtos)  
        self.valor_da_parcela = self.valor_dos_produtos / self.numero_parcelas  
        self.data_da_compra = datetime.now().strftime('%d/%m/%y :%H:%M')


    def tipo_pagamneto(self,produtos,taxa = 1.05):
        lista = []
        
        for produto in produtos:
            lista.append(produto['preco'])

        if self.forma_de_pagamento == 'débito' and self.numero_parcelas == 1:
            return sum(lista)
                
        if self.forma_de_pagamento == 'crédito':
            return sum(lista) * taxa



class compra_em_analise:
    def __init__(self,usuario,venda,produtos):
        self.usuario = usuario
        del self.usuario['_senha'],self.usuario['carrinho_lista']
        self.informacao_de_venda = venda
        self.produtos = produtos



class Efetiva_Venda:
    def __init__(self,funcionario :dict):
        self.funcionario = funcionario
        del self.funcionario['senha']       
        self.data_de_validacao = datetime.now().strftime('%d/%m/%y :%H:%M')



class Efetiva_Compra:
    def __init__(self,funcionario: dict, usuario: dict, venda: dict, produtos: dict):
        self.valida = funcionario       
        self.usuario = usuario
        
        self.informacao_de_venda = venda
        self.produtos = produtos

