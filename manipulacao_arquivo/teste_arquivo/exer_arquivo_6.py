import json
import os.path



class ClienteAcesso:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


class Arquivo:
    def __init__(self,diretorio: str,classe: ClienteAcesso):
        self.__diretorio = diretorio
        if os.path.isfile(self.__diretorio):
            self.classe = classe

            if isinstance(self.classe,ClienteAcesso):
                self.classe = classe.__dict__
                self.arquivos_lido = self.__ler_arquivo()
                self.arquivo = None
                self.__procuro()

            else:
                raise 'objeto incompatível'

        else:
            raise 'O arquivos não existe.'


    def __ler_arquivo(self):
        with open(self.__diretorio,encoding='utf8') as arquivo:
            return [json.loads(item) for item in arquivo]


    def __procuro(self):
        for num,item in enumerate(self.arquivos_lido):
            if self.classe['__nome'] == item['__nome'] and self.classe['__cpf'] == item['__cpf'] and self.classe['__senha'] == item['__senha']:
                self.indice = num
                self.arquivo = self.arquivos_lido[num]
                del self.arquivos_lido
                return True

        del self.arquivos_lido


    def __adiciona_arquivo(self,dicio):
        with open(self.__diretorio, 'a', encoding='utf8') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')


    def delete_arquivo(self):
        del self.arquivos_lido[self.indice]
        with open(self.__diretorio, 'w') as arquivo:
            for item in self.arquivos_lido:
                self.__adiciona_arquivo(item)
        del self.arquivos_lido


    def acesso_arquivo(self):
        if self.__procuro():
            lista = [self.arquivo['__nome'],self.arquivo['__cpf'],self.arquivo['__senha'],
                     self.arquivo['__saldo'],self.arquivo['usuario'],self.arquivo['agencia']]

            return lista



cliente = ClienteAcesso('luan','34234324234','675464345343')




def conecao_banco(func,cls):
    arq = func('lista_test_2.json',cls)
    dicio = arq.__dict__

    try:
        print(dicio['_Arquivo__diretorio'])
        print(dicio['classe'])
        print(dicio['arquivos'])
        print(item for item in arq.arquivos_lido)

    finally:
        return dicio




conecao_banco(Arquivo,cliente)


