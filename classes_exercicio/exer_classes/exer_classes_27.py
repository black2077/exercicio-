






def meu_decorador(funcao_original):
    def funcao_decorada(*args, **kwargs):
        
        resultado = funcao_original(*args, **kwargs)
        
        return resultado
    return funcao_decorada





class telefone:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero
        

class contato:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero


class ligar:
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero




class Interface:
    def __init__(self,componente_1,componente_2,componente_3):
        self.componente_1 = componente_1
        self.componente_2 = componente_2
        self.componente_3 = componente_3
    
    
    @meu_decorador
    def contato(self):
        return self.componente_1
    
    
    @meu_decorador
    def telefone(self):
        return self.componente_2
    
    
    @meu_decorador
    def ligar(self):
        return self.componente_3 

    def __enter__(self):
        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        pass



with Interface(contato,telefone,ligar) as arquivo:
    contato_cliente = arquivo.ligar()
    print(contato_cliente('ana','324243242').__dict__)
    
































