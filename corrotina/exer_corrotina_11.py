
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
        caminho = self.caminho / nome_arquivo
        self.arquivos = open(caminho)
        yield from self.arquivos

    async def buscar(self, nome, cpf, senha,nome_arquivo):
        for num, item in enumerate(self.carrega_linha(nome_arquivo)):
            dicio = json.loads(item)

            if dicio['nome'] == nome and dicio['cpf'] == cpf and dicio['senha'] == senha:
                return {num: dicio}

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if hasattr(self,'arquivos'):
            self.arquivos.close()


async def teste_1(nome,cpf,senha):
    async with AsyncContextManager('arquivos') as arquivo:
        return await arquivo.buscar(nome,cpf,senha,'lista_1.json')


async def teste_2():
    return await asyncio.gather(teste_1('ana','5345345','adaw'),teste_1('ruan','5345345','adaw'))



if __name__ == "__main__":
    lis = teste_2()
    lista = asyncio.run(lis)
    print(lista)





















