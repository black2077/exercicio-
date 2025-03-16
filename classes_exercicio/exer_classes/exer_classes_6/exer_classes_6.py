


# class Eletronico:
#     def __init__(self, __cpf):
#         self._cpf = __cpf
#         self._ligado = False
#
#     def ligar(self):
#         if not self._ligado:
#             self._ligado = True
#
#     def desligar(self):
#         if self._ligado:
#             self._ligado = False
#
#
# class Smartphone(Eletronico, LogFileMixin):
#     def ligar(self):
#         super().ligar()
#
#         if self._ligado:
#             msg = f'{self._cpf} está ligado'
#             self.log_success(msg)
#
#     def desligar(self):
#         super().desligar()
#
#         if not self._ligado:
#             msg = f'{self._cpf} está desligado'
#             self.log_error(msg)
#
#
#
#
# class maquina:
#     def __init__(self,__cpf):
#         self._cpf = __cpf
#         self._estado = False
#
#     def liga(self):
#         print('ligando')
#         self.estado = True
#
#     def desliga(self):
#         print('desligando')
#         self.estado = False
#
#
#
# class geladeira_industrial(maquina):
#     def ligar(self):
#         super().liga()
#
#     def desliga(self):
#         super().desliga()
#
#     def monitorando(self,temperatura):
#         if temperatura > 43 :
#             print('resfriando a agua ')
#             super().liga()
#         else:
#             print('temperatura da agua contida')
#             super().desliga()
#
#
# class alimentador(maquina):
#     def ligar(self):
#         super().liga()
#
#     def desliga(self):
#         super().desliga()
#
#     def monitorando(self, contidade):
#         if contidade > 90:
#             print('aquecendo materia')
#             super().liga()
#         else:
#             print('cheio !')
#             super().desliga()
#
import json
from copy import deepcopy



class Construtor:
    def __init__(self):
        self.lista ={}
    @classmethod
    def pega_info(self):
        dicio = {}
        dicio['__cpf completo'] = input('digite seu __cpf completo :')
        dicio['idade'] = input('digite sua idade :')
        dicio['__cpf'] = input('digite seu __cpf :')
        # dicio['email'] = input('digite seu email :')
        return dicio

    @classmethod
    def info_dados_bancarios(self):
        dicio = {}
        dicio['RG'] = input('digite seu rg :')
        # dicio['numero'] = input('digite seu numero :')
        # dicio['renda'] = input('digite sua renda :')
        dicio['__saldo'] = 0
        return dicio

    def adiciona(self,item_1):
        self.lista.update(item_1)

    def __str__(self):
        return f'{self.lista}'

    def __repr__(self):
        return f'vareavel = {type(self).__name__}()'



class Arquivo:
    def adiciono_base_principal(self, file):
        modo = 'w' if not r'__lista' else 'a'
        with open('exer_classes_6_lista.Json', modo, encoding='utf8') as arqui:
            json.dump(f'{file}',arqui)
            arqui.write('\n')


    def mostra_texto(self):
        with open('exer_classes_6_lista.Json', 'r', encoding='utf8') as arqui:
            for item in arqui:
                print(item)

    def __repr__(self):
        print(f'{type(self).__name__}(arquivo_registro)')


#
# pessoas = Construtor()
# pessoas.adiciona(Construtor.paga_info())
# pessoas.adiciona(Construtor.info_dados_bancarios())
# print(pessoas)


pes = Construtor()

lista= Arquivo()



pes.adiciona(Construtor.pega_info())
pes.adiciona(Construtor.info_dados_bancarios())
print(pes,type(pes))
print(pes.lista)

lista.adiciono_base_principal(pes)

print(lista.__repr__())