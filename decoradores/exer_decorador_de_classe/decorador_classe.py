
# chatgpt =============================================================================
def meu_decorador(classe):
    class NovaClasse:
        def __init__(self, *args):
            self.objeto_decorado = classe(*args)

        def minha_funcao(self):
            print("Executando minha_funcao() adicionalmente")
            return self.objeto_decorado.minha_funcao()

    return NovaClasse

@meu_decorador
class MinhaClasse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def minha_funcao(self):
        return self.x + self.y
#
# objeto = MinhaClasse(3, 4)
# print(objeto.minha_funcao())








# =========================================================================================

def call_classe(classe):
    class nova_classe:
        num_exec = 0

        def __init__(self,*args,**kwargs):
            self.classe_nova = classe(*args,**kwargs)


        def soma(self):
            return 2 * 5


        def __call__(self):
            self.num_exec +=1
            return self.classe_nova.__dict__

    return nova_classe

@call_classe
class produto:
    def __init__(self,marca,modelo,preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco

#
# p1 = produto('sony','ps4 -pro' , '1400')
#
# print(p1.__call__())
# print(p1.__call__())
# print(p1.__call__())
# print(p1.soma())
#
# print(p1.num_exec)
#
# p2 = produto('lg','tv - 32','790')
# print(p2.__call__())
# print(p2.num_exec)
# print(p2.soma())


# ==========================================================================================

lista = [{'__nome': 'ana','__cpf': '67564344334'},{'__nome': 'luana','__cpf': '878645432234','peso': '60'}
    ,{'__nome': 'ruan','__cpf': '135547795453','peso': '77'},{'__nome': 'mario','__cpf': '675678954656','peso': '89'}]


class ferramentas_arquivo:
    def __init__(self,cls):
        self.nova_classe = cls


    def __call__(self, *args, **kwargs):
        self.resultado = self.nova_classe(*args,**kwargs)
        global lista
        if self.resultado.__dict__ in lista :
            return f'{self.resultado.__dict__}'



@ferramentas_arquivo
class Pessoa_AR:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


# p1 = Pessoa('ana','67564344334')
#
# print(p1)

# =======================================================================================================

class ferramentas_produto:
    def __init__(self,cls):
        def interna(*args,**kwargs):
            self.resultado = cls(*args,**kwargs)
            return self.resultado
        return interna

    def __call__(self, *args, **kwargs):
        pass


# @ferramentas_produto
class Produto:
    def __init__(self,marca,preco,modelo):
        self.marca = marca
        self.preco = preco
        self.modelo = modelo


#
# pro1 = Produto('SONY','1900','PS4')
# print(pro1)

# ===========================================================================

class usuario:
    def __init__(self,cls):
        self.conta = cls
        self.tenta = 5
    def mostra(self):
        print('foi')
        self.tenta -= 1

    def __call__(self, *args, **kwargs):
        if self.tenta > 0:
            self.mostra()
            return self.conta(*args,**kwargs).__dict__,self.tenta
        return None

@usuario
class cliente:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha


#
# cli = cliente_acesso('luana_89','65443')
# cli = cliente_acesso('luana_89','65443')
# cli = cliente_acesso('luana_89','65443')
# cli = cliente_acesso('luana_89','65443')
# cli = cliente_acesso('luana_89','65443')
# cli = cliente_acesso('luana_89','65443')
#
# print(cli)
# ====================================================================================


class conta:
    def __init__(self,*args):
        self.chave = args

    def __call__(self,cls):
        def interna(*args,**kwargs):
            self.conta = cls(*args,**kwargs).__dict__
            print(self.chave)
            if self.chave[0] and self.chave[1] in self.conta:
                return self.conta
        return interna


@conta('__nome','__cpf')
class Pessoa:
    def __init__(self,nome,cpf,peso):
        self.nome = nome
        self.cpf = cpf
        self.peso = peso

p1 = Pessoa('ana','8975444323','67')
print(p1)

# ============================================================================















