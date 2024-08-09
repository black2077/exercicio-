from objeto_editor_de_arquivo import Editor_de_Arquivo
from interface_de_coleta import filtra,coleta_input,coleta_data
import json



class Texto:
    def __init__(self,titulo,assunto,texto):
        self.titulo = titulo
        self.assunto = assunto
        self.texto = texto

    def editar(self,chave,novo_valor):
        if hasattr(self,chave):
            setattr(self,chave,novo_valor)

    
def linha(tamanho=50):
    print('=' * tamanho)



class interface:


    def pagina_de_apresentacao(self):
        print()
        print()
        linha(120)
        print()
        print('                                       ( 1 ) = adicionar nota  ')
        print('                                       ( 2 ) = adicionar nota por data  ')
        print('                                       ( 3 ) = editar arquivo  ')
        print('                                       ( 4 ) = listar Diretórios    ')
        print('                                       ( 5 ) = listar  notas    ')
        print('                                       ( 6 ) = listar assunto     ')
        print('                                       ( 7 ) = listar Diretório específico     ')
        print('                                       ( 8 ) = deleta da lista     ')
        print('                                       ( 9 ) = deleta de diretório específico     ')
        print()
        linha(120)
        op = filtra('digite seu opção :',int,'1','2','3','4','5','6','7','8','9')
        linha(120)
        print()
        print()
        return int(op)


    def adiciona_nota(self):
        with Editor_de_Arquivo() as arquivo:
            linha(120)
            linha(120)
            print()
            print('                                    adicionar em arquivo')
            print()
            titulo = coleta_input('digite o titulo :',str)
            assunto = coleta_input('digite o assunto :',str)
            texto = coleta_input('digite o texto :',str)

            salvo_texto = Texto(titulo,assunto,texto).__dict__
            arquivo.adiciona_em_arquivo(salvo_texto,arquivo.caminho)
            print()
            linha(120)
            linha(120)


    def adiciona_por_data(self):
        linha(120)
        data = coleta_data()
        linha(120)

        with Editor_de_Arquivo() as arquivo:
            mes = f'mes_{data[3:5]}'
            if mes in arquivo.lista_nome_de_diretorio(arquivo.cria_caminho_por_ano()):
                nome_arquivo = f'data_{data}.json'
                caminho = arquivo.caminho.parent.parent/ mes / nome_arquivo
                print(caminho)
                if not arquivo.checa_caminho_de_arquivo(caminho):
                    print()
                    linha(120)
                    titulo = coleta_input('digite o Título : ',str)
                    assunto = coleta_input('digite o assunto : ',str)
                    texto_completo = coleta_input('digite o texto : ',str)
                    txt = Texto(titulo,assunto,texto_completo)
                    linha(120)

                    arquivo.adiciona_em_arquivo(txt.__dict__,caminho)


    def editar_arquivo(self):
        lista = []

        with Editor_de_Arquivo() as arquivo:
            for num,item in enumerate(arquivo.carrego_arquivo(arquivo.caminho)):
                lista.append(json.loads(item))
                print('================================ ',num,' ==================================')
                print(item)
                linha(140)
            

            linha(120)
            indice = coleta_input('digite o indice:',int)
            linha(120)

            tamanho = len(lista)
            if tamanho and tamanho -1 >= indice:
                print()
                print(lista[indice])
                print()

                linha(120)
                classe = Texto(*lista[indice].values())
                chave = input('digite a chave : ')
                linha(120)

                if chave in classe.__dict__.keys():
                    novo_chave = input('digite a nova chave : ')

                    classe.editar(chave,novo_chave)
                    print(classe.__dict__)
                    arquivo.editar_arquivo(indice,classe.__dict__)
                

    def lista_diretorio(self):
        with Editor_de_Arquivo() as arquivo:
            lista = arquivo.lista_nome_de_diretorio(arquivo.caminho.parent)
            linha(120)
            linha(120)
            print()
            print('                                 lista de diretorios')  
            print()
            for num,item in enumerate(lista):
                print(f'                                  {num} =',item)
            print()
            linha(120)
            linha(120)

        return lista


    def lista_notas(self):
        with Editor_de_Arquivo() as arquivo:
            lista = [json.loads(item) for item in arquivo.carrego_arquivo(arquivo.caminho)]

        linha(90)
        print('                              lista de notas')
        linha(90)
        print()  
        for num,item in enumerate(lista):

            linha(90)
            print(f'                              nota : {num}  ')
            print()
            print('                        titulo  = ',item['titulo'])
            print()
            print('                        assunto  = ',item['assunto'])
            print()
            print(item['texto'])
            print()
            linha(90)
            

    def lista_assunto(self):

        def pega_txt(item,txt):
            dicio = json.loads(item)
            return dicio.get(txt)


        with Editor_de_Arquivo() as arquivo:
            for num,item in enumerate(arquivo.carrego_arquivo(arquivo.caminho)):
                linha(100)
                print(f'          asunto do texto {num} = ',pega_txt(item,'assunto'))
            linha(100)


    def lista_diretorio_Especifico(self):
        lista = self.lista_diretorio()
        indice = coleta_input('digite o indice :',int)
        linha(120)

        if len(lista) - 1 >= indice:
            with Editor_de_Arquivo() as arquivo:
                caminho = arquivo.caminho.parent / lista[indice]
                print()
                for num,item in enumerate(arquivo.carrego_arquivo(caminho)):
                    
                    dicio = json.loads(item)
                    print()
                    print(f'======================  {num}  ==========================================================================')
                    print('                                     (  Título  )  =',dicio['titulo'])
                    print()
                    print('                                     (  assunto  ) = ',dicio['assunto'])
                    print()
                    print('    (  texto  )  =')
                    print()
                    print('    ',dicio['texto'])
                    linha(100)

        else:
            print('                     erro ')    


    def deletar(self):
        with Editor_de_Arquivo() as arquivo:
            self.lista_notas()
            linha(90)
            indice = coleta_input('digite o indice do deseja deletar :',int)
            linha(90)
            arquivo.deletar(indice)


    def deleta_de_diretorio_especifico(self):
        self.lista_diretorio_Especifico()
        linha(90)
        indice = coleta_input('digite o indice que deseja deletar :',int)
        linha(90)



    def __enter__(self):
        with Editor_de_Arquivo() as arquivo:
            return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self






while True:
    with interface() as editor:
        op = editor.pagina_de_apresentacao()
        
        match op:

            case 1:
                editor.adiciona_nota()
            
            case 2:
                editor.adiciona_por_data()

            case 3:
                editor.editar_arquivo()

            case 4:
                editor.lista_diretorio()

            case 5:
                editor.lista_notas()
                
            case 6:
                editor.lista_assunto()
            
            case 7:
                editor.lista_diretorio_Especifico()

            case 8:
                editor.deletar()

            case 9:
                editor.deleta_de_diretorio_especifico()



