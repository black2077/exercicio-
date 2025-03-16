










import json


class Pessoas:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __enter__(self):
        print('foi')
        lista = [self.nome,int(self.idade)]
        self.pasta = open('exer_classes_9.json', 'a')
        self.pasta.write(f'{lista}')
        self.pasta.write('\n')


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pasta.close()
        print('encerrou')
        with open('listatxt','w') as error:
            error.write(exc_type)
            error.write(exc_val)
            error.write(exc_tb)
            error.write('\n')







li = Pessoas('ANA','21').__enter__()

print(li)



















def pagar_arquivo(txt,modo):
    try:
        pasta = open(txt,modo)

    except Exception as erro:
        with open('../errors_em_abertura', 'w') as error:
            error.write(str(erro))
            error.write('\n')

    finally:
        pasta.close()




















