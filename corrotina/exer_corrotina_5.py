
import asyncio


def catador():

    while True:
        conti = yield from range(10)

num = catador()

# print(next(num))

# =============================================

def contador():
    cont = 0
    while True:
        cont += 1
        yield cont
        if cont in [9,19,29,39,49,59,69,79,89,99]:
            yield '100000'
            cont +=1

# con = contador()
#
#
# print(next(con))
# print(next(con))
# print(next(con))

# ================================================
def texto(txt):
    return txt

def teste(*args):
    for item in args:
        yield item

mk1 = teste(texto('foi fazer amor'),texto('cheio de T'),texto('passei amor'),texto('passei o dedinho'),texto('subir o cherinho'))

for item in mk1:
    print(item)
# ================================================


async  def filtro(txt):
    if isinstance(txt,str):
        await asyncio.sleep(0.1)
        return txt

    return None


# Definindo uma corotina
async def minha_corotina(txt):
    cont = 0
    while True:
        cont += 1
        valor = await filtro(txt)
        if isinstance(txt,str) and cont <= 5:
            print(cont, ")Inicio a corotina", txt)
            valor = await filtro(txt)
             # Simula uma operação assíncrona
            print(valor)
            print(cont, ")fim concluída", valor)
        else:
            break


        print('================================')



# Executando a corotina
async def main(txt):
    return await minha_corotina(txt)



async def super_main(txt_1,txt_2):
    valor = await minha_corotina(txt_1)
    valor_2 = await minha_corotina(txt_2)

    return valor,valor_2






# Rodando o loop de eventos
if __name__ == "__main__":
    # valor = main('texto')
    # asyncio.run(valor)
    po = super_main('ta','tu')
    asyncio.run(po)
    print(po)








