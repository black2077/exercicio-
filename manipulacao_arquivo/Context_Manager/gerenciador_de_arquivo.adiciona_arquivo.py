# import json
import pathlib



def arquivo():

    caminho = pathlib.Path(__file__).parent / 'lista' /'lista_teste.json'
    # with open(arquivo, 'r') as f:
    #     linhas = f.readlines()

    with open(caminho, '+r') as f:
        for index, linha in enumerate(f.readline()):

            if index == 2:
                del linha

                # print(linha)
                # del f.readline()
                print(f.readline())





























