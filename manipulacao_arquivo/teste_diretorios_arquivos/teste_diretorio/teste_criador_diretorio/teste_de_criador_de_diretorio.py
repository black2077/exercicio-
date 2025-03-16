import os


class Gerenciamento_diretorio:
    def __init__(self, *caminho):
        self.caminho_ = self.caminho_arquivo(*caminho)

    def caminho_arquivo(self, *caminho):
        return os.path.join(*caminho)

    def lista_arquivos_em_diretorio(self):
        with os.scandir(self.caminho_) as diretorio:
            lista = []
            for item in diretorio:
                if item.name.endswith('.json'):
                    lista.append(item.name)

        return lista

    def cria_arquivo(self, nome_do_arquivo, *diretorio):
        caminho = self.caminho_arquivo(*diretorio)+'\\'+nome_do_arquivo
        with open(caminho, 'w') as arquivo:
            pass

    def cria_diretorio(self,nome_de_diretorio,*caminho):
        caminho_do_diretorio = self.caminho_arquivo(*caminho)+'\\'+nome_de_diretorio
        os.makedirs(caminho_do_diretorio)



# \Users\johnr\PycharmProjects\exercicio\manipulacao_arquivo

jh = Gerenciamento_diretorio('/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo',
                             'teste_criador_diretorio')

jh.cria_arquivo('lista_tudo.json', '/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo',
                'teste_criador_diretorio','diretorio')
jh.cria_diretorio('diretorio_3','/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo','teste_criador_diretorio')

print(jh.lista_arquivos_em_diretorio())
print(jh.__dict__)
