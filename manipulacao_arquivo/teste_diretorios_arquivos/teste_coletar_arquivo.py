

import json
import pathlib



class Arquivo_base:
    def __init__(self,pasta,subpasta,nome_arquivo):
        self.caminho = self.cria_caminho(pasta,subpasta,nome_arquivo)

    def checa_existencia(self,caminho_arquivo):
        if pathlib.Path.exists(caminho_arquivo):
            return True


    def cria_caminho(self,pasta,subpasta,nome_arquivo):
        caminho = pathlib.Path(__file__).parent/ pasta / subpasta / nome_arquivo

        if self.checa_existencia(caminho):
            return caminho

        raise 'não existente'


    def arquivos(self):
        self.arquivo = open(self.caminho)
        yield from self.arquivo


    def __filtra(self,item):
        valor : dict = json.loads(item)
        del valor['preco_lote'],valor['contidade'],valor['preco_unidade'],valor['lote'],valor['data_entrega'],valor['frete']
        return valor


    def busca_produtos(self,chave1,chave2='',chave3=''):
        lista = []
        for num,item in enumerate(self.arquivos()):
            dicio = self.__filtra(item)
            if chave1 in dicio.values() or chave2 in dicio.values() or chave3 in dicio.values():
                lista.append(dicio)

        return lista


    def busca_id(self,id):
        for item in self.arquivos():
            dicio = self.__filtra(item)
            if dicio['id'] == id:
                return dicio


    def busca_visitante(self,classe):
        for item in self.arquivos():
            dicio = json.loads(item)
            if dicio['IP'] == classe['IP'] and dicio['id'] == classe['id']:
                return (True,dicio)

        return (False,None)


    def busca_usuario(self,classe):
        for num,item in enumerate(self.arquivos()):
            dicio = json.loads(item)
            if dicio['IP'] == classe['IP'] and dicio['id'] == classe['id'] and dicio['_nome'] == classe['_nome'] and dicio['_cpf'] == classe['_cpf'] and dicio['_senha'] == classe['_senha']:
                return (num,dicio)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self,'arquivo'):
            self.arquivo.close()
            del self.arquivo






with Arquivo_base('produtos','eletrodomestico.json','') as arquivo:
    
    print(arquivo.busca_id('66666'))
    
    




