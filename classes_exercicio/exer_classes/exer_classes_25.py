
def condicao(cls):
    class propriedades(cls):
        def massa(self,protons,neutros,eletron):
            self.protons = protons
            self.neutros = neutros
            self.eletron = eletron
            return self.protons + self.neutros + self.eletron

        def estado(self):
            if self.eletron > self.protons:
                self.eletron = -self.eletron

            if self.eletron < self.protons:
                self.eletron = +self.eletron

    return propriedades

@condicao
class ferro:
    def __init__(self,protons,neutros,eletron):
        self.protons = protons
        self.neutros = neutros
        self.eletron = eletron

    def camada_valencia(self,valor):
        if self.eletron <= 24 :
            self.eletron = valor


ferroo = ferro(26,26,26)

print(ferroo.__dict__,ferroo.massa(26,26,26))




















