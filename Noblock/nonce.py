'''
1- Considerando el programa noblock.py, realizando un programa que lance dos procesos hijos
que intenten encontrar el nonce para un No-Bloque con una dificultad dada.
El hijo que lo encuentre primero debe comunicarse con el padre mediante una señal guardando
el nonce en una fifo para que el padre pueda leerla. Hacer otra versión pero utilizando tuberías.
'''

#!/usr/bin/python3

import os, signal, psutil
from noblock import NoBlock



class HashParser():
    def __init__(self, fifoPath: str = "/", fifoName: str = "fifo") -> None:
        self.fifopath = (fifoPath + fifoName)
        os.mkfifo(self.fifopath)

    def run(self, seed: str, nonce: int = 0, difficulty: int = 1, childsAmount: int = 2):
        signal.signal(signal.SIGINT, self.readFifo)
        if self.mksubp(childsAmount):
            block = NoBlock(seed, nonce, difficulty)
            hash, nonce = block.proof_of_work()
            ppid = os.getppid()
            os.kill(ppid, 2)
            with open(self.fifopath, "a") as fifo:
                fifo.write(f'{nonce}\n{hash})
        else:
            signal.pause()

    def readFifo(self, uno, dos):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        with open(self.fifopath, "r") as fifo:
            result = fifo.readlines()
        parent = psutil.Process(os.getpid())
        for child in parent.children(recursive=True):
            child.kill()
        os.unlink(self.fifopath)
        print(f'nonce: {result[0]}hash: {result[1]}')

    def mksubp(self, childs):
        for child in range(0, childs):
            self.pid = os.fork()
            if self.pid == 0:
                return True
        return False

if __name__ == "__main__":
    app = HashParser(
        '/home/andres/Documentos/Facultad/Computacion_II/Computacion_2023/GitHub/Computacion-II-2023/Noblock/',
        'fifo1')
    app.run("hash test1 *172sppo4er", 0, 6, 100)
