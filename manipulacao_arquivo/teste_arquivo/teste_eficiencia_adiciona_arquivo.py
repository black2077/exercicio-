import json
import pathlib


def crie_caminho( nome_arquivo):
    caminho = pathlib.Path(__file__).parent
    return caminho / nome_arquivo



def arquivo_linha(caminho_arquivo):
    with open(caminho_arquivo) as arquivo:
        yield from arquivo


cami = crie_caminho('arquivos/lista_1.json')


def arquivo_teste(nome, cpf, senha):
    lista = [json.loads(item) for item in arquivo_linha(cami)]


    with open(cami ,'w') as arquivo:
        for item in lista:

            if nome == item['nome'] and  cpf == item['cpf'] and senha == item['senha'] :
                pass
            else:
                json.dump(item,arquivo)
                arquivo.write('\n')





















# "nome": "anderson", "cpf": "39465385524", "senha": "1973"

p = arquivo_teste('anderson', '39465385524', '1973')
print(p)


