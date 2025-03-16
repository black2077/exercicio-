

import json

# class Arquivo:
#     def __init__(self,cls):
#         self.cls = cls.__dict__
#         self.__arquivo = self._le_arquivos()
#
#     def _le_arquivos(self):
#         with open('banco_contas_correntes.json') as arquivos:
#             return [ json.loads(item) for item in arquivos ]
#
#     def acesso_cliente(self):...
#
#     def edita_arquivo(self):
#         with open('banco_contas_correntes.json', 'a') as arquivos:
#             json.dump(self.cls, arquivos)
#             arquivos.write('\n')
#
#     def delete_conta(self):
#         del self.__arquivo[resultado[0]]
#
#         for item in self.__arquivo:
#             print(item)
#
#     def adiciona_base_dados(self,dicio):
#         with open('banco_contas_correntes.json', 'a') as arquivos:
#             json.dump(dicio, arquivos)
#             arquivos.write('\n')
#
#     def mostra_conta(self):
#         print('foi edita_arquivo')
#         print(self.__dict__)
#
#     def procuro_arquivo(self):
#         for num,item in enumerate(self.__arquivo):
#             if  self.cls['__nome'] == item['__nome'] and self.cls['__cpf'] == item['__cpf'] :
#                 if self.cls['__senha'] == item['__senha'] and self.cls['usuario'] == item['usuario']:
#                     return [num,item]
# class Arquivo:
#     def __init__(self, cls):
#         self.cls = cls.__dict__
#         self.arquivos = self.le_arquivo()
#
#     def le_arquivo(self):
#         with open('banco_contas_correntes.json') as arquivos:
#             return [json.loads(item) for item in arquivos]
#
#     def aplico_funcao(self, funcao):
#         return [funcao(item) for item in self.arquivos]
#
#     def adiciona_base_dados(self, dicio):
#         with open('banco_contas_correntes.json', 'a') as arquivos:
#             json.dump(dicio, arquivos)
#             arquivos.write('\n')
#
#     def delete(self):
#         resultado = self.procuro_arquivo()
#         with open('banco_contas_correntes.json','w') as arquivos:
#             pass
#
#         del self.arquivos[resultado]
#         self.aplico_funcao(self.adiciona_base_dados)
#
#     def procuro_arquivo(self):
#         for num, item in enumerate(self.arquivos):
#             if self.cls['__nome'] == item['__nome'] and self.cls['__cpf'] == item['__cpf']:
#                 if self.cls['__senha'] == item['__senha'] and self.cls['usuario'] == item['usuario']:
#                     return num
#
# dicio = {'__nome': 'ana','__cpf' : '6743534534','__senha': '098998'}

class Arquivo:
    def __init__(self,diretorio: str,classe: dict):
        self.__diretorio = diretorio
        self.classe = classe
        self.__arquivos_lido = self.__ler_arquivo()

    def __ler_arquivo(self):
        with open(self.__diretorio) as arquivo:
            return [json.loads(item) for item in arquivo]

    def procuro(self):
        for num,item in enumerate(self.__arquivos_lido):
            if self.classe['__nome'] == item['__nome'] and self.classe['__cpf'] == item['__cpf'] \
                and self.classe['__senha'] == item['__senha']:
                self.indice = num
                self.arquivo = self.__arquivos_lido[num]
                # del self.arquivos_lido
                return True

        del self.__arquivos_lido

    def __adiciona_arquivo(self,dicio):
        with open(self.__diretorio, 'a', encoding='utf8') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')

    def delete_arquivo(self):
        del self.__arquivos_lido[self.indice]
        with open(self.__diretorio, 'w') as arquivo:
            for item in self.__arquivos_lido:
                self.__adiciona_arquivo(item)
        del self.__arquivos_lido


    def acesso_arquivo(self):
        if self.procuro():
            # del self.arquivos_lido
            lista = [self.arquivo['__nome'],self.arquivo['__cpf'],self.arquivo['__senha'],
                     self.arquivo['__saldo'],self.arquivo['usuario'],self.arquivo['agencia']]

            return lista


class ClienteAcesso:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


if __name__ == '__main__':

    clie = ClienteAcesso('ana', '6743534534', '098998')
    arq = Arquivo('banco_contas_correntes.json', clie.__dict__)
    if arq.procuro():
        print('entrando em usuario')
        arquivo_cli = arq.acesso_arquivo()
        cliente = classes_usuario.Usuario_Poupanca(*arquivo_cli)
        # pasta.delete_arquivo()
        print(cliente.__dict__)
        print(arq.__dict__)


    else:
        print('usuario não encontrada')
        # print(cliente_acesso.__dict__)
        print(arq.__dict__)




