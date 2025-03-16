
import time
import psutil
import os

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

        print(f"A função {func.__name__}   levou {t2 - t1} segundos para executar e usou {mem2 - mem1} MB de memória.")
        return result
    return wrapper
