import json





class monitora_atividade:
    def __init__(self,nome,cpf,diretorio,adic = False):
        self.diretorio = diretorio
        self.nome = nome
        self.cpf = cpf
        self.adic = adic

    def lista_arquivo(self):
        with open(self.diretorio) as arquivo:
            return [json.loads(item) for item in arquivo]

    def procura(self):
        self.arquivo = self.lista_arquivo()
        for num, item_dicio in enumerate(self.arquivo):
            item = item_dicio['usuario']
            if self.nome == item['nome'] and self.cpf == item['cpf']:
                self.indice = num
                self.dicio = item_dicio
                return True

        del self.arquivo

    def contador_saque(self,resultado):
        self.dicio['saque'].append(resultado)
        if len(self.dicio['saque']) >= 10:
            del self.dicio['saque'][0]

    def contador_deposito(self,resultado):
        self.dicio['deposito'].append(resultado)
        if len(self.dicio['deposito']) >= 10:
            del self.dicio['deposito'][0]

    def adiciona_novo(self):
        dicio = {'usuario': {'nome': self.nome, 'cpf': self.cpf} ,'saque': [] , 'deposito' :[]}
        with open(self.diretorio,'a') as arquivo:
            json.dump(dicio,arquivo)
            arquivo.write('\n')

    def adiciona_info(self,lista):
        with open(self.diretorio,'w') as arquivo:
            for dicio in lista:
                json.dump(dicio,arquivo)
                arquivo.write('\n')

    def __call__(self,func):
        def interna(*args,**kwargs):
            resultado = func(*args, **kwargs)

            if func.__name__ == 'deposito' and self.procura():
                self.contador_deposito(resultado)
                self.adiciona_info(self.arquivo)

            if func.__name__ == 'saque' and self.procura():
                self.contador_saque(resultado)
                self.adiciona_info(self.arquivo)

            if self.adic:
                self.adiciona_novo()

            return resultado
        return interna


nome = 'mario'
cpf = '575466654'
senha = '324234'


class cliente:
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0
        self.conta = '64564'
        self.banco = '34534532'

    @monitora_atividade(nome,cpf,'_lista_atividade_contas.json')
    def saque(self,valor) -> int:
        self.saldo -= valor
        return valor

    @monitora_atividade(nome,cpf,'_lista_atividade_contas.json')
    def deposito(self,valor) -> int:
        self.saldo += valor
        return valor


vl = cliente(nome,cpf,senha)
vl.deposito(80060)
vl.saque(1000)



















