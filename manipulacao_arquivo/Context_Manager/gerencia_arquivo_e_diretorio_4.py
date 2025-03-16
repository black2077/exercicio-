import json
import pathlib
import os
import time
import psutil


tempo = 0

def monitora_velocidade_memoria(func):
    def wrapper(*args, **kwargs):
        global tempo
        t1 = time.time()
        process = psutil.Process(os.getpid())
        mem1 = process.memory_info().rss / 1024 / 1024
        result = func(*args, **kwargs)
        t2 = time.time()

        process = psutil.Process(os.getpid())
        mem2 = process.memory_info().rss / 1024 / 1024
        tempo = t2-t1

        print(f"A função {func.__name__}   levou {t2 - t1} segundos para executar e usou {mem2 - mem1} MB de memória.")
        return result
    return wrapper



class Arquivo:
    def __init__(self, diretorio_iguia = ''):
        self.diretorio = self.cria_caminho(diretorio_iguia)


    def cria_caminho(self,caminho):
        novo_caminho = pathlib.Path(__file__).parent / caminho
        return novo_caminho


    def cria_arquivo(self,nome_arquivo):
        caminho = self.diretorio / nome_arquivo
        if not self.verifica_existencia(caminho):
            self.arquivo = open(caminho,'w',encoding='utf8')


    def cria_diretorio(self,nome):
        caminho = self.diretorio / nome
        if not os.path.exists(caminho):
            os.mkdir(caminho)


    def lista_diretoio(self):
        return {'tamanho' : len(os.listdir(self.diretorio)), 'diretorios' : os.listdir(self.diretorio)}


    def lista_arquivo(self,nome_arquivo ='') :
        caminho = self.diretorio / nome_arquivo
        self.arquivo = open(caminho)
        yield from self.arquivo


    def adiciona(self,item, nome_arquivo =''):
        caminho = self.diretorio / nome_arquivo

        if isinstance(item,dict):
            self.arquivo = open(caminho , 'a',encoding='utf8')
            json.dump(item,self.arquivo)
            self.arquivo.write('\n')


    def busco_arquivo_filtro(self,func_filtro,chave,diretorio =''):
        lista = []

        for item in self.lista_arquivo(diretorio):
            dicio = json.loads(item)

            if func_filtro(dicio,chave):
                lista.append(dicio)

        return lista


    def busco_indice(self,indice,diretorio):
        novo = self.diretorio / diretorio
        for num,item in enumerate(self.lista_arquivo(novo)):
            if indice == num:
                return item


    def altera_arquivo(self, indice :int, novo_arquivo :dict, diretorio :str):

        if isinstance(indice,int) and isinstance(novo_arquivo,dict) and isinstance(diretorio,str):
            lista = [json.loads(item) for item in self.lista_arquivo(diretorio)]

            for num,item in enumerate(lista):
                if num == indice:
                    lista[indice] = novo_arquivo

            self.cria_arquivo(diretorio)
            [self.adiciona(item,diretorio) for item in lista ]


    def verifica_existencia(self,nome_arquivo):
        novo = self.diretorio / nome_arquivo
        if os.path.exists(nome_arquivo):
            return True
        else:
            return False


    def excluir(self,nome_arquivo):
        caminho = self.diretorio / nome_arquivo
        if self.verifica_existencia(caminho):
            os.remove(caminho)



    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()


class Arquivo_2:
    def __init__(self,caminho = ''):
        self.caminho = self.cria_caminho(caminho)

    def cria_caminho(self,caminho):
        novo_caminho = pathlib.Path(__file__).parent / caminho
        return novo_caminho


    def cria_arquivo(self,nome_arquivo):
        caminho = self.caminho / nome_arquivo
        # print(caminho)
        if self.verifica_existencia(caminho):
            with open(caminho,'w') as arquivo:
                arquivo.close()


    def cria_diretorio(self,nome):
        caminho = self.caminho.parent / nome
        if not os.path.exists(caminho):
            os.mkdir(caminho)


    def lista_diretoio(self,pasta=''):
        novo = self.caminho / pasta
        return {'tamanho' : len(os.listdir(novo)), 'diretorios' : os.listdir(novo)}


    def lista_arquivo(self,nome_arquivo):
        caminho = self.caminho / nome_arquivo
        with open(caminho) as arquivo:
            for item in arquivo:
                dicio = json.loads(item)
                yield dicio


    def adiciona(self,nome_arquivo,item):

        if os.path.exists(nome_arquivo):
            with open(nome_arquivo,'a') as arquivo:
                json.dump(item,arquivo)
                arquivo.write('\n')


    def busco_arquivo_nome(self,dicio,pasta,diretorio):
        caminho = arquivo.caminho / pasta /diretorio
        info = []

        for nun,item in enumerate(self.lista_arquivo(caminho)):
            dados = json.loads(item)
            if dicio['nome'] == dados['nome']:
                info.append({f'{nun}':dados})
                return info


    def busco_indice(self,indice,pasta,diretorio):
        novo = self.caminho / pasta / diretorio
        for num,item in enumerate(self.lista_arquivo(novo)):
            if indice == num:
                return item


    def altera_arquivo(self,indice,novo_arquivo,pasta,diretorio):
        novo_caminho = self.caminho / pasta / diretorio
        lista = [item for item in self.lista_arquivo(novo_caminho)]
        lista[indice] = novo_arquivo

        with open(novo_caminho,'w') as arquivo:
            [(json.dump(item,arquivo),arquivo.write('\n')) for item in lista]


    def verifica_existencia(self,nome_arquivo):
        if os.path.exists(nome_arquivo):
            return True
        else:
            return False


    def excluir(self,nome_arquivo):
        caminho = self.caminho / nome_arquivo
        if self.verifica_existencia(caminho):
            os.remove(caminho)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def busca_usuario(dicio,chave):
    if dicio.get('nome') == chave:
        return True

    else:
        return False




@monitora_velocidade_memoria
def teste_1():
    with Arquivo('lista') as arq:
        lista = [json.loads(item) for item in arq.lista_arquivo('lista_teste.json')]
        print(lista)

        arq.cria_arquivo('lista_teste_2.json')
        # arq.excluir('lista_teste_2.json')

        # arq.adiciona({},'lista_teste.json')
        # arq.altera_arquivo(2, {},  'lista_teste.json')

    return


@monitora_velocidade_memoria
def teste_2():
    with Arquivo_2('lista') as arq:
        lista = [item for item in arq.lista_arquivo('lista_teste.json')]
        print(lista)

        arq.cria_arquivo('lista_teste_2.json')
        # arq.excluir('lista_teste_2.json')

        # arq.adiciona('lista_teste.json',{})
        # arq.altera_arquivo(2,{},'','lista_teste.json')

    return

teste_2()
teste_1()




