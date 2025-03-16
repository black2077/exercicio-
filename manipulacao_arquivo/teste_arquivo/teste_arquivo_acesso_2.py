
import json


class Cliente_Acesso:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


class Cliente:
    def __init__(self,nome,cpf,senha,saldo,conta,banco):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo
        self.conta = conta
        self.banco = banco

    def sacar(self,valor):
        self.saldo -= valor

    def deposito(self,valor):
        self.saldo += valor

# ============

class Arquivo:
    def __init__(self,diretorio,cls):
        self.diretorio = diretorio
        self.usuario = cls

    def arquivos(self):
        with open(self.diretorio) as arquivo:
            return  [json.loads(item) for item in arquivo]


    def procura(self):
        lista = self.arquivos()
        for num,item in enumerate(lista):
            if self.usuario['nome'] == item['nome'] and self.usuario['cpf'] == item['cpf'] and self.usuario['senha'] == item['senha']:
                self.indice,self.arquivo = num,item
                return True


    def edita_arquivo(self,novo_arquivo):
        with open(self.diretorio,'w') as arquivo:
            self.arquivos[self.indice] = novo_arquivo
            lista = [json.dumps(item) +'\n' for item in self.arquivos]
            arquivo.writelines(lista)
        del self.arquivos,self.indice


class Acesso_Banco_Dados(Arquivo):
    def __init__(self,diretorio,cls_acesso):
        super().__init__(diretorio,cls_acesso)

        acesso_arquivo = Arquivo(diretorio,cls_acesso)
        if acesso_arquivo.procura():
            self.info = acesso_arquivo.arquivo

    def acesso_info(self):
        return [item for item in self.info.values()]

# ============

if __name__ == '__main__':
    while True:
        print('=' * 23)
        nome = input('digite seu nome:')

        print('=' * 23)
        cpf = input('digite seu cpf :')

        print('=' * 23)
        senha = input('digite sua senha :')

        cliente_acessa = Cliente_Acesso('an','12345678','1234')

        arqui = Acesso_Banco_Dados('lista_clientes.json',cliente_acessa.__dict__)
        if arqui.procura():
        # ==============
            while True:
                acesso_cliente = Cliente(*arqui.acesso_info())
                print('=' * 60)
                print('   | (deposito - dp) | (saque - sq) | (extrato - xtr) |')
                print('=' * 60)
                opicao = input('o que deseja ?:')

                match opicao:
                    case 'deposito'|'dp':
                        print('========+deposito+=========')
                        valor = int(input('digite o valor :'))
                        acesso_cliente.deposito(valor)

                    case 'saque' | 'sq':
                        valor = int(input('digite o valor :'))
                        acesso_cliente.sacar(valor)

                    case 'extrato' |'xtr':
                        print('foi')




