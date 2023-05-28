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
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# turn-on the worker thread
th = threading.Thread(target=worker, daemon=True)
th.start()

# send thirty task requests to the worker
for item in range(30):
    print(f'Putting item {item}')
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')
