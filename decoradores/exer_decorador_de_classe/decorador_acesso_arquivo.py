import json
# =========================================================
class AcessoArquivo:
    def __init__(self,cls):
        self.classe = cls
        self.arquivo = self.arquivo_lista()

    def arquivo_lista(self):
        with open('arquivo_lista.json') as arquivo:
            return [json.loads(item) for item in arquivo]

    def procura(self):
        for item in self.arquivo:
            if self.classe['__nome'] == item['__nome'] and self.classe['__cpf'] == item['__cpf']:
                if self.classe['__senha'] == item['__senha']:
                    del self.arquivo
                    return True

        del self.arquivo

    def __call__(self, *args, **kwargs):
        self.classe = self.classe(*args,**kwargs).__dict__
        if self.procura():
            return self.classe

# =========================================================
class Avalidor_tipo:
    def __init__(self,cls):
        self.classe = cls

    def checa_tipo(self,classe):
        if  classe == None:
            raise f'{classe}'
        return classe

    def __call__(self, *args, **kwargs):
        self.classe(*args,**kwargs)
        print(self.classe.__dict__)
        return self.checa_tipo(self.classe)

# =========================================================

@Avalidor_tipo
@AcessoArquivo
class Usuario:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


usu = Usuario('ana','987654321','123456')
print(usu.__dict__)
























