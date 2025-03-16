

import json




class Arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio

    def carrega_arquivo(self,dicio):
        with open(self.diretorio) as arquivo:
            self.indice = 0
            while True:
                try:
                    item = json.loads(arquivo.readline())

                    if dicio.get('nome') == item.get('nome') and dicio.get('senha') == item.get('senha'):

                        return item


                    else:
                        self.indice += 1

                except json.decoder.JSONDecodeError:
                    self.indice = None
                    break


    def _carrega_indice(self,indice):
        if type(indice):
            with open(self.diretorio) as arquivo:
                lista = list(arquivo)
                return json.loads(lista[indice])



class leitor_arquivo(Arquivo):
    def __init__(self,diretorio,indice = None):
        super().__init__(diretorio)
        self._indice = indice

    def __call__(self,cls):
        def interna(*args,**kwargs):
            resultado = cls(*args, **kwargs)
            arquivo = Arquivo(self.diretorio)
            print('no decorador',)

            if isinstance(self._indice,int):
                print('saindo do decorador')
                return [self._carrega_indice(self._indice),self._indice]

            arquivo.carrega_arquivo(resultado.__dict__)

            print('saindo do decorador')

            return [resultado,arquivo.indice]

        return interna



@leitor_arquivo('arquivo_lista.json')
class Cliente:
    def __init__(self,nome,senha,cpf):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf



cl = Cliente('maria luiza','665654','987654321')
print('================================')
print(cl[0].__dict__,cl[1])
print(cl[0],cl[1])






























