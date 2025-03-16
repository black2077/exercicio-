


def filtra_tipo(valor):
    match type(valor):

        case int,:
            print(f'o {valor} e do tipo {type(valor)}')

        case _:
            print('não é do tipo definido')


filtra_tipo(1)













