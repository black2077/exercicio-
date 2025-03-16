import pathlib


class Arquivo:
    def __init__(self):
        self.caminho = self.cria_caminho()

    def cria_caminho(self,nome_arquivo = ''):
        return pathlib.Path(__file__).parent / nome_arquivo

    def teste_dicio(self,caminho):
        with open(caminho) as arquivo:
            lista = [item.replace('\n','').rsplit(',') for item in arquivo]
            lista_dicio = []

            for num in range(1,len(lista)):
                for item in lista[num]:
                    dicio = {item: '' for item in lista[0]}
                    dicio['nome'] = lista[num][0]
                    dicio['idade'] = lista[num][1]
                    dicio['cpf'] = lista[num][2]
                    dicio['sobrenome'] = lista[num][3]
                    dicio['meme'] = lista[num][4]

                lista_dicio.append(dicio.copy())

            return lista_dicio

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



with Arquivo() as arquivo:
    caminho = 'arquivo/nome.csv'

    teste = arquivo.teste_dicio(caminho)
    for item in teste:
        print(item)


    # print(teste)



            # lista_dicio = []
            # for item in lista[1]:
            #     dicio = {item: '' for item in lista[0]}
            #     dicio['nome'] = lista[1][0]
            #     dicio['idade'] = lista[1][1]
            #     dicio['cpf'] = lista[1][2]
            #     dicio['sobrenome'] = lista[1][3]
            #     dicio['meme'] = lista[1][4]
            #
            # lista_dicio.append(dicio)
            # print(lista_dicio)








