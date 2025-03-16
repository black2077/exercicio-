
import exer_3_cliente
from random import randint



def gerador_chave(tamanho):
    return  ''.join(str(randint(1,9)) for _ in range(1,tamanho+1))


def novo_cliente_poupanca():
    nome = input('digite seu nome:')
    cpf = input('digite seu cpf:')
    senha = input('digite sua senha:')
    agencia = gerador_chave(6)
    conta = gerador_chave(5)

    classe = exer_3_cliente.cliente_poupanca(nome,cpf,senha,agencia,conta)
    return classe


def novo_cliente_corrente():
    nome = input('digite seu nome:')
    cpf = input('digite seu cpf:')
    senha = input('digite sua senha:')
    agencia = gerador_chave(6)
    conta = gerador_chave(5)

    classe = exer_3_cliente.cliente_corrente(nome,cpf,senha,agencia,conta)
    return classe


def dados_cliente(dicio):
    lista_cliente = [{'_nome': 'ana', '_cpf': '123456', '_senha': '12345', 'agencia': '444444', 'conta': '44444', 'saldo': 90,'limite': 0},
                    {'_nome': 'lucas', '_cpf': '123456', '_senha': '12345', 'agencia': '998915', 'conta': '53216', 'saldo': 70}]

    for num,item in enumerate(lista_cliente):
        if dicio['_nome'] == item['_nome'] and dicio['_cpf'] == item['_cpf'] and dicio['_senha'] == item['_senha']:
            return True,{f'{num}': item}

    return False,dicio


def login():
    # nome = input('digite seu nome :')
    # cpf = input('digite seu cpf :')
    # senha = input('digite sua senha :')
    # agencia = input('digite sua agencia :')
    # conta = input('digite sua conta :')
    nome = 'ana'
    cpf = '123456'
    senha = '12345'
    agencia = '444444'
    conta = '44444'

    classe = exer_3_cliente.cliente_corrente(nome,cpf,senha,agencia,conta)
    return classe




print('=============================')
print('    novo cliente = 1')
print('    login = 2')
print('    contato = 3')
print('=============================')
print()
op = input('digite seu opção de entrada :')
print()
print('=============================')

match op:
    case '1':
        print('conta corrente = cc')
        print('conta poupança = cp')
        print('==================================================')

        tipo = input('digite o tipo de conta :')
        print('=============================')

        if tipo == 'cc':
            novo = novo_cliente_corrente()
            lista_cliente.append(novo.__dict__)

        elif  tipo == 'cp':
            novo = novo_cliente_poupanca()
            lista_cliente.append(novo.__dict__)


    case '2':
        cliente = login()
        acesso = dados_cliente(cliente.__dict__)
        if acesso[0]:
            while True:
                item = acesso[1]['0']
                print()
                print(f'=========| conta ({item["conta"]}) ========| agencia ({item["agencia"]})')
                print(f'       seu saldo atual :{item["saldo"]}')
                print()
                print('========================================')
                op = input('digite sua opção :')

        else:
            print('essa conta n existe !')


    case '3':
        print(lista_cliente)


















