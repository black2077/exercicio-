import asyncio
import pathlib
import json


class AsyncContextManager:
    def __init__(self, pasta):
        self.caminho = self.crie_caminho(pasta)


    def crie_caminho(self,nome_arquivo):
        caminho = pathlib.Path(__file__).parent
        return caminho / nome_arquivo


    def carrega_linha(self,nome_arquivo):
        self.arquivos = open(nome_arquivo)
        yield from self.arquivos


    async def buscar(self, nome, cpf, senha,nome_arquivo):
        caminho = self.caminho / nome_arquivo
        for num, item in enumerate(self.carrega_linha(caminho)):
            dicio = json.loads(item)

            if dicio['nome'] == nome and dicio['cpf'] == cpf and dicio['senha'] == senha:
                return await {num: dicio}


    async def adiciona_arquivos(self,nome_arquivo,dicio):
        caminho = self.caminho / nome_arquivo
        self.arquivos = open(caminho,'a')
        json.dump(dicio,self.arquivos)
        self.arquivos.write('\n')


    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if hasattr(self,'arquivos'):
            self.arquivos.close()



async def adiciona_arquivos(item,nome_arquivos):
    async with AsyncContextManager('arquivos') as arquivos:
        caminho = arquivos.caminho / nome_arquivos
        await arquivos.adiciona_arquivos(caminho,item)


async def executa_(lista,nome_arquivos):
    for item in lista:
        await adiciona_arquivos(item,nome_arquivos)


async def executa_todo(lista,nome_arquivos):
    
    return asyncio.gather(*[adiciona_arquivos(item,nome_arquivos) for item in lista])





lista = [{'nome' : 'ana' ,'cpf' : '94435354334','senha' : '4345'},{'nome' : 'luana' ,'cpf' : '94435354334','senha' : '4345'},{'nome' : 'mariana' ,'cpf' : '94435354334','senha' : '4345'},{'nome' : 'mario' ,'cpf' : '94435354334','senha' : '4345'}]

# executa_todo(lista,'lista_1.json')
asyncio.run(executa_todo(lista,'lista_1.json'))

# for item in lista:
#     print(*item.values())

