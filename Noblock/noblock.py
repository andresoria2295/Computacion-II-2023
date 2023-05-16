'''
1- Considerando el programa noblock.py, realizando un programa que lance dos procesos hijos
que intenten encontrar el nonce para un No-Bloque con una dificultad dada.
El hijo que lo encuentre primero debe comunicarse con el padre mediante una señal guardando
el nonce en una fifo para que el padre pueda leerla. Hacer otra versión pero utilizando tuberías.

Extracción de código en https://github.com/satwikkansal/python_blockchain_app
'''

#!/usr/bin/python3

from hashlib import sha256
import json, random

class NoBlock:
    def __init__(self, seed: str, nonce: int = 0, difficulty: int = 1):
        self.seed = seed
        self.nonce = nonce
        self.difficulty = difficulty

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest() #Devuelve el hash del bloque

    def proof_of_work(block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * block.difficulty):
            block.nonce += random.randint(1, 9)*random.randint(1, 9)
            computed_hash = block.compute_hash()
        return computed_hash, block.nonce

# b = NoBlock(seed='La semilla que quiera', nonce=0)
# h = b.compute_hash()
# new_hash = proof_of_work(b)
# print(new_hash)

​
