
import json
from teste_arquivo_acesso import monitora_velocidade_memoria







class cliente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    def deposito(self,valor):
        self.saldo += valor


cliente_1 = cliente('ana','45435345543','432422')
cliente_2 = cliente('luana', '4787657463', '467562')
cliente_3 = cliente('lua','47856465455','654655')

# ==========================================
class Arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio


    def arquivos(self):
        with open(self.diretorio) as arquivo:
            return  [json.loads(item) for item in arquivo]


    def procura(self,usuario):
        lista = self.arquivos()
        for num,item in enumerate(lista):
            if usuario['nome'] == item['nome'] and usuario['cpf'] == item['cpf'] and usuario['senha'] == item['senha']:
                self.lista_arquivos = lista
                self.indice = num

    def edita_arquivo(self,usuario):
        self.lista_arquivos[self.indice] = usuario
        with open(self.diretorio,'w') as arquivo:
            for item in self.lista_arquivos:
                json.dump(item,arquivo)
                arquivo.write('\n')

        del self.lista_arquivos,self.indice

@monitora_velocidade_memoria
def teste_class(cls):
    print('=' * 50)
    cls.deposito(900)
    af = Arquivo('lista_clientes.json')
    af.procura(cls.__dict__)
    af.edita_arquivo(cls.__dict__)
    print(cls.__dict__)
    print(af.__dict__)
    print('='*50)


# =========================================
class Arquivo_2:
    def __init__(self,diretorio):
        self.diretorio = diretorio


    def __arquivos(self):
        with open(self.diretorio) as arquivo:
            return {f'{num}': json.loads(item) for num,item in enumerate(arquivo)}


    def procura(self,usuario):
        lista = self.__arquivos()
        for num,item in lista.items():
            if usuario['nome'] == item['nome'] and usuario['cpf'] == item['cpf'] and usuario['senha'] == usuario['senha']:
                self.indice = num
                self.arquivos = lista


    def edita_arquivo(self,novo_arquivo):
        with open(self.diretorio,'w') as arquivo:
            self.arquivos[self.indice] = novo_arquivo
            lista = [json.dumps(item) +'\n' for item in self.arquivos.values()]
            arquivo.writelines(lista)

        del self.arquivos,self.indice

@monitora_velocidade_memoria
def teste_class_2(cls):
    print('=' * 50)
    teste_de_arquivo_2 = Arquivo_2('lista_clientes.json')
    teste_de_arquivo_2.procura(cls.__dict__)
    teste_de_arquivo_2.edita_arquivo(cls.__dict__)
    print(cls.__dict__)
    print(teste_de_arquivo_2.__dict__)
    print('=' * 50)

# ===========================================
class Arquivo_3:
    def __init__(self,diretorio):
        self.diretorio = diretorio


    def arquivos(self):
        with open(self.diretorio) as arquivo:
            return  [json.loads(item) for item in arquivo]


    def procura(self,usuario):
        lista = self.arquivos()
        for num,item in enumerate(lista):
            if usuario['nome'] == item['nome'] and usuario['cpf'] == item['cpf'] and usuario['senha'] == item['senha']:
                self.arquivos,self.indice = lista ,num


    def edita_arquivo(self,novo_arquivo):
        with open(self.diretorio,'w') as arquivo:
            self.arquivos[self.indice] = novo_arquivo
            lista = [json.dumps(item) +'\n' for item in self.arquivos]
            arquivo.writelines(lista)

        del self.arquivos,self.indice

@monitora_velocidade_memoria
def teste_class_3(cls):
    print('=' * 50)
    teste_de_arquivo_2 = Arquivo_2('lista_clientes.json')
    teste_de_arquivo_2.procura(cls.__dict__)
    teste_de_arquivo_2.edita_arquivo(cls.__dict__)
    print(cls.__dict__)
    print(teste_de_arquivo_2.__dict__)
    print('=' * 50)




teste_class(cliente_1)
teste_class_2(cliente_2)
teste_class_3(cliente_3)



