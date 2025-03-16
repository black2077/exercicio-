



class coleta_input:
    def __init__(self,txt = '',tamanho= 40):
        self.texto = txt
        self.tamanho = tamanho

        self.valor = self.input_coleta(self.texto,tamanho)
        

    def input_coleta(self,txt='',tamanho=40):
        while True:
            valor = input(txt).strip()
            if len(valor) <= tamanho :               
                return valor


    def filtra_input(self,numero_tentivas: int = 100): 
        
        cont = 0
        while True:
            cont += 1

            if self.valor.isnumeric():
                return self.valor

            elif all(char.isalpha() or char.isspace() for char in self.valor) and not all(char.isspace() for char in self.valor):
                return self.valor
        
            if numero_tentivas <= cont:
                break
            
            self.valor = self.input_coleta(self.texto,self.tamanho)

        
    def checa_condicoes(self,*condicoes):
            
        if self.valor in condicoes:
            return self            

        
            


    def __str__(self):
        return self.valor








def input_coleta(txt: str,tamanho:int = 40):
    
    while True:
        valor = input(txt).strip()
        if len(valor) <= tamanho :
            return valor


def filtra_input(txt: str, tamanho: int =40,numero_tentivas: int = 100): 
    cont = 0

    while True:
        cont += 1
        valor = input_coleta(txt,tamanho)
        
        if valor.isnumeric():
            return int(valor)

        elif all(char.isalpha() or char.isspace() for char in valor) and not all(char.isspace() for char in valor):
            return valor    
        
        if numero_tentivas <= cont:
            break



def checa_condicoes(txt,tamanho = 40,*condicoes):
    while True:
        valor = filtra_input(txt,tamanho)
        if valor in condicoes:
            return valor
        
        

if __name__ == '__main__':
    

    lk = checa_condicoes('digite sua opção :', 1 , 1,2,3,4)
    print(lk)

    coleta = coleta_input('digite :').filtra_input()
    print(coleta)
    
