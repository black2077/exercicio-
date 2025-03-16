import json
import os



class gerenciador_diretorio:
    def __enter__(self):
        return self

    def cria_caminho(self,*pasta_caminho):
        return os.path.join(*pasta_caminho)

    def lista_diretorios(self,caminhos):
        caminho = self.cria_caminho(*caminhos)
        return os.listdir(caminho)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print()


class gerenciador_arquivo:
    def __init__(self,diretorios):
        self.diretorio = self.cria_caminho(*diretorios)

    def __enter__(self):
        return self

    def cria_caminho(self, *diretorios):
        return os.path.join(*diretorios)

    def busca_arquivo(self,caminho,cpf,senha):
        with open(caminho) as arquivo:
            numero = 0
            try:
                while True:
                    dados = json.loads(arquivo.readline())
                    if dados['cpf'] == cpf and dados['senha'] == senha:
                        return {f'{numero}': dados}
                    numero +=1

            except json.decoder.JSONDecodeError:
                pass

    def lista_arquivos(self,caminho):
        with open(caminho) as arquivo:
            return [json.loads(item) for item in arquivo]

    def medidor_tamanho_arquivos(self,diretorios):
        caminho = self.cria_caminho(diretorios)
        return len(self.lista_arquivo(caminho))

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# \Users\johnr\PycharmProjects\exercicio\manipulacao_arquivo\Context_Manager\lista

# with gerenciador_diretorio() as diretorio:
#     print()


caminho = ['/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo','Context_Manager', 'lista', 'lista_teste.json']

caminho_pasta = ['/Users', 'johnr', 'PycharmProjects', 'exercicio', 'manipulacao_arquivo','Context_Manager', 'lista']


with gerenciador_arquivo(caminho) as arquivo:
    
    with gerenciador_diretorio() as  pasta:
        print(pasta.lista_diretorios(caminho_pasta))
    # print(arquivo.medidor_tamanho_arquivo(arquivo.diretorio))




