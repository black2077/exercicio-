





dicio = {'nome' : 'maria' ,'cpf':'123456','senha':'654321'}
dicio_1 = {'funcionario': {'nome': 'maria', 'codigo': 0, 'senha': '0'}, 'data_de_validacao': '02/07/24 :04:37', 'dados_de_compra': {'usuario': {'IP': 383940703320, 'id': 50493, '_nome': 'maria', '_cpf': 12345678910, 'data_nascimento': '09/02/1998', 'endereco': '1234', 'rua': 'carlos alves', 'estado': 'rio de janeiro'}, 'forma_de_pagamento': 'cr\u00e9dito', 'numero_parcelas': 12, 'produtos': [{'id': 66688, 'nome': 'notebook lenovo s22', 'modelo': 'notebook lenovo s22 amd 5', 'marca': 'lenovo', 'tipo': 'eletronico', 'preco': 4000}], 'valor_da_parcela': 350.0, 'data_da_compra': '30/06/24 :01:51'}}


def valida_integridade(formato):
    match formato:
        case {'funcionario': {'nome': _ , 'codigo': _ , 'senha': _ }, 'data_de_validacao': _ , 
              'dados_de_compra': {'usuario': {'IP': _ , 'id': _ , '_nome': _ , '_cpf': _ , 'data_nascimento': _ , 'endereco': _ , 'rua': _ , 'estado': _ },
              'forma_de_pagamento': _ , 'numero_parcelas': _, 'produtos': [_], 'valor_da_parcela': _ , 'data_da_compra': _ }}:
            
            return True
        
        case _:
            return False



if valida_integridade(dicio_1):
    print('foi')

else:
    print('n')









