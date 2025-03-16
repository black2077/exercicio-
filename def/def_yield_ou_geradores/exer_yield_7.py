
import pathlib
import json



def cria_caminho(pasta,nome_arquivo):
    return pathlib.Path(__file__).parent.parent / pasta / nome_arquivo


def gerador_arquivo(pasta,nome_arquivo):
    caminho = pathlib.Path(__file__).parent.parent / pasta / nome_arquivo
    
    with open(caminho) as arquivo:
        
        for num,item in enumerate(arquivo):
            numero = yield 
            if numero == num:
                yield item
                

def meu_gerador_indi():
    mensagem = yield 

    lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    while len(lista) >= mensagem:
        mensagem = yield lista[mensagem]

        print('==')


def meu_gerador(caminho):

    while True:
        with open(caminho) as arquivo:
            
            indice = yield
            for num,item in enumerate(arquivo):
                
                dicio = item
                
                if indice == num:
                    yield dicio 
                    
                arquivo.seek(0,0)



def meu_gerador_w(caminho):
    with open(caminho) as arquivo:
        lista = list(json.loads(item) for item in arquivo)
        
        while True:
            indice = yield
            item = yield lista[indice]


caminho = cria_caminho('arquivos_pra_teste','lista.json')

kj = meu_gerador_w(caminho)

next(kj)

print(kj.send(9))
print(kj.send(10))
print(kj.send(9))
