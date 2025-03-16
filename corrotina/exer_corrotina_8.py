import asyncio
from  exer_corrotina_7 import   Arquivo





async def busca_indice(num,pasta,arquivo):
    with Arquivo() as arq:
        return arq.busco_indice(num,pasta,arquivo)



async def tarefa_1(valor):
    await asyncio.sleep(2.5)
    return valor + 3


async def executa_tudo(tarefa_1,tarefa_2,tarefa_3):
    resulta = asyncio.gather(busca_indice(tarefa_1,'backup_arquivos','lista_1_backup.json'),busca_indice(tarefa_2,'backup_arquivos','lista_1_backup.json'),busca_indice(tarefa_3,'backup_arquivos','lista_1_backup.json'))
    await resulta
    return resulta


item = asyncio.run(executa_tudo(4,1,3))
item_2 = asyncio.run(busca_indice(2,'backup_arquivos','lista_1_backup.json'))


print(item)
























