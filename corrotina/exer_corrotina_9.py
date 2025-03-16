import asyncio
import pathlib
from exer_corrotina_7 import Arquivo


async def copio_arquivo(pasta_1,arquivo,pasta_backup):
    with Arquivo() as arqui:
        caminho = arqui.caminho / pasta_1 / arquivo
        novo_caminho = arqui.caminho / pasta_backup / arquivo

        lista = [item for item in arqui.lista_arquivo(caminho)]
        [arqui.adiciona(novo_caminho,item) for item in lista]


async def informacao_diretorio(pasta):
    with Arquivo() as arqui:
        await asyncio.sleep(0)
        item = arqui.lista_diretoio(pasta)
        return item


async def arquivos(pasta,arquivo):
    
    with Arquivo() as arqui:
        caminho = arqui.caminho / pasta / arquivo

        if arqui.verifica_existencia(caminho):
            return [item for item in arqui.lista_arquivo(caminho)]

        else:
            print(caminho)


async def executa_todo():
    resultado = await asyncio.gather(informacao_diretorio('arquivos'),informacao_diretorio('backup_arquivos'),arquivos('arquivos','lista_2.json'),arquivos('arquivos','lista_1.json'))

    return resultado


item = asyncio.run(executa_todo())


for id in item:
   print(id)









