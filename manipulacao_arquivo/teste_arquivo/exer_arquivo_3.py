


import json

def test_arquivO():

    with open('arquivos/lista_test.json') as arquivo:
        lista = [ item for item in arquivo]
        print(lista)



    # Abrir o arquivos JSON
    with open('arquivos/lista_test.json') as file:
        lista_file = [item for item in file]
        print(len(lista_file))

    data = []
    # Adicionar a lista dentro de outra lista
    data.append(['item1', 'item2', 'item3'])
    data.append(['item4', 'item5', 'item6'])
    data.append(['item7', 'item8', 'item9'])


    # Escrever no arquivos JSON
    with open('arquivos/lista_test.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')


class Arquivo_Matriz:
    def __init__(self,dicio,chave):
        self.chave = chave
        self.dicio = dicio
        self.arquivos_em_lista()
        self.adiciona_lista()

    def arquivos_em_lista(self):
        with open('arquivos/lista_test_2.json') as arquivo:
            return [json.loads(item)  for item in arquivo]

    def adiciona_lista(self):
        with open('arquivos/lista_test.json', 'a') as arquivo:
            if isinstance(self.dicio,list|dict):
                json.dump({self.chave : self.dicio},arquivo)
                arquivo.write('\n')
            else:
                raise 'não é lista nem dicionario'

    def busca_lista(self):...
        




class Usuario:
    def __init__(self,nome,cpf,email,rg,telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.rg = rg
        self.telefone = telefone
        # self.endereco('','','','')

    def endereco(self,rua,numero,cidade,estado):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado



cla = Usuario('ANA','54657567565','sfadda','65344543544','65453445')
print(cla.__dict__)

Arquivo_Matriz(cla.__dict__,'informacoes pessoas')

cla.endereco('rua marcio santos','43 s','rio de janeiro','rio de janeiro')
print(cla.__dict__)

Arquivo_Matriz(cla.__dict__,'informacoes pessoas')




