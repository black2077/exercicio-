

class arquivo:
    def mostra(self,cls):
        dicio_classe = cls.__dict__
        print(dicio_classe)

    def lista(self):
        print(1,2,3,4,5,6,7,8,9,10)


def func_classe(classe,diretorio):
    def classe_exe(cls):
        def interna(*args,**kwargs):
            resultado = cls(*args,**kwargs)
            arq = classe()
            arq.mostra(resultado)
            arq.lista()
            
            return resultado
        return interna
    return classe_exe


@func_classe(arquivo,'diretorio')
class Cliente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


pesso = Cliente('ana','65434543534','435345')

























