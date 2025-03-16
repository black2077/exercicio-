
class MinhaClasseArquivo:
    def __init__(self):
        self.data = self.arquivo()

    def arquivo(self):
        with open('lista_teste.json') as arquivo:
            return [json.loads(item) for item in arquivo]

    def __getattr__(self, nome_atributo):
        self.data = self.arquivo()
        for item in self.data:
            if nome_atributo['__nome'] == item['__nome'] and nome_atributo['__cpf'] == item['__cpf'] and \
               nome_atributo['__senha'] == item['__senha'] :
                return item

    def __call__(self,cls):
        def interna(*args,**kwargs):
            resultado =  cls(*args,**kwargs).__dict__
            return self.__getattr__(resultado)
        return interna

# =========================================================== classe decoradora
class MeuArquivo:
    def __init__(self,cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        resultado = self.cls(*args,**kwargs)
        print('com classe')
        return resultado.__dict__

# ===========================================================
# @MinhaClasseArquivo()
@MeuArquivo
class Usuario:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


usu = Usuario('ana' ,'6743534534','098998')
print(usu)
