'''
2 - Analizar el comportamiento de el programa queue0.py y explicarlo. Usar Queue.join(), Thead.join().
Ejecutar el hilo deamon=True y deamon=False.
'''
#!/usr/bin/python3

import threading, queue

q = queue.LifoQueue()
#q = queue.Queue()   # FIFO

def worker():
    while True:
        item = q.get()
        print('Working on '+str(item))
        print('Finished '+str(item))
        #Marcar tareas de la cola como realizadas.
        q.task_done()

# turn-on the worker thread. Un hilo daemon ejecutan tareas en segundo plano.
th = threading.Thread(target=worker, daemon=True)
th.start()

# send thirty task requests to the worker
for item in range(30):
    print('Putting item '+str(item))
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done. Notifica cuando todas las tareas se hayan realizado.
q.join()
#Forma de que un subproceso se bloquee hasta que otro subproceso haya terminado.
#th.join()
print('All work completed')
