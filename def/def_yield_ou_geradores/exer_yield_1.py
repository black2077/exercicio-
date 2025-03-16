





def da_ordem(ini = 0):
    while True:
        ini += 1
        yield ini

        

p = da_ordem()

print(next(p))


