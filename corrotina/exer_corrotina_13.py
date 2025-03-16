

import asyncio
import pathlib
import json
from random import randint
import time



class Arquivo_assicrono:
    def __init__(self,pasta,subpasta,nome_arquivo):
        self.pasta = pasta
        self.subpasta = subpasta
        self.nome_arquivo = nome_arquivo
        self.caminho = self.crie_caminho(pasta,subpasta,nome_arquivo)
        
        
    def crie_caminho(self,pasta,subpasta,nome_arquivo):
        caminho = pathlib.Path(__file__).parent / pasta / subpasta / nome_arquivo
        return caminho 
        
        
    def carrega_linha(self,caminho):       
        self.arquivo = open(caminho)
        yield from self.arquivo 
    
    
    async def buscar_chaves(self,cliente_dicio): 
        
        for item in self.carrega_linha(self.caminho):
            dicio = json.loads(item)
            if dicio['nome'] == cliente_dicio['nome'] and dicio['cpf'] == cliente_dicio['cpf'] and dicio['senha'] == cliente_dicio['senha']:
                return dicio
           

    async def buscar_indice(self,indice): 
        for num,item in enumerate(self.carrega_linha(self.caminho)):
            if num == indice :
                dicio = json.loads(item)
                return {num:dicio}
           


    def adiciona(self,dicio,caminho):
        self.arquivo = open(caminho,'a')
        json.dump(dicio,self.arquivo)
    
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self,exc_type,exc_value,traceback):
        if hasattr(self,'arquivos'):
            self.arquivos.close()





async def carrega(pasta,subpasta,nome_arquivo =''):
    async with Arquivo_assicrono(pasta,subpasta,nome_arquivo) as arquivo:
        dicio = {'nome': 'daniel', 'cpf': '52005892232', 'senha': '4175'}
        return await arquivo.buscar_chaves(dicio)
            


async def carrega_indice(indice,pasta,subpasta,nome_arquivo =''):
    async with Arquivo_assicrono(pasta,subpasta,nome_arquivo) as arquivo:
        return await arquivo.buscar_indice(indice)




async def teste():
    
    return await asyncio.gather(*[carrega_indice(randint(100,10000),'arquivos','lista_1.json') for item in range(20)])

lista = asyncio.run(teste())

for item in lista:
    print(item)
















