
import os
import pathlib
import datetime
import json






class Editor_de_Arquivo:
    def __init__(self,diretorio ='',mes_diretorio='',nome_arquivo=''):
        self.diretorio = diretorio
        self.sub_diretorio = mes_diretorio
        self.nome_arquivo = nome_arquivo

    def cria_arquivo(self,caminho_de_arquivo):
        with open(caminho_de_arquivo, 'a',encoding='utf-8') as arquivo:
            arquivo.close()


    def crie_diretorio(self, nome_diretorio):
        os.makedirs(nome_diretorio, exist_ok=True)


    def lista_nome_de_diretorio(self, diretorio):
        return os.listdir(diretorio)


    def pega_data(self):
        return datetime.datetime.now().strftime("%d/%m/%Y").replace('/','_')


    def pega_dia(self):
        data = self.pega_data()      
        return data[0:2]


    def pega_mes(self):
        data = self.pega_data()  
        return data[3:5]


    def pega_ano(self):
        data = self.pega_data()  
        return data[6:10]


    def editar_arquivo(self,indice,novo_arquivo):
        lista = [json.loads(item) for item in self.carrego_arquivo(self.caminho)]
        if isinstance(novo_arquivo,dict):
            lista[indice] = novo_arquivo
            arquivo_limpo = open(self.caminho,'w')
            arquivo_limpo.close()

            [self.adiciona_em_arquivo(item,self.caminho) for item in lista]

    

    def crie_caminho(self,diretorio,subdiretorio= '' ,nome_arquivo=''):
        return pathlib.Path(__file__).parent / diretorio / subdiretorio / nome_arquivo


    def carrego_arquivo(self,caminho):
        self.arquivo = open(caminho)
        yield from self.arquivo


    def checa_caminho_de_arquivo(self,caminho):    
        if pathlib.Path.is_file(caminho):
            return True
        
        
        return False


    def checa_caminho_de_diretorio(self,caminho):
        if pathlib.Path.is_dir(caminho):
            return True
        
        
        return False


    def adiciona_em_arquivo(self,dicio,caminho):   
        self.arquivo = open(caminho,'a',encoding='utf-8')
        json.dump(dicio,self.arquivo)
        self.arquivo.write('\n')


    def crie_caminho_por_data(self,formato_ano ='ano_',formato_mes = 'mes_',formato_data = 'data_'):
        caminho_ano = formato_ano + self.pega_ano()
        caminho_mes = formato_mes + self.pega_mes()
        caminho_data = formato_data + self.pega_data() + '.json'
        return self.crie_caminho(caminho_ano,caminho_mes,caminho_data) 


    def crie_caminho_por_mes(self,formato_ano ='ano_',formato_mes = 'mes_'):
        caminho_ano = formato_ano + self.pega_ano()
        caminho_mes = formato_mes + self.pega_mes()
        return self.crie_caminho(caminho_ano,caminho_mes)


    def cria_caminho_por_ano(self,formato = 'ano_'):
        caminho_ano = formato + self.pega_ano()

        return self.crie_caminho(caminho_ano)


    def deletar(self,indice):
        lista = [item for item in self.carrego_arquivo(self.caminho)]
        if len(lista)>= indice:
            del lista[indice]
            with open(self.caminho,'w',encoding='utf-8') as arquivo:
                [arquivo.write(item) for item in lista]


    def __enter__(self):
        caminho = self.crie_caminho_por_mes()

        if self.checa_caminho_de_diretorio(caminho):
            caminho = self.crie_caminho_por_data()

            if self.checa_caminho_de_diretorio(caminho):
                self.caminho = self.crie_caminho_por_data()

            else:
                self.caminho = self.crie_caminho_por_data()
                self.cria_arquivo(self.caminho)

        else:
            self.crie_diretorio(caminho)

        

        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'arquivo'):
            
            self.arquivo.close()
            del self.arquivo















if __name__ == '__main__':

    with Editor_de_Arquivo() as arquivo:
        # arquivo.adiciona_em_arquivo({'nome':'ana'},arquivo.caminho)
        print(arquivo.__dict__)
        print()
        print(arquivo.cria_caminho_por_ano())
        print(arquivo.crie_caminho_por_mes())
        print()
        

















