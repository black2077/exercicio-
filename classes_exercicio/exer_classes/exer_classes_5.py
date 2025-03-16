
class ClassePai:
    def __init__(self):
        self.atributo1 = "valor1"

class ClasseFilha(ClassePai):
    def __init__(self):
        super().__init__()
        self.atributo2 = "valor2"


classeFilha = ClasseFilha()
print(classeFilha.atributo1)
