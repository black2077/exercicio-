import json
import pathlib



def cria_caminho(pasta,arquivo):
    cami = pathlib.Path(__file__).parent.parent / pasta /arquivo
    return cami



def leitura_linhas_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            yield json.loads(linha)


def ler_arquivos(caminho):
    yield from open(caminho)



cami = cria_caminho('arquivos_pra_teste','lista.json')

lista =  ler_arquivos(cami)



for item in ler_arquivos(cami):
    print(item)



# print(lista_2)
# print(next(leitura_linhas_arquivo(cami)))
# print(lista)






























