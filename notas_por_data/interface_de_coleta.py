
import datetime




def coleta_input(txt,tipo_obj: str|int):
    while True:
        valor = input(txt).strip().lower()

        if valor.isnumeric() and tipo_obj == int:     
            return valor

        if tipo_obj == str and not all(item.isspace() for item in valor):
            return valor


def filtra(txt,tipo_obj,*item):
    while True:
        valor = coleta_input(txt,tipo_obj)
        if valor in item:
            return valor


            

def coleta_data():

    def coleta_dia():
        while True:
            dia = int(coleta_input('digite o dia : ',int))
            if dia in range(32):
                return str(dia)

    def coleta_mes():
        while True:
            mes = int(coleta_input('digite o mes : ',int))
            if mes in range(13):
                return str(mes)

    dia = coleta_dia()
    mes = coleta_mes()

    if int(dia) in range(10):
        dia = dia.zfill(2)

    if int(mes) in range(32):
        mes = mes.zfill(2)
    
    return f'{dia}_{mes}_{datetime.datetime.now().strftime('%Y')}'



# def adicionar_zero(numero):
#     numero_str = str(numero)
#     numero_com_zero = numero_str.zfill(2)  # Adiciona zero à esquerda se necessário
#     return numero_com_zero

# Exemplo de uso:
# numero_digitado = int(input("Digite um número entre 1 e 10: "))
# if 1 <= numero_digitado <= 10:
#     numero_formatado = adicionar_zero(numero_digitado)
#     print(f"Número formatado: {numero_formatado}")
# else:
#     print("Número fora do intervalo válido (1 a 10).")




if __name__ == '__main__':
    pass


















