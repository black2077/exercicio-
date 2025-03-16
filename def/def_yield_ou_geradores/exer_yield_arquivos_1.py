import json
import pathlib
import time
import psutil
import os

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
    def __init__(self,pasta,arquivo):
        self.pasta = pasta
        self.arquivo = arquivo
        self.caminho = self.cria_caminho(pasta,arquivo)

    def cria_caminho(self,pasta,arquivo) -> str:
        novo = pathlib.Path(__file__).parent.parent / pasta /arquivo
        return novo

    def linha_arquivo(self,caminho :str):
        yield from open(caminho)


    def busco(self,item,dicio):
        if item['nome'] == dicio['nome'] and item['nome'] == dicio['nome']:
            return dicio

    def filtra(self,lista):
        for num,item in enumerate(lista):
            if item !=  None:
                return {f'{num}': item}




class Arquivo_2:
    def __init__(self,pasta,arquivo):
        self.pasta = pasta
        self.arquivo = arquivo
        self.caminho = self.cria_caminho(pasta, arquivo)

    def cria_caminho(self,pasta,arquivo) -> str:
        novo = pathlib.Path(__file__).parent.parent / pasta /arquivo
        return novo

    def linha_arquivo(self,caminho :str):
        with open(caminho) as arquivo:
            return [json.loads(item) for item in arquivo]


    def busco(self,item,dicio):
        if item['nome'] == dicio['nome'] and item['nome'] == dicio['nome']:
            return dicio

    def filtra(self,lista):
        for num,item in enumerate(lista):
            if item !=  None:
                return {f'{num}': item}



item = {'conta' : '375275', 'nome': 'diego'}


@monitora_velocidade_memoria
def arquivo_teste_1(item):
    fd = Arquivo('arquivos_pra_teste','lista_1.json')
    caminho = fd.cria_caminho('arquivos_pra_teste','lista_1.json')
    lista = [(fd.busco(item,json.loads(item_))) for item_ in fd.linha_arquivo(caminho)  ]
    return fd.filtra(lista)
    # print(lista,len(lista))
    # print(fd.cria_caminho('arquivos_pra_teste','lista_1.json'))
    # print(fd.__dict__)



@monitora_velocidade_memoria
def arquivo_teste_2(item):
    fd = Arquivo_2('arquivos_pra_teste','lista_1.json')
    caminho = fd.cria_caminho('arquivos_pra_teste','lista_1.json')
    lista = [(fd.busco(item,item_)) for item_ in fd.linha_arquivo(caminho) ]
    return fd.filtra(lista)
    # print(fd.filtra(lista))
    # print(lista,len(lista))
    # print(fd.cria_caminho('arquivos_pra_teste','lista_1.json'))
    # print(fd.__dict__)


arq = arquivo_teste_1(item)

arq_2 = arquivo_teste_2(item)

print(arq)
print(arq_2)







