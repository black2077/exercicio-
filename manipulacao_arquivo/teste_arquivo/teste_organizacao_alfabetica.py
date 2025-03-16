

import json

class arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio
        self.arquivos = self.carrega_arquivos()

    def carrega_arquivos(self):
        with open(self.diretorio) as arquivo:
           return [json.loads(item) for item in arquivo]


    def organizo_alfabetica(self):
        lista = {}
        try:
            for item in self.arquivos:
                if item['nome'][0] in lista.keys():
                    lista[item['nome'][0]].append(item)
                else:
                    lista.update({item['nome'][0] : [item]})
        except (KeyError):
            raise 'foi'

        self.arquivos_organizado = lista


    def adiciona_em_arquivo(self,diretorio):
        with open(diretorio,'w') as arquivo:
           for item in self.arquivos_organizado.items():
               json.dump({item[0]:item[1]},arquivo)
               arquivo.write('\n')



be = arquivo('lista_clientes.json')
be.organizo_alfabetica()
be.adiciona_em_arquivo('lista_clientes_ordenada.json')



ca = arquivo('lista_clientes_ordenada.json')


for item in ca.arquivos:
    print(item)





