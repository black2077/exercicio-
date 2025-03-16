import json
import pathlib
from random import randint,choice


class Gerador_de_arquivo:
    def __init__(self,pasta,nome_arquivo):
        self.caminho = self.cria_caminho(pasta,nome_arquivo)

    def cria_caminho(self,pasta,arquivo=''):
        resultado = pathlib.Path(__file__).parent /pasta/ arquivo 
        return resultado 


    def cria_arquivo(self,nome_arquivo):
        self.caminho = self.caminho / nome_arquivo
        if self.filtro_de_arquivo(nome_arquivo,'.json') or self.filtro_de_arquivo(nome_arquivo,'.CSV'):
            self.arquivos = open(self.caminho,'w')


    def filtro_de_arquivo(self, nome_arquivo: str, extensão_de_arquivo):
        if extensão_de_arquivo in nome_arquivo:
            return True

        return False


    def gerador_de_usuario(self):
        caminho = self.cria_caminho('gerador_csv') / 'lista_de_nomes.CSV'
        lista_nomes = [item.rstrip('\n') for item in open(caminho)]
        item = choice(lista_nomes)

        return {'nome': item ,'cpf': self.gerador_de_numeros(11),'senha':self.gerador_de_numeros(4)}


    def gerador_de_numeros(self,tamanho):
        return ''.join(str(randint(0,9)) for _ in range(0,tamanho))


    def adiciona_nomes_arquivo_csv(self,nome):
        caminho = self.cria_caminho('gerador_csv') / 'lista_de_nomes.CSV'
        self.arquivos_csv = open(caminho,'a')
        self.arquivos_csv.write(nome)
        self.arquivos_csv.write('\n')


    def carrega_linha(self):
        self.arquivos = open(self.caminho)
        yield from self.arquivos


    def buscar(self,nome,cpf,senha):
        for num,item in enumerate(arquivo.carrega_linha()):
            dicio = json.loads(item)

            if dicio['nome'] == nome and dicio['cpf'] == cpf and dicio['senha'] == senha:
               return {num : dicio}


    def adiciona_arquivo_json(self,dicio):
        self.arquivos = open(self.caminho,'a',encoding='utf8')
        json.dump(dicio,self.arquivos)
        self.arquivos.write('\n')


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, "arquivos") :
            self.arquivos.close()

        elif hasattr(self,"arquivos_csv"):
            self.arquivos_csv.close()




# def interface():
#     with Gerador_de_arquivo('gerador_json',) as arquivo:
#         # arquivo.cria_arquivo('lista_1.json')
#         print(arquivo.gerador_de_usuario())
#         print(arquivo.gerador_de_numeros(10))
#         print(arquivo.caminho)
#         pass


def gerador_para_arquivos(tamanho):
    with Gerador_de_arquivo('gerador_json','lista_1.json') as arquivo:
        for item in range(tamanho):
            arquivo.adiciona_arquivo_json(arquivo.gerador_de_usuario())

    print('pronto')


# objetos_e_classes()
gerador_para_arquivos(5000)


with Gerador_de_arquivo('gerador_json','lista_1.json') as arquivo:
    print(arquivo.__dict__)




















