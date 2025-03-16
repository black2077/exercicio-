

import json
import pathlib
from abc import ABC,abstractmethod




class base_gerenciador(ABC):
    def __init__(self,pasta = '',subpasta = '',nome_arquivo = ''):
        self.pasta = pasta
        self.subpasta = subpasta
        self.nome_arquivo = nome_arquivo


    @abstractmethod
    def cria_caminho(self,pasta = '',subpasta = '', nome_arquivo = ''):...


    def lista_diretorios(self,caminho):
        return pathlib.Path.iterdir(caminho)

    def __enter__(self):
        return self
    

    def __exit__(self,exc_type,exc_val,exc_tb):
        pass




class gerenciador_diretorio(base_gerenciador):
    def __init__(self,pasta = '',subpasta = '',nome_arquivo = ''):
        self.pasta = pasta
        self.subpasta = subpasta
        self.nome_arquivo = nome_arquivo


    def cria_caminho(self,pasta = '',subpasta = '', nome_arquivo = ''):
        return pathlib.Path(__file__).parent / pasta / subpasta / nome_arquivo 


    def cria_diretorio(self,caminho):
        pathlib.Path.mkdir(caminho,exist_ok= True)

    def __enter__(self):
        return self
    

    def __exit__(self,exc_type,exc_val,exc_tb):
        pass
    



class gerenciador_arquivo(base_gerenciador):
    def __init__(self,pasta = '',subpasta = '',nome_arquivo = ''):
        self.pasta = pasta
        self.subpasta = subpasta
        self.nome_arquivo = nome_arquivo


    def cria_caminho(self, pasta='', subpasta='', nome_arquivo=''):
        caminho = pathlib.Path(__file__).parent / pasta / subpasta / nome_arquivo 

        if not self.checa_existencia_arquivo(caminho):
            return caminho 
        
        return False
        
    def checa_existencia_arquivo(self,caminho):
        if pathlib.Path.exists(caminho):
            return False
        
        return False


    def carrega_arquivo(self,caminho):
        self.arquivo = open(caminho)
        yield from self.arquivo

    def adicionar_arquivo(self,dicio,caminho):
        self.arquivo = open(caminho,'a')
        json.dump(dicio,self.arquivo)
        self.arquivo.write('\n')


    def __enter__(self):
        return self
    

    def __exit__(self,exc_type,exc_val,exc_tb):
        if hasattr(self,'arquivo'):
            self.arquivo.close()
            del self.arquivo





with gerenciador_arquivo() as arquivo, gerenciador_diretorio() as diretorio:
    caminho_diretorio = diretorio.cria_caminho('lista_teste')
    diretorio.cria_diretorio(caminho_diretorio)

    caminho_arquivo = arquivo.cria_caminho('lista_teste','lista.json')
    arquivo.adicionar_arquivo({'nome':'ana'},caminho_arquivo)























