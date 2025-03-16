



import time
import psutil
import os



def linha(tamanho = 80):
    print('='* tamanho)



tempo = 0

def monitora_velocidade_memoria(func):
     
    def wrapper(*args, **kwargs):
        global tempo
        t1 = time.time()
        process = psutil.Process(os.getpid())
        mem1 = process.memory_info().rss / 1024 / 1024
        result = func(*args, **kwargs)
        t2 = time.time()

        process = psutil.Process(os.getpid())
        mem2 = process.memory_info().rss / 1024 / 1024
        tempo = t2-t1

        # print(f'levou {t2 - t1} segundos para executar e usou {mem2 - mem1} MB de memória A função {func.__name__}   .')
        tempo_de_execucao = round(t2 - t1,5)
        memoria_usada = round(mem2 - mem1,5)

        return {'tempo_de_execucao': tempo_de_execucao , 'Memoria_usada' : memoria_usada }
    
    return wrapper


# ===================================================================================


class Interface_de_teste:
    def __init__(self,lista_de_funcoes,valores):
        self.lista_de_funcoes = lista_de_funcoes
        self.valores = valores
        self.tamanho = 10


    def teste_funcao(self,tamanho,func,args):
        lista = []

        def teste(func,args):
            for item in args:
                teste = monitora_velocidade_memoria(func)
            return teste(*item)


        for num in range(tamanho):
            lista.append(teste(func,args))

        return lista


    def opcao_teste(self):
        print()
        print()
        linha(100)
        print()
        print('                       Lista de funções              ')
        print()
        print('                   ( testar função específica  = 1)  ')
        print('                   ( mostra todas as funções   = 2)  ')
        print('                   ( Comparar funções          = 3)  ')
        print('                   ( testa tudo                = 4)  ')
        print('                   ( Definir tamanho do teste  = 5)  ')
        print()
        linha(100)
        op = int(input('                  digite sua o numero : '))
        linha(100)
        print()
        print()
        return op


    def mostra(self,lista):
        for item in lista:
            print('     |',item)


    def mostra_funcoes(self):
        print()
        print('                                 lista de funções    ')
        print()

        for num,item in enumerate(self.lista_de_funcoes):
            print(f'                       | {num} =',item)
        
        print()
        
        
    def teste_todo(self,tamanho,args):
        lista = []

        lista_decorada = [ monitora_velocidade_memoria(func)  for func in self.lista_de_funcoes ]


        for num in range(tamanho):
            for item in args:
                dicio = [func(*item) for func in lista_decorada]

                lista.append(dicio)

        return lista


    def tamanho_de_teste(self):
        while True:
            tamanho = int(input('digite o contidade de teste :'))

            if tamanho > 0:
                self.tamanho = tamanho
                break
            
            else:
                print('Mínimo de teste necessário é 1')


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass 



# ========================================================================================================================================

def interface_testador(funcoes:list,valores: list):
    with Interface_de_teste(funcoes,valores) as Funcao_de_testagem:

        while True:
            op = Funcao_de_testagem.opcao_teste()

            match op:
                case 1:
                    Funcao_de_testagem.mostra_funcoes()
                    linha(100)
                    indice = int(input('digite o indice : '))
                    linha(100)
                    print()
                    lista = Funcao_de_testagem.teste_funcao(Funcao_de_testagem.tamanho,Funcao_de_testagem.lista_de_funcoes[indice],Funcao_de_testagem.valores)
                    print()
                    linha(100)
                    print()
                    Funcao_de_testagem.mostra(lista)


                case 2:
                    Funcao_de_testagem.mostra_funcoes()


                case 3:
                    linha(100)
                    print()
                    print('                                 Comparar funções ')
                    print()
                    Funcao_de_testagem.mostra_funcoes()
                    print()
                    linha(100)
                    indice_1 = int(input('digite o indice da primeira função : '))
                    linha(100)
                    indice_2 = int(input('digite o indice da segunda função : '))
                    linha(100)
                    print()

                    lista_1 = Funcao_de_testagem.teste_funcao(Funcao_de_testagem.tamanho,Funcao_de_testagem.lista_de_funcoes[indice_1],Funcao_de_testagem.valores)
                    lista_2 = Funcao_de_testagem.teste_funcao(Funcao_de_testagem.tamanho,Funcao_de_testagem.lista_de_funcoes[indice_2],Funcao_de_testagem.valores)

                    print(f'                                    {Funcao_de_testagem.lista_de_funcoes[indice_1].__name__}                      |                  {Funcao_de_testagem.lista_de_funcoes[indice_2].__name__} ')
                    print()

                    for item_1,item_2 in zip(lista_1,lista_2):
                        print(f'  |     {str(item_1).center(40)}          |     {str(item_2).center(40)} ',end='')
                        print(f'    ')

                case 4:
                    linha(100)
                    lista = Funcao_de_testagem.teste_todo(Funcao_de_testagem.tamanho,Funcao_de_testagem.valores)
                    
                    for item in Funcao_de_testagem.lista_de_funcoes:
                        print(f'|                            {item.__name__}                |', end='')

                    print()
                    def mostra(item):
                        for it in item:
                            print(f'|  {it} |',end='')
                        print()

                    print()
                    for item in lista:
                        mostra(item)

                case 5:
                    Funcao_de_testagem.tamanho_de_teste()


interface_testador([],[])
