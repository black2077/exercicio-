from .objetos_e_classes.objetos_operacao_em_arquivo import Arquivo_base,Arquivo_Funcionario,Arquivo_Administrador
import json



def mostra_lista_produtos(*caminho):
    with Arquivo_base(*caminho) as arquivo:
        for item in arquivo.produtos():
            print(item)
            print()

def mostra_item(objeto):
    for item in objeto:
        print(item)


def linha(tam = 40):
    print('=' * tam)


def linha_cores(tam = 40,cor = '0;0',):
    print(f"\033[{cor}m" + ('=' * tam) + '\033[0;0m')


def mostra_compras_tendentes_de_cliente(*caminho):
    def mostra(item,num):
        print('=' * 80, f'  {num}  ' ,'=' * 80)
        dicio = json.loads(item)
        del dicio['usuario']['IP']
        print()
        print('| usuario = ',dicio['usuario'],sep= '')
        print('| pagamento = ',dicio['informacao_de_venda'],sep= '')
        print()
        print('                                                             produtos')
        print()
        for item in dicio['produtos']:
            print(item)
        print()
        linha(170)
        print()

    with Arquivo_Funcionario(*caminho) as arquivo:
        for num,item in enumerate(arquivo.arquivos()):
            mostra(item,num)

        
def mostra_compras_validas_de_cliente(*caminho):
    def mostra(item:dict,num =''):
        dicio = json.loads(item)
        print('=' * 70,f'  {num}  ','=' * 70)
        print()
        print('funcionario que Válido =',dicio['valida'],sep=' ')
        print('usuario =',dicio['usuario'])
        print('informação de venda =',dicio['informacao_de_venda'])
        print()
        linha(150)
        print()
        print('                                                             produtos')
        print()
        for item in dicio['produtos']:
            print(item)

        print()
        linha(150)

    with Arquivo_Funcionario(*caminho) as arquivo:
        for num,item in enumerate(arquivo.arquivos()):
            mostra(item,num)
            print()


def mostra_produtos_funcionario(*caminho):

    def exibir_produto_funcionario(dicio :dict, num: str =''):
        
        linha(110)
        print()
        print(f'   | id : {dicio['id']} | nome : {dicio['nome']} | modelo : {dicio['modelo']} | marca: {dicio['marca']} | tipo : {dicio['tipo']} | preço : {dicio['preco']} ')
        print(f'{num}')
        print(f'   | frete : {dicio['frete']} | preço lote : {dicio['preco_lote']} | contidade : {dicio['contidade']} | preço por unidade : {dicio['preco_unidade']} | lote : {dicio['preco_unidade']} | data de entrega : {dicio['data_entrega']}')
        print()

    with Arquivo_Funcionario(*caminho) as arquivo:
        for num,item in enumerate(arquivo.arquivos()):
            dicio = json.loads(item)
            exibir_produto_funcionario(dicio,num)


def mostra_compras_tendentes_pra_cliente(cliente,*caminho):

    with Arquivo_Funcionario(*caminho) as arquivo:
        lista = []
        cliente = cliente.__dict__
        for item in arquivo.arquivos():
            dicio = json.loads(item)
            if dicio['usuario']['_nome'] == cliente['_nome'] and dicio['usuario']['_cpf'] == cliente['_cpf']:
                lista.append(dicio['produtos'])

        for item in lista:
            print(item)
        
        return lista


def mostra_funcionario(*caminho):
    with Arquivo_Administrador(*caminho) as arquivo:
        for item in arquivo.arquivos():
            dicio = json.loads(item)
            del dicio['senha']
            print(dicio)



if __name__ == '__main__':
    mostra_compras_validas_de_cliente('diretorios','compras','compras_validas.json')

