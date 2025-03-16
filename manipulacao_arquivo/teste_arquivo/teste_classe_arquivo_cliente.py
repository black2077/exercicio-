import json
import os



class ClienteAcesso:
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


class Arquivo:
    def __init__(self, diretorio: str, cls:ClienteAcesso):
        self.diretorio = diretorio

        if os.path.isfile(self.diretorio):
            if isinstance(cls, ClienteAcesso):
                self.cls = cls .__dict__
                self.__acesso = self.procura()
            else:
                raise 'erro de classe'

        else:
            raise 'diretorio erro'

    def carrega_arquivos(self):
        with open(self.diretorio) as lista_arquivo:
            return [json.loads(item) for item in lista_arquivo]

    def adiciona_arquivo(self,dicio):
        with open(self.diretorio,'a') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')

    def procura(self):
        lista_arquivo = self.carrega_arquivos()

        for indic,itens in enumerate(lista_arquivo):
            if self.cls['nome'] == itens['nome'] and self.cls['cpf'] == itens['cpf'] and self.cls['senha'] == itens['senha']:
                self.arquivo = itens
                self.indice = indic
                return True

    def delete_(self):
        lista_arquivo = self.carrega_arquivos()

        del lista_arquivo[self.indice]
        with open(self.diretorio,'w') as arquivo:
            [self.adiciona_arquivo(item) for item in lista_arquivo]

    def copia_seguranca(self,diretorio,lista):
        with open(diretorio,'w') as arquivo:
            lista_copia = [(json.dump(item,arquivo),arquivo.write('\n')) for item in lista]

    def edita_arquivo(self, dicio):

        def arquivo():
            try:
                lista = self.carrega_arquivos()
                self.copia_seguranca('backup_lista_clientes.json', lista)
                lista[self.indice] = dicio

                with open(self.diretorio, 'w') as arquivo:
                    lista = [self.adiciona_arquivo(item) for item in lista]

            except AttributeError:
                raise 'função não pode ser executada'

        arquivo()

    def lista_acesso(self):
        return [item for item in self.arquivo.values()]



nome = 'lui'
cpf = '7897645653'
senha = '123342354'

clien = ClienteAcesso(nome,cpf,senha)


li = Arquivo('lista_clientes.json',clien)

if li.procura():
    cliente_conta = Cliente(*li.lista_acesso())
    lista = li.__dict__
    li.edita_arquivo(cliente_conta.__dict__)
    li.copia_seguranca()
    print(lista['cls'])
    print(lista['arquivo_registro'])
    print(lista['indice'])
    print(lista['_Arquivo__acesso'])

print(li.__dict__)



































