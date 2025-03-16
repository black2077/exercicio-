import asyncio



def func_media():
    total = 0
    contador = 0
    media = None
    while True:
        entrada = yield media
        print(total)
        total += entrada

        print()
        contador += 1
        media = total/contador
#
# media = func_media()
#
# next(media)
#
# print(media.send(10))
# print(media.send(10))
# print(media.send(18))
# print(media.send(6))
# print(media.send(10))



async def filtra_str(txt :str):
    if txt.isalpha() and not txt.isspace():
        return txt

async def filtra_int(num :str|int):
    if num.isnumeric() :
        return int(num)

    if isinstance(num,int):
        return num

async def tamanho(txt):
    return len(txt)


async def test_1(txt,*func):
    lista = []

    for item in func:
        await item(txt)



asyncio.run(test_1('ana',filtra_int,filtra_str,tamanho))


#
# fun = filtra_str('1')
# inti = filtra_int('5')
#
# print(fun)
# print(inti)



# te = test_1()
#
# print(next(te))
# print(next(te))
# print(next(te))

