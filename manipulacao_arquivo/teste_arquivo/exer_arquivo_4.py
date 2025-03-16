





import json




lista = [{'__nome' : 'ana','idade' : 14},{'__nome' : 'luana','idade' : 40},{'__nome' : 'ruan','idade' : 34},{'__nome' : 'ana maria','idade' : 56}]


class Ordena_Lista:

    def __init__(self):
        self.arquivo = self.ler_arquivos()
        self.lista_ordenada = self.ordena_lista(self.arquivo)

    def ler_arquivos(self):
        with open('arquivos/lista_test.json') as arquivo:
            return [json.loads(item) for item in arquivo]

    def ordena_lista(self,lista) -> list:
        try:
            return lista.sort(key=lambda item: item['__nome'])
        except KeyError:
            raise 'chave não encontrada'





lis = Ordena_Lista()

print(lis.__dict__)




kl = {'__nome' : 'thiago'}

print(kl['__nome'][0])








