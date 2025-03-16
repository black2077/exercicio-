from time import sleep

vida = 90

if True:
    while True:
        sleep(0.1)
        vida -= 1
        print('dano' ,1)
        if vida == 0:
            print('morreu')
            break