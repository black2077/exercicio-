

import json
from datetime import datetime
import test_decorador_monitora_atividades_2


def registra_atividade(cls):
    def interna(*args,**kwargs):
        with open('arquivos/lista_clientes.json') as ler_arquivo:
            lista = [item for item in ler_arquivo]
            dicio = {f'{datetime.now().strftime("%d/%m/%y | %H:%M")}' : __name__}

            if len(lista) <= 5:
                resultado = cls(*args, **kwargs)
                with open('arquivos/lista_clientes.json', 'a') as arquivo:
                    json.dump(dicio,arquivo)
                    arquivo.write('\n')

                return resultado
    return interna



@registra_atividade
class Usuario:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha



if __name__ == '__main__':

    # usu = Usuario('ana','hdrfsef')
    # print(usu)

    jh = test_decorador_monitora_atividades_2.Cliente_Acesso('ana', '645354342', '553445')
    print(jh.__dict__)
    print('='*40)

    gf = test_decorador_monitora_atividades_2.Cliente('ana', '45643535433', '534534', 900, '65634534', '78766')
    print('='*40)
    gf.sacar(299)
    gf.deposito(645)
    print(gf.__dict__)







