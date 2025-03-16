



def perna_direita():
    txt = 'perna direita'
    yield txt


def perna_esquerda():
    txt = 'perna esquerda'
    yield txt


def controle_de_passo():
    cont =  0
    num = 0

    while True:

        yield next(perna_direita()),cont
        cont+=1
        yield next(perna_esquerda()),cont
        cont+=1
        num -= 1


def corre(passadas):
    func = controle_de_passo()
    for item in range(passadas+1):
        print(next(func))




valor = controle_de_passo()


corre(80)

