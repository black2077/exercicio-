




from datetime import datetime


class Relogio:
    hora = datetime.now().strftime("%H:%M")
    data = datetime.now().strftime("%d/%m/%y")

    def __repr__(self):
        return f'{self.hora} | {self.data}'


dad = Relogio()
ds = Relogio()

# ======================================================================================
class Pessoa:
    hora = datetime.now().strftime("%H:%M")
    data = datetime.now().strftime("%d/%m/%y")

    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return f"{self.kwargs}| {self.hora} | {self.data}"


dicio = {'__cpf':'ana','idade':'43','peso':'67'}
dicio_2 = {'__cpf':'luana','idade':'23','peso':'57'}

pessoa_1 = Pessoa(**dicio)

pessoa_2 = Pessoa(**dicio_2)

print(pessoa_1)

print(pessoa_2)





